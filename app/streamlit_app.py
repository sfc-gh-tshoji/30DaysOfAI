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
        st.Page("pages/05_post_generator.py", title="Day 5: ポスト生成アプリ", icon=":material/post:"),
        st.Page("pages/06_post_generator_v2.py", title="Day 6: 長時間タスクのステータスUIつきアプリ", icon=":material/psychology:"),
        st.Page("pages/07_post_generator_v3.py", title="Day 7: テーマ、レイアウト設定", icon=":material/side_navigation:"),
    ],
    "Week 2: チャットUI、セッションステート": [
        st.Page("pages/08_chat_elements.py", title="Day 8: チャットUI基礎", icon=":material/chat:"),
        st.Page("pages/09_session_state.py", title="Day 9: セッションステート", icon=":material/memory:"),
        st.Page("pages/10_first_chatbot.py", title="Day 10: 初めてのチャットボット", icon=":material/chat:"),
        st.Page("pages/11_display_chat_history.py", title="Day 11: チャット履歴の表示", icon=":material/chat:"),
        st.Page("pages/12_streaming_response.py", title="Day 12: 回答のストリーミング", icon=":material/airwave:"),
        st.Page("pages/13_adding_system_prompt.py", title="Day 13: システムプロンプトの追加", icon=":material/theater_comedy:"),
        st.Page("pages/14_adding_avatars_and_error_handling.py", title="Day 14: アバター追加とエラーハンドリング", icon=":material/account_circle:"),
    ],
    "Week 3: RAGアプリ": [
        # st.Page("pages/15_.py", title="Day 15: xxx", icon=":material/vpn_key:"),
        # st.Page("pages/16_.py", title="Day 16: xxx", icon=":material/smart_toy:"),
        # st.Page("pages/17_.py", title="Day 17: xxx", icon=":material/airwave:"),
        # st.Page("pages/18_.py", title="Day 18: xxx", icon=":material/cached:"),
        # st.Page("pages/19_.py", title="Day 19: xxx", icon=":material/question:"),
        # st.Page("pages/20_.py", title="Day 20: xxx", icon=":material/cached:"),
        # st.Page("pages/21_.py", title="Day 21: xxx", icon=":material/cached:"),
    ],
    "Week 4: マルチモーダルAI、自動化エージェント": [
        # st.Page("pages/22_.py", title="Day 1: xxx", icon=":material/vpn_key:"),
        # st.Page("pages/23_.py", title="Day 2: xxx", icon=":material/smart_toy:"),
        # st.Page("pages/24_.py", title="Day 3: xxx", icon=":material/airwave:"),
        # st.Page("pages/25_.py", title="Day 4: xxx", icon=":material/cached:"),
        # st.Page("pages/26_.py", title="Day 5: xxx", icon=":material/question:"),
        # st.Page("pages/27_.py", title="Day 6: xxx", icon=":material/cached:"),
        # st.Page("pages/28_.py", title="Day 7: xxx", icon=":material/cached:"),
    ]
})

# ナビゲーション実行
pg.run()