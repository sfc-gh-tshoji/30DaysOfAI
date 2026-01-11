# 30 Days of AI with Streamlit

SnowflakeとStreamlitを使って、30日間でAI開発の基礎から応用までを学ぶ学習プログラムです。

## 概要

このリポジトリは、TSHOJIがSnowflake Cortex AIとStreamlitを組み合わせた実践的なAIアプリケーション開発を学ぶためのチュートリアルに取り組むための作業リポジトリです。

## カリキュラム

### Week 1: LLMコール、ストリーミング、キャッシング
- Day 1: Snowflake接続
- Day 2: Hello Cortex (AI関数の基本)
- Day 3: 書き出しストリーミング
- Day 4: キャッシング
- Day 5-7: ポスト生成アプリの構築

### Week 2: チャットUI、セッションステート
- Day 8: チャットUI基礎
- Day 9: セッションステート
- Day 10: 初めてのチャットボット
- Day 11-14: (準備中)

### Week 3: RAGアプリ
- (準備中)

### Week 4: マルチモーダルAI、自動化エージェント
- (準備中)

## プロジェクト構成

```
app/
├── streamlit_app.py      # メインエントリーポイント
├── pyproject.toml        # SiSコンテナランタイム用設定ファイル
├── pages/                # 各日のチュートリアルページ
│   ├── 00_home.py
│   ├── 01_connect_to_snowflake.py
│   ├── 02_hello_cortex.py
│   └── ...
└── .streamlit/           # Streamlit設定
```

## 必要環境

- Snowflakeアカウント
- Streamlit

## リンク

- [30 Days of AI チャレンジアプリ](https://30daysofai.streamlit.app/)
