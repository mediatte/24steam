# from dotenv import load_dotenv
# load_dotenv()

# from langchain_openai import ChatOpenAI
from langchain_openai import ChatOpenAI
import streamlit as st

llm = ChatOpenAI()



st.title('게임 닉네임 추천 프로그램')

title = st.text_input("당신의 이름을 입력해주세요.")

if title :
    result = llm.predict(title + "의 이름을 가지고 게임 닉네임을 한글 8글자 이내로 3개 만들어줘. 닉네임은 이름과 잘 어울리고 개성이 있어야 해. 이걸 잘 하면 200달러를 줄게.")
    st.write(title + "의 게임 닉네임 추천")
    st.write(result)


