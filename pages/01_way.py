import streamlit as st

st.title("게임방법")

st.write("1. **1-100까지 범위**에서 숫자 하나를 이미 함지고가 골라놨다!")
st.write("2. 함지고에게 질문하며 **함지고가 고른 정답**을 찾아가라!")
st.subheader("과연 함지고의 생각을 읽어 숫자를 맞출 수 있을까?!")

btn_s = st.button("게임시작")

if btn_s:
    st.switch_page("pages/02_start.py")