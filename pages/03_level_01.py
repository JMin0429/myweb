import streamlit as st

st.title("진짜 게임을 시작하지. <Level 01>")

st.subheader("1-1000 범위에서 수 하나를 골랐다.")
st.write("과연 이번에도 맞출 수 있을까?")

정답 = 355
입력 = st.number_input("**함지고**가 고른 숫자는?",1,1000)

if 정답 > 입력:
    st.write("함지고 : **아직 많이 부족하다!**")
elif 정답 < 입력:
    st.write("함지고 : **욕심이 많구만!**")
else:
    st.subheader("함지고 : 이걸 맞추다니!")
    st.write("제1회 입학식 : 355명(11학급)")
    btn_02 = st.button("다음으로")
    if btn_02:
        st.switch_page("pages/04_level_02.py")

btn_g = st.button("돌아가기")
btn_h2 = st.button("힌트")

if btn_g:
    st.switch_page("game.py")
if btn_h2:
    st.write("함지고 : **제1회 입학식에서 입학한 입학생 수**")