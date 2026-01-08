import streamlit as st
import json
from snowflake.snowpark.functions import ai_complete

# Snowflake への接続
try:
    # SiS での接続
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    # Streamlit Community Cloudやローカルでの接続
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create()

# キャッシュされるCortex AI関数
@st.cache_data
def call_cortex_llm(prompt_text):
    # モデル
    model = 'openai-gpt-5.2'

    # AI_COMPLETE実行
    df = session.range(1).select(
        ai_complete(model=model, prompt=prompt_text).alias("response")
    )

    # 回答の取得とパース
    response_raw = df.collect()[0][0]
    response_json = json.loads(response_raw)
    return response_json

# --- App UI ---
st.title(":material/post: Day 5: LinkedIn Post Generator")

# Inputウィジェット
content = st.text_input("コンテンツURL:", "https://docs.snowflake.com/en/user-guide/views-semantic/overview")
tone = st.selectbox("トーン:", ["プロフェッショナル", "カジュアル", "愉快"])
word_count = st.slider("ワード数:", 50, 300, 100)

# 生成ボタン
if st.button("ポスト生成"):
    # プロンプトの構成
    prompt = f"""
    あなたはソーシャルメディア管理のエキスパートです。次の情報をもとにLinkedIn用のポストを生成してください:

    トーン: {tone}
    望ましい長さ: おおよそ {word_count} 文字
    コンテンツとして使用するURL: {content}

    LinkedInポスト用のテキストのみを生成してください。箇条書きには - を使用してください。
    """

    response = call_cortex_llm(prompt)
    
    st.subheader("生成されたポスト:")
    st.markdown(response)

# クイックスタートボタン
if st.button("🏃‍♂️ 次へ進む", type="primary", use_container_width=True):
    st.switch_page("pages/06_post_generator_v2.py")

# フッター
st.divider()
st.caption("Day 5: Post Generator App | 30 Days of AI")