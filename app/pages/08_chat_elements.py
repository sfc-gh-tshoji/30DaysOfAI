import streamlit as st

st.title(":material/chat: Day 8: Meet the Chat Elements")

# サイドバー設定
with st.sidebar:
    # クイックスタートボタン
    if st.button("🏃‍♂️ 次へ進む", type="primary", use_container_width=True):
        st.switch_page("pages/09_session_state.py")
    
    # フッター
    st.divider()
    st.caption("Day 8: Meet the Chat Elements | 30 Days of AI")

# 1. 静的メッセージの表示
with st.chat_message("user"):
    st.write("こんにちは！Streamlitが何か、説明していただけますか？")

with st.chat_message("assistant"):
    st.write("Streamlitは、データアプリを構築するためのオープンソースのPythonフレームワークです。")
    st.bar_chart([10, 20, 30, 40])

# 2. Chat Input ウィジェット
prompt = st.chat_input("メッセージをこちらに入力してください...")

# 3. 入力に対する反応
if prompt:
    # ユーザーの新規メッセージを表示
    with st.chat_message("user"):
        st.write(prompt)
    
    # アシスタントの回答モックの表示
    with st.chat_message("assistant"):
        st.write(f"あなたは今、次のように言いました:\n\n'{prompt}'\n\n（私はまだメモリ機能を持っていません)")
