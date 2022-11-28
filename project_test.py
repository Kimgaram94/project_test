import streamlit as st
import joblib
import numpy as np

# 타이틀 설정
st.title('책 제목을 통한 유사 도서 추천')

def main():
    st.text_input("책 제목을 입력해주세요")
    
    st.title(fname)
    
    if st.button("click button"):
        st.write("검색")
    