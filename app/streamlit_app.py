import streamlit as st

# ページ設定
st.set_page_config(
    page_title="30 Days Of AI with Streamlit",
    page_icon=":material/ac_unit:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ナビゲーション設定
pg = st.navigation({
    "Home": [
        st.Page("pages/00_home.py", title="30 Days of AI Home", icon=":material/home:"),
    ],
    "Week 1: LLM コール、ストリーミング、キャッシング": [
        st.Page("pages/01_connect_to_snowflake.py", title="Day 1: Snowflake接続", icon=":material/vpn_key:"),
        st.Page("pages/02_hello_cortex.py", title="Day 2: Hello Cortex", icon=":material/smart_toy:"),
        st.Page("pages/03_write_stream.py", title="Day 3: 書き出しストリーミング", icon=":material/airwave:"),
        st.Page("pages/04_caching_app.py", title="Day 4: キャッシング", icon=":material/cached:"),
        # st.Page("pages/day_5.py", title="Day 5: xxx", icon=":material/question:"),
        # st.Page("pages/day_6.py", title="Day 6: xxx", icon=":material/cached:"),
        # st.Page("pages/day_7.py", title="Day 7: xxx", icon=":material/cached:"),
    ],
    "Week 2: チャットUI、セッションステート": [
        # st.Page("pages/day_8.py", title="Day 1: Snowflake接続", icon=":material/vpn_key:"),
        # st.Page("pages/day_9.py", title="Day 2: Hello Cortex", icon=":material/smart_toy:"),
        # st.Page("pages/day_10.py", title="Day 3: 書き出しストリーミング", icon=":material/airwave:"),
        # st.Page("pages/day_11.py", title="Day 4: キャッシング", icon=":material/cached:"),
        # st.Page("pages/day_12.py", title="Day 5: xxx", icon=":material/question:"),
        # st.Page("pages/day_13.py", title="Day 6: xxx", icon=":material/cached:"),
        # st.Page("pages/day_14.py", title="Day 7: xxx", icon=":material/cached:"),
    ],
    "Week 3: RAGアプリ": [
        # st.Page("pages/day_15.py", title="Day 1: Snowflake接続", icon=":material/vpn_key:"),
        # st.Page("pages/day_16.py", title="Day 2: Hello Cortex", icon=":material/smart_toy:"),
        # st.Page("pages/day_17.py", title="Day 3: 書き出しストリーミング", icon=":material/airwave:"),
        # st.Page("pages/day_18.py", title="Day 4: キャッシング", icon=":material/cached:"),
        # st.Page("pages/day_19.py", title="Day 5: xxx", icon=":material/question:"),
        # st.Page("pages/day_20.py", title="Day 6: xxx", icon=":material/cached:"),
        # st.Page("pages/day_21.py", title="Day 7: xxx", icon=":material/cached:"),
    ],
    "Week 4: マルチモーダルAI、自動化エージェント": [
        # st.Page("pages/day_22.py", title="Day 1: Snowflake接続", icon=":material/vpn_key:"),
        # st.Page("pages/day_23.py", title="Day 2: Hello Cortex", icon=":material/smart_toy:"),
        # st.Page("pages/day_24.py", title="Day 3: 書き出しストリーミング", icon=":material/airwave:"),
        # st.Page("pages/day_25.py", title="Day 4: キャッシング", icon=":material/cached:"),
        # st.Page("pages/day_26.py", title="Day 5: xxx", icon=":material/question:"),
        # st.Page("pages/day_27.py", title="Day 6: xxx", icon=":material/cached:"),
        # st.Page("pages/day_28.py", title="Day 7: xxx", icon=":material/cached:"),
    ]
})

# ナビゲーション実行
pg.run()