import streamlit as st

st.title("여기까지 용케 왔군.<Final Level>")
st.subheader("마지막은 1-100,000,000 범위이다!!")

정답 = 20080301
입력 = st.number_input("**함지고**가 고른 숫자는?",1,100000000)

if 정답 > 입력:
    st.write("함지고 : **아직 많이 부족하다!**")
elif 정답 < 입력:
    st.write("함지고 : **욕심이 많구만!**")
else:
    st.subheader("함지고에 대해서 많이 알고 있구나!!")
    st.write("함지고의 설립일자 : 2008년 03월 01일")
    st.title("감사합니다.")
 

btn_g = st.button("돌아가기")
btn_h3 = st.button("힌트")

if btn_g:
    st.switch_page("game.py")
if btn_h3:
    st.write("함지고 : **함지고의 설립일자** -> 예를 들어 1234년 56월 78일이라면 쉼표없이 12345678로 입력!")