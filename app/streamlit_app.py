import streamlit as st

st.title(":material/vpn_key: Day 1: Connect to Snowflake")

# Snowflake への接続
try:
    # SiS での接続
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    # Streamlit Community Cloudやローカルでの接続
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create()

# Snowflakeバージョンのクエリ
version = session.sql("SELECT CURRENT_VERSION()").collect()[0][0]

# 結果の表示
st.success(f"Successfully connected! Snowflake Version: {version}")