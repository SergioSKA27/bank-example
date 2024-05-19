import bcrypt
import streamlit as st
from components import MySQLClient



def registration(client: MySQLClient):
    with st.container(border=True):
        st.title('Registro de Usuario')
        name = st.text_input('Nombre')
        last_name = st.text_input('Apellido')
        email = st.text_input('Correo Electronico')
        password = st.text_input('Contraseña', type='password')
        rpt_password = st.text_input('Repetir Contraseña', type='password')
        register = st.button('Registrar',use_container_width=True)
        
        if register:
            if password == rpt_password:
                user = {
                    'Nombre': name,
                    'Apellido': last_name,
                    'CorreoElectronico': email,
                    'Contraseña': bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                }
                if client.insert_user(user):
                    st.toast('Usuario registrado exitosamente', icon=':material/thumb_up:' )
                else:
                    st.toast('Error al registrar usuario', icon='❗')
            else:
                st.error('Las contraseñas no coinciden',icon=':material/error:')
        