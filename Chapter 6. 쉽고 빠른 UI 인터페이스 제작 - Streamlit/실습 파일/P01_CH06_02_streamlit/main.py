import streamlit as st

st.title("AI tutor Title")
st.subheader("sub header")
st.write("hello world")

"""
# This is title
## This is sub title
### This is sub title

- 첫번째
- 두번째
- 세번째
"""

text = st.text_input("text input")
st.write(text)

gender = st.selectbox('성별', ('남자', '여자'))
st.write(f"gender: {gender}")

selected = st.checkbox("동의하시겠습니까?")

if selected:
    st.success("동의했습니다.")


options = st.multiselect('취미', ['음악 감상', '독서', '게임'])
st.write(', '.join(options))

with st.sidebar:
    add_radio = st.radio("언어 선택", ("한국어", "영어"))


col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
