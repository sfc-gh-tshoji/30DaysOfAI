import streamlit as st
from snowflake.snowpark.functions import ai_complete
import json

st.title(":material/smart_toy: Day 2: Hello, Cortex!")

# Snowflake への接続
try:
    # SiS での接続
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    # Streamlit Community Cloudやローカルでの接続
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create()


# モデルおよびプロンプト
model = 'openai-gpt-5.2'
prompt = st.text_input("プロンプトを入力してください:")

# LLM推論の実行
if st.button("回答の生成"):
    df = session.range(1).select(
        ai_complete(model=model, prompt=prompt).alias("response")
    )
    
    # レスポンスの取得と表示
    response_raw = df.collect()[0][0]
    response = json.loads(response_raw)
    st.write(response)

# フッター
st.divider()
st.caption("Day 2: Hello, Cortex! | 30 Days of AI")