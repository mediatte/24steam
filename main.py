from langchain_openai import ChatOpenAI
import streamlit as st

llm = ChatOpenAI()



st.title('이름 뜻 풀이 프로그램')

title = st.text_input("당신의 이름을 입력해주세요.")

if title :
    result = llm.predict(title + "의 이름 뜻 풀이를 해줘.")
    st.write(title + "의 이름 뜻풀이")
    st.write(result)


