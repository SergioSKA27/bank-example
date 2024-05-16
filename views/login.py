import streamlit as st 
from components.validators import Validator
from components.mysql_client import MySQLClient
from components.session_handler import SessionHandler




def login(client: MySQLClient):
    if 'session' not in st.session_state:
        st.session_state.session = SessionHandler(client)
    else:
        # Si la sesion ya esta activa, redirigir a la pagina principal
        if st.session_state.session.is_active():
            st.switch_page('app.py')

    with st.container(border=True):
        st.title('Login')
        email = st.text_input('Email')
        password = st.text_input('Password', type='password')
        validate = Validator(client)
        login = st.button('Login')
        if login:
            if validate.validate_user(email, password):
                st.toast('Sesion iniciada correctamente', icon=':material/sentiment_satisfied:')
                st.session_state.session.start_session(email)
            else:
                st.error('Fallo al iniciar Sesion',icon=":material/sentiment-dissatisfied:")



