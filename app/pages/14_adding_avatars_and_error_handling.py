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

st.title(":material/account_circle: Day 14: Adding Avatars and Error Handling")

# 指定がない場合、システムプロンプトを初期化
if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = "あなたは有能なAIアシスタントです。"

# セッションステート内のメッセージリストを初期化
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "こんにちは！私はCortex AIアシスタントです。今日はどのようにお手伝いしましょうか？特異なキャラクターをご希望であれば、サイドバーからパーソナリティを指定してください。"}
    ]

# サイドバー設定
with st.sidebar:
    st.header(":material/settings: 設定")
    
    # アバターカスタマイズ
    st.subheader(":material/palette: あなたのアバター")
    user_avatar = st.selectbox(
        "あなたのアバター:",
        ["👤", "🧑‍💻", "👨‍🎓", "👩‍🔬", "🦸", "🧙"],
        index=0
    )
    
    assistant_avatar = st.selectbox(
        "アシスタントのアバター:",
        ["🤖", "🧠", "✨", "🎯", "💡", "🌟"],
        index=0
    )

    st.divider()
    
    # システムプロンプト
    st.subheader(":material/description: システムプロンプト")
    st.text_area(
        "動作のカスタマイズ:",
        height=100,
        key="system_prompt",
        help="AIの行動と回答の仕方を定義します"
    )
    
    st.divider()
    
    # エラーをシミュレーションするためのデバッグトグル
    st.subheader(":material/bug_report: デバッグモード")
    simulate_error = st.checkbox(
        "APIエラー シミュレーション",
        value=False,
        help="エラー処理メカニズムをテストするためにこれを有効にします"
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
    
    # # クイックスタートボタン
    # if st.button("🏃‍♂️ 次へ進む", type="primary", use_container_width=True):
    #     st.switch_page("pages/14_adding_avatars_and_error_handling.py")
    
    # フッター
    st.divider()
    st.caption("Day 14: Adding Avatars and Error Handling | 30 Days of AI")

# カスタムアバターと合わせて履歴から全てのメッセージを表示
for message in st.session_state.messages:
    avatar = user_avatar if message["role"] == "user" else assistant_avatar
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("何を知りたいですか？"):
    # ユーザーメッセージをステートに追加
    st.session_state.messages.append({"role": "user", "content": prompt})

    # ユーザーメッセージを表示
    with st.chat_message("user", avatar=user_avatar):
        st.markdown(prompt)

    # アシスタントの回答を生成、表示
    with st.chat_message("assistant", avatar=assistant_avatar):
        try:
            if simulate_error:
                raise Exception("Simulated API error: Service temporarily unavailable (429)")
                
            with st.spinner("思考中..."):
                response = st.write_stream(stream_generator)
                
            # アシスタントの回答をステートに追加
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()  # サイドバーのスタッツ更新のため強制リラン
        
        except Exception as e:
            error_message = f"I encountered an error: {str(e)}"
            st.error(error_message)
            st.info(":material/lightbulb: **Tip:** This might be a temporary issue. Try again in a moment, or rephrase your question.")
