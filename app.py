import streamlit as st
from components import MySQLClient,SessionHandler


st.set_page_config(page_title="UniBank", page_icon=":bank:", layout="wide")

client = MySQLClient(host="localhost",
                    user="root",
                    password=st.secrets["PASS"],
                    database="unibank")

client.connect()


if 'session' not in st.session_state:
    st.session_state.session = SessionHandler(client)

if st.session_state.session.is_active():
    st.write(st.session_state.session.get_session_owner())

def heromain():
    cols = st.columns([.6,.4])
    
    with cols[0]:
        st.title("UniBank - Tu banco digital")
        st.caption("Bienvenido a UniBank, tu banco digital. Aquí podrás realizar todas tus operaciones bancarias de manera rápida y segura.")
        b1, b2 = st.columns([1,1])
        with b1:
            st.button("Iniciar sesión")
        with b2:
            reg = st.button("Registrarse")
            if reg:
                st.switch_page("pages/register.py")
            
    with cols[1]:
        st.image("https://img.freepik.com/free-vector/linear-flat-internet-banking-infographics-template-icons-website-hero-image-vector-illustration_126523-2982.jpg",
                 use_column_width=True)

if __name__ == "__main__":
    heromain()