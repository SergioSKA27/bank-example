import streamlit as st 


def login():
    with st.container(border=True):
        st.title('Login')
        #email = st.text_input('Email')
        #password = st.text_input('Password', type='password')
        login = st.button('Login')
        if login:
            st.write('Login Successful')



