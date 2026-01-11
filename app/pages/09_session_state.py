import streamlit as st

st.title(":material/memory: Day 9: Understanding Session State")

# サイドバー設定
with st.sidebar:
    # クイックスタートボタン
    if st.button("🏃‍♂️ 次へ進む", type="primary", use_container_width=True):
        st.switch_page("pages/10_first_chatbot.py")
    
    # フッター
    st.divider()
    st.caption("Day 9: Understanding Session State | 30 Days of AI")

st.warning("**手順:** 両方の列の + と - ボタンをクリックして、違いを確認してみてください")

# 比較するための2カラムを作成
col1, col2 = st.columns(2)

# --- COLUMN 1: 誤った方法 ---
with col1:
    st.header(":material/cancel: 通常変数")
    st.write("クリックの度にリセットされます")

    # この行は、ページ上にあるいずれのボタンをクリックしても毎回実行されます
    # これにより、進捗は即座に消去されます
    count_wrong = 0

    # ここでは + と - ボタンを並べて配置するためにネストしたカラムを使用しています
    subcol_left, subcol_right = st.columns(2)

    with subcol_left:
        # 注意: 各ボタンには一意の "key" を与える必要があります
        if st.button(":material/add:", key="std_plus"):
            count_wrong += 1

    with subcol_right:
        if st.button(":material/remove:", key="std_minus"):
            count_wrong -= 1
        
    st.metric("標準カウント", count_wrong)
    st.caption("計算が実行される前に count_wrong が 0 にリセットされるため、1 または -1 を超えることはありません。")


# --- COLUMN 2: 正しい方法 ---
with col2:
    st.header(":material/check_circle: セッションステート")
    st.write("メモリを保持します")

    # 1. 初期化: まだ存在しない場合にだけ Key を作成
    if "counter" not in st.session_state:
        st.session_state.counter = 0

    # ここでもネストしたカラムを使用
    subcol_left_2, subcol_right_2 = st.columns(2)

    with subcol_left_2:
        # 2. 変更: 辞書の値を更新（増加）
        if st.button(":material/add:", key="state_plus"):
            st.session_state.counter += 1

    with subcol_right_2:
        # 2. 変更: 辞書の値を更新（減少）
        if st.button(":material/remove:", key="state_minus"):
            st.session_state.counter -= 1
    
    # 3. 読み込み: 値を表示
    st.metric("ステートカウント", st.session_state.counter)
    st.caption("これが機能するのは、Counter が存在しない場合にのみ値を 0 に設定するためです")
