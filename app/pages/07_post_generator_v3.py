import streamlit as st
import json
import time
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

st.title(":material/post: Day 7: LinkedIn Post Generator v3")
st.success("入力されたリンクのコンテンツを使用して、LinkedInポストを生成するアプリ")    

# Inputウィジェット
st.subheader(":material/input: コンテンツ入力")
content = st.text_input("コンテンツURL:", "https://docs.snowflake.com/en/user-guide/views-semantic/overview")

# サイドバー設定 - トーン、ワード数などの調整用ウィジェットとフッター等
with st.sidebar:
    tone = st.selectbox("トーン:", ["プロフェッショナル", "カジュアル", "愉快"])
    word_count = st.slider("ワード数:", 50, 300, 100)
    
    # クイックスタートボタン
    if st.button("🏃‍♂️ 次へ進む", type="primary", use_container_width=True):
        st.switch_page("pages/08_chat_elements.py")
    
    # フッター
    st.divider()
    st.caption("Day 7: Post Generator App v3 | 30 Days of AI")

# 生成ボタン
if st.button("ポスト生成"):

    # ステータスコンテナの初期化
    with st.status("エンジンをスタートしています...", expanded=True) as status:

        # Step 1: プロンプトの構成
        st.write(":material/psychology: 思考中: 制約とトーンを分析しています...")
        prompt = f"""
        あなたはソーシャルメディア管理のエキスパートです。次の情報をもとにLinkedIn用のポストを生成してください:
    
        トーン: {tone}
        望ましい長さ: おおよそ {word_count} 文字
        コンテンツとして使用するURL: {content}
    
        LinkedInポスト用のテキストのみを生成してください。箇条書きには - を使用してください。
        """

        # Step 2: APIコール
        st.write(":material/flash_on: 生成中: Snowflake Cortex へ接続しています...")        
        
        # 短時間のディレイを追加
        time.sleep(2)

        # Cortexコール
        response = call_cortex_llm(prompt)

        # Step 3: 完了に伴うステータス更新
        st.write(":material/check_circle: ポスト生成が完了しました！")
        status.update(label="ポスト生成に成功！", state="complete", expanded=False)
    
    st.subheader("生成されたポスト:")
    st.markdown(response)