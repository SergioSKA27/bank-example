import bcrypt
import streamlit as st
from components import MySQLClient





COUNTRY = ['Colombia', 'Venezuela', 'Peru', 'Ecuador', 'Argentina', 'Chile', 'Brasil', 'Uruguay', 'Paraguay', 'Bolivia',
           'Panama', 'Costa Rica', 'Nicaragua', 'Honduras', 'El Salvador', 'Guatemala', 'Mexico', 'Estados Unidos', 'Canada',
           'España', 'Francia', 'Alemania', 'Italia', 'Portugal', 'Inglaterra', 'Holanda', 'Belgica', 'Suiza', 'Suecia', 'Noruega',
           'Finlandia', 'Dinamarca', 'Rusia', 'China', 'Japon', 'Corea del Sur', 'India', 'Australia', 'Nueva Zelanda', 'Sudafrica',
           'Egipto', 'Marruecos', 'Argelia', 'Tunez', 'Libia', 'Nigeria', 'Ghana', 'Camerun', 'Sudan', 'Etiopia', 'Kenia', 'Uganda',
           'Tanzania', 'Zambia', 'Zimbabwe', 'Mozambique', 'Madagascar', 'Angola', 'Congo', 'RDC', 'Gabon', 'Congo', 'Cabo Verde',
           'Mauritania', 'Mali', 'Niger', 'Chad', 'Burkina Faso', 'Benin', 'Togo', 'Costa de Marfil', 'Senegal', 'Guinea', 'Guinea Bissau',
           'Sierra Leona', 'Liberia', 'Gambia', 'Burundi', 'Ruanda', 'Uganda', 'Sudan del Sur', 'Eritrea', 'Djibouti', 'Somalia', 'Yemen',
           'Oman', 'Emiratos Arabes Unidos', 'Qatar', 'Kuwait', 'Arabia Saudi', ]

def registration(client: MySQLClient):
    with st.container(border=True):
        st.title('Registro de Usuario')
        name = st.text_input('Nombre')
        last_name = st.text_input('Apellido')
        email = st.text_input('Correo Electronico')
        country = st.selectbox('Pais', COUNTRY,index=COUNTRY.index('Mexico'))
        password = st.text_input('Contraseña', type='password')
        rpt_password = st.text_input('Repetir Contraseña', type='password')
        register = st.button('Registrar',use_container_width=True)
        
        if register:
            if password == rpt_password:
                user = {
                    'Nombre': name,
                    'Apellido': last_name,
                    'CorreoElectronico': email,
                    'Contraseña': bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode(),
                    'Pais': country,
                }
                if client.insert_user(user):
                    st.toast('Usuario registrado exitosamente', icon=':material/thumb_up:' )
                else:
                    st.toast('Error al registrar usuario', icon='❗')
            else:
                st.error('Las contraseñas no coinciden',icon=':material/error:')
        