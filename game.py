import streamlit as st

st.title("숫자 맞추기 게임")

btn_s = st.button("게임시작")
btn_w = st.button("게임방법")

if btn_s:
    st.switch_page("start.py")
if btn_w:
    st.switch_page("way.py")