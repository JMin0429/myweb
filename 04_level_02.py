import streamlit as st

st.title("쉽지 않을 걸?! <Level 02>")

정답 = 4250
입력 = st.number_input("**함지고**가 고른 숫자는?",1,10000)

if 정답 > 입력:
    st.write("함지고 : **더 올려라!**")
elif 정답 < 입력:
    st.write("함지고 : **더 낮춰라!**")
else:
    st.subheader("함지고 : 내 마음을 꿰둟었군.")
    st.write("함지고 주소는 대구광역시 북구 학정로42길 50")

btn_g = st.button("돌아가기")
btn_h3 = st.button("힌트")

if btn_g:
    st.switch_page("game.py")
if btn_h3:
    st.write("함지고 : 함지고 주소 (**대구광역시 북구 학정로 OO길 OO**) -> 정답은 OOOO으로 작성!")