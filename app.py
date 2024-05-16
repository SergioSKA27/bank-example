import streamlit as st
from components import MySQLClient


st.set_page_config(page_title="UniBank", page_icon=":bank:", layout="wide")

client = MySQLClient(host="localhost",
                    user="root",
                    password=st.secrets["PASS"],
                    database="unibank")

client.connect()

st.write(client.list_tables())

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