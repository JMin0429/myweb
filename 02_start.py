import streamlit as st

st.title("숫자 맞추기 게임")
st.write("참고 : 힌트를 보면 길이 쉽게 열릴 것이다.")

정답 = 27
입력 = st.number_input("**함지고**가 고른 숫자는?",1,100)

if 정답 > 입력:
    st.write("함지고 : **더 올려라!**")
elif 정답 < 입력:
    st.write("함지고 : **더 낮춰라!**")
else:
    st.subheader("함지고 : 내 마음을 꿰둟었군.")
    st.write("1학년 : 8학급,  2학년 : 9학급,  3학년 : 8학급 -> 총 27학급")
    btn_01 = st.button("다음으로")
    if btn_01:
        st.switch_page("pages/03_level_01.py")

btn_g = st.button("돌아가기")
btn_h1 = st.button("힌트")

if btn_g:
    st.switch_page("game.py")
if btn_h1:
    st.write("함지고 : **2024년 현재 운영되고 있는 학급수**")