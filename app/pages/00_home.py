import streamlit as st

# ページ設定
st.set_page_config(
    page_title="30 Days Of AI with Streamlit",
    page_icon=":material/ac_unit:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# メインタイトル
st.title(":material/ac_unit: 30 Days Of AI with Streamlit Learning Journey")

# メインコンテンツエリア
if 'current_page' not in st.session_state:
    # ホームページコンテンツ
    st.markdown("""
    ## 🚀 AI学習の旅へようこそ！
    
    この30日間のプログラムで、SnowflakeとAIの基礎から応用まで学習できます。
    
    ### 📖 学習内容
    - **Week 1**: Snowflakeへの接続、Cortex AI関数のコール、ストリーミングやキャッシングの実装方法
    - **Week 2**: チャットUIの実装と、セッションステートの使用方法
    - **Week 3**: RAGアプリの実装
    - **Week 4**: マルチモーダルAIと自動化エージェントの構築
    
    ### 🎯 目標
    - Snowflakeの基本操作をマスター
    - AIを活用したデータ活用スキルの習得
    - 実用的なアプリ、エージェントの作成
    
    ### 🔗 リンク
    [30 Days of AI チャレンジアプリ](https://30daysofai.streamlit.app/)
    """)
    
    # クイックスタートボタン
    if st.button("🏃‍♂️ 学習を始める", type="primary", use_container_width=True):
        st.switch_page("pages/01_connect_to_snowflake.py")

# フッター
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        <small>🎓 30 Days of AI with Snowflake | Built with Streamlit</small>
    </div>
    """, 
    unsafe_allow_html=True
)