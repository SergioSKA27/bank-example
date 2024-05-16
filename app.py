import streamlit as st
from components import MySQLClient,SessionHandler
from elements import navbar


st.set_page_config(page_title="UniBank", page_icon=":bank:", layout="wide")

client = MySQLClient(host="localhost",
                    user="root",
                    password=st.secrets["PASS"],
                    database="unibank")

client.connect()


if 'session' not in st.session_state:
    # Create a new session handler
    st.session_state.session = SessionHandler(client)


navbar(st.session_state.session)
def heromain():
    cols = st.columns([.4,.6])
    
    with cols[1]:
        style = """<style>
                .header-hero {
                    font-size: 10vw;
                    font-weight: bold;
                    color: #1E90FF;
                    text-align: center;
                    margin: 0;
                }
                .caption-hero {
                    font-size: 16px;
                    color: #1E90FF;
                    text-align: center;
                }
                </style>
                """
        st.markdown(style, unsafe_allow_html=True)

        st.markdown("<p class='header-hero'>UniBank</p>", unsafe_allow_html=True)
        st.caption("""
                   <p style='text-align: center;'>
                   Bienvenido a UniBank, tu banco digital. Aquí podrás realizar todas tus operaciones bancarias de manera rápida y segura.
                   </p>
                   """, unsafe_allow_html=True)
        _, b1,b2 = st.columns([1,1,1])
        with b1:
            log = st.button("Iniciar sesión",use_container_width=True)
            if log:
                st.switch_page("pages/login.py")
        with b2:
            reg = st.button("Registrarse",use_container_width=True)
            if reg:
                st.switch_page("pages/register.py")
            
    with cols[0]:
        st.image("https://img.freepik.com/free-vector/linear-flat-internet-banking-infographics-template-icons-website-hero-image-vector-illustration_126523-2982.jpg",
                 use_column_width=True)

if __name__ == "__main__":
    heromain()