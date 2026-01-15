import streamlit as st
import json
from snowflake.snowpark.functions import ai_complete 
import time

# Snowflake への接続
try:
    # SiS での接続
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    # Streamlit Community Cloudやローカルでの接続
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create()

def call_cortex(prompt_text: str) -> str:
    # Snowflake Cortex AI_COMPLETE実行
    df = session.range(1).select(
        ai_complete(model=model, prompt=prompt_text).alias("response")
    )

    # 回答の取得とパース
    response_raw = df.collect()[0][0]
    response_json = json.loads(response_raw)

    # 回答からテキストを抽出
    if isinstance(response_json, dict):
        return response_json.get("choices", [{}])[0].get("messages", "")
    
    return str(response_json)

# --- App UI ---

st.title(":material/chat: Day 12: Chatbot with Streaming")

# セッションステート内のメッセージリストを初期化
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "こんにちは！私はCortex AIアシスタントです。今日はどのようにお手伝いしましょうか？"}
    ]

# 履歴から全てのメッセージを表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# サイドバー設定
with st.sidebar:
    st.header("会話スタッツ")
    
    user_msgs = len([m for m in st.session_state.messages if m["role"] == "user"])
    assistant_msgs = len([m for m in st.session_state.messages if m["role"] == "assistant"])
    
    st.metric("あなたのメッセージ", user_msgs)
    st.metric("AIの回答", assistant_msgs)
    
    if st.button("履歴のクリア"):
        st.session_state.messages = [
            {"role": "assistant", "content": "こんにちは！私はCortex AIアシスタントです。今日はどのようにお手伝いしましょうか？"}
        ]
        st.rerun()

    # モデル選択
    models_list = ['openai-gpt-5.2', 'claude-sonnet-4-5', 'gemini-3-pro']
    model = st.selectbox("モデルを選んでください", models_list)
    
    # クイックスタートボタン
    if st.button("🏃‍♂️ 次へ進む", type="primary", use_container_width=True):
        st.switch_page("pages/13_adding_system_prompt.py")
    
    # フッター
    st.divider()
    st.caption("Day 12: Chatbot with Streaming | 30 Days of AI")

# Chat input
if prompt := st.chat_input("何を知りたいですか？"):
    # ユーザーメッセージをステートに追加
    st.session_state.messages.append({"role": "user", "content": prompt})

    # ユーザーメッセージを表示
    with st.chat_message("user"):
        st.markdown(prompt)

    # コンテキストのためにすべての会話履歴を構築
    conversation = "\n\n".join([
        f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
        for msg in st.session_state.messages
    ])
    full_prompt = f"{conversation}\n\nAssistant:"

    # ストリーム生成
    def stream_generator():
        response_text = call_cortex(full_prompt)
        for word in response_text.split(" "):
            yield word + " "
            time.sleep(0.02)

    # アシスタントの回答を生成、表示
    with st.chat_message("assistant"):
        with st.spinner("思考中..."):
            response = st.write_stream(stream_generator)

    # アシスタントの回答をステートに追加
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()  # サイドバーのスタッツ更新のため強制リラン