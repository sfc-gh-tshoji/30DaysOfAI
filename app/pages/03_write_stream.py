import streamlit as st
from snowflake.cortex import Complete
import time

st.title(":material/airwave: Day 3: Write Streams")

# Snowflake への接続
try:
    # SiS での接続
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    # Streamlit Community Cloudやローカルでの接続
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create()

# モデル選択
models_list = ['openai-gpt-5.2', 'claude-4-sonnet', ]
model = st.selectbox("モデルを選んでください", models_list)

# プロンプト指定
example_prompt = 'Pythonとは何ですか'
prompt = st.text_input("プロンプトを入力してください:", example_prompt)

# ストリーミング手法の選択
streaming_method = st.radio(
    "ストリーミング手法:",
    ["直接(stream=true)", "カスタム生成"],
    help = '回答のストリーミング方法を選択します'
)

# LLM推論の実行
if st.button("回答の生成"):

    # Method 1: stream=true による直接ストリーミング
    if streaming_method == "直接(stream=true)":
        with st.spinner(f"{model}を使用して回答を生成中"):
            stream_generator = Complete(
                session = session,
                model = model,
                prompt = prompt,
                stream = True
            )

            st.write_stream(stream_generator)

    # Method 2: カスタム生成
    else:
        def custom_stream_generator():
            """
            ジェネレータが st.write_stream に互換性のない場合の代替手法
            """
            output = Complete(
                session = session,
                model = model,
                prompt = prompt,
            )

            for chunk in output:
                yield chunk
                time.sleep(0.01)    # スムースなストリーミングのために小さなディレイ

        with st.spinner(f"{model}を使用して回答を生成中"):
            st.write_stream(custom_stream_generator)

# クイックスタートボタン
if st.button("🏃‍♂️ 学習を始める", type="primary", use_container_width=True):
    st.switch_page("pages/04_caching_app.py")

# フッター
st.divider()
st.caption("Day 3: Write streams | 30 Days of AI")