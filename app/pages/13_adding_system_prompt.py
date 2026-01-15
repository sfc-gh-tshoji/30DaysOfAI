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

# Cortex AI_COMPLETE の実行と回答抽出
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

# ストリーム生成
def stream_generator():
    # コンテキストのためにすべての会話履歴を構築
    conversation = "\n\n".join([
        f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
        for msg in st.session_state.messages
    ])
    
    # システムプロンプトを含むプロンプトを作成
    full_prompt = f"""{st.session_state.system_prompt}
    これまでの会話はこちらです:{conversation}
    
    ユーザーの直近のメッセージに、キャラクターを維持したまま返信してください。
    """

    response_text = call_cortex(full_prompt)
    for word in response_text.split(" "):
        yield word + " "
        time.sleep(0.02)

# --- App UI ---

st.title(":material/chat: Day 13: Customizable Chatbot")

# セッションステート内のメッセージリストを初期化
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "こんにちは！私はCortex AIアシスタントです。今日はどのようにお手伝いしましょうか？特異なキャラクターをご希望であれば、サイドバーからパーソナリティを指定してください。"}
    ]

# 履歴から全てのメッセージを表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# サイドバー設定
with st.sidebar:
    st.header(":material/theater_comedy: チャットボットパーソナリティ")

    # プリセット パーソナリティ
    st.subheader("プリセット")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button(":material/sailing: 海賊"):
            st.session_state.system_prompt = "あなたはキャプテン・ジャックという名の、親切な海賊アシスタントです。海賊らしい言葉遣いをし、航海に関する比喩を使い、適切な場面では文末を「お分かり？」で締めくくります。"
            st.rerun()
    
    with col2:
        if st.button(":material/school: 教師"):
            st.session_state.system_prompt = "あなたは、忍耐強く励ます先生である福沢先生です。あなたは概念を明確に説明し、例を使用し、常に理解度を確認します。"
            st.rerun()

    col3, col4 = st.columns(2)
    with col3:
        if st.button(":material/mood: コメディアン"):
            st.session_state.system_prompt = "あなたはイノケン、気の利いたコメディアンアシスタントです。あなたは駄洒落、ジョーク、ユーモアが大好きですが、それでも本当に役に立ちます。あなたは、役立つ情報を提供する一方で、雰囲気を明るくします。"
            st.rerun()
    
    with col4:
        if st.button(":material/smart_toy: ロボット"):
            st.session_state.system_prompt = "あなたはUNIT-7、有能なロボットアシスタントです。正確で論理的な話し方をします。時折、回路や処理ユニットに言及することがあります。"
            st.rerun()
            
    st.divider()

    st.text_area(
        "システムプロンプト:",
        height=200,
        key="system_prompt"
    )

    st.divider()
    
    # 会話スタッツ
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

    st.divider()
    
    # モデル選択
    models_list = ['openai-gpt-5.2', 'claude-sonnet-4-5', 'gemini-3-pro']
    model = st.selectbox("モデルを選んでください", models_list)
    
    # クイックスタートボタン
    if st.button("🏃‍♂️ 次へ進む", type="primary", use_container_width=True):
        st.switch_page("pages/14_adding_avatars_and_error_handling.py")
    
    # フッター
    st.divider()
    st.caption("Day 13: Adding a System Prompt | 30 Days of AI")

# Chat input
if prompt := st.chat_input("何を知りたいですか？"):
    # ユーザーメッセージをステートに追加
    st.session_state.messages.append({"role": "user", "content": prompt})

    # ユーザーメッセージを表示
    with st.chat_message("user"):
        st.markdown(prompt)

    # アシスタントの回答を生成、表示
    with st.chat_message("assistant"):
        with st.spinner("思考中..."):
            response = st.write_stream(stream_generator)

    # アシスタントの回答をステートに追加
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()  # サイドバーのスタッツ更新のため強制リラン
