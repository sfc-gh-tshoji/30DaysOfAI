import streamlit as st
import time
import json
from snowflake.snowpark.functions import ai_complete

st.title(":material/cached: Day 4: Caching App")

# Snowflake への接続
try:
    # SiS での接続
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    # Streamlit Community Cloudやローカルでの接続
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create()

# Cortex実行関数の定義とキャッシング
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

prompt = st.text_input("プロンプトを入力してください:", "Snowflakeの概要を教えて")

if st.button("実行"):
    start_time = time.time()
    response = call_cortex_llm(prompt)
    end_time = time.time()

    st.success(f"*実行に {end_time - start_time:.2f} 秒かかりました*")
    st.write(response)

# クイックスタートボタン
if st.button("🏃‍♂️ 次へ進む", type="primary", use_container_width=True):
    st.switch_page("pages/day_5.py")

# フッター
st.divider()
st.caption("Day 4: Caching App | 30 Days of AI")