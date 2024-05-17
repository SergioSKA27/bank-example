import streamlit as st
from components import MySQLClient,SessionHandler
from elements import navbar


st.set_page_config(page_title="UniBank", page_icon=":bank:", layout="wide")

client = MySQLClient(host="localhost",
                    user="root",
                    password=st.secrets["PASS"],
                    database="unibank")

client.connect()


st.markdown("""
<style>
.bg {
  animation:slide 20s ease-in-out infinite alternate;
  background-image: url("data:image/svg+xml;utf8,%3Csvg viewBox=%220 0 2000 1000%22 xmlns=%22http:%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cmask id=%22b%22 x=%220%22 y=%220%22 width=%222000%22 height=%221000%22%3E%3Cpath fill=%22url(%23a)%22 d=%22M0 0h2000v1000H0z%22%2F%3E%3C%2Fmask%3E%3Cpath fill=%22%23fff%22 d=%22M0 0h2000v1000H0z%22%2F%3E%3Cg style=%22transform-origin:center center%22 stroke=%22%238c96d5%22 stroke-width=%222%22 mask=%22url(%23b)%22%3E%3Cpath fill=%22none%22 d=%22M0 0h125v125H0z%22%2F%3E%3Cpath fill=%22%238c96d5b3%22 d=%22M375 0h125v125H375z%22%2F%3E%3Cpath fill=%22none%22 d=%22M875 0h125v125H875z%22%2F%3E%3Cpath fill=%22%238c96d5fe%22 d=%22M1000 0h125v125h-125z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1375 0h125v125h-125z%22%2F%3E%3Cpath fill=%22%238c96d5a9%22 d=%22M375 125h125v125H375z%22%2F%3E%3Cpath fill=%22none%22 d=%22M500 125h125v125H500zM1500 125h125v125h-125z%22%2F%3E%3Cpath fill=%22%238c96d583%22 d=%22M0 250h125v125H0z%22%2F%3E%3Cpath fill=%22none%22 d=%22M125 250h125v125H125z%22%2F%3E%3Cpath fill=%22%238c96d5f8%22 d=%22M1000 250h125v125h-125z%22%2F%3E%3Cpath fill=%22%238c96d5c6%22 d=%22M1125 250h125v125h-125z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1250 250h125v125h-125zM0 375h125v125H0zM500 375h125v125H500z%22%2F%3E%3Cpath fill=%22%238c96d507%22 d=%22M1000 375h125v125h-125z%22%2F%3E%3Cpath fill=%22%238c96d5d8%22 d=%22M1500 375h125v125h-125z%22%2F%3E%3Cpath fill=%22none%22 d=%22M375 500h125v125H375z%22%2F%3E%3Cpath fill=%22%238c96d59e%22 d=%22M750 500h125v125H750z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1000 500h125v125h-125z%22%2F%3E%3Cpath fill=%22%238c96d53b%22 d=%22M1250 500h125v125h-125z%22%2F%3E%3Cpath fill=%22%238c96d53d%22 d=%22M1875 500h125v125h-125z%22%2F%3E%3Cpath fill=%22%238c96d54f%22 d=%22M1250 625h125v125h-125z%22%2F%3E%3Cpath fill=%22none%22 d=%22M1500 625h125v125h-125z%22%2F%3E%3Cpath fill=%22%238c96d5e3%22 d=%22M1750 625h125v125h-125z%22%2F%3E%3Cpath fill=%22none%22 d=%22M0 750h125v125H0zM1125 750h125v125h-125zM1500 750h125v125h-125zM1875 750h125v125h-125zM125 875h125v125H125zM250 875h125v125H250zM1125 875h125v125h-125zM1250 875h125v125h-125zM1375 875h125v125h-125zM1750 875h125v125h-125zM1875 875h125v125h-125z%22%2F%3E%3C%2Fg%3E%3Cdefs%3E%3CradialGradient id=%22a%22%3E%3Cstop offset=%220%22 stop-color=%22%23fff%22%2F%3E%3Cstop offset=%221%22 stop-color=%22%23fff%22 stop-opacity=%220%22%2F%3E%3C%2FradialGradient%3E%3C%2Fdefs%3E%3C%2Fsvg%3E");
  bottom:0;
  left:-50%;
  opacity:.5;
  position:fixed;
  right:-50%;
  top:0;
  z-index:0;
  ackground-size: cover;
  background-position: center center;
}

</style>
<div class="bg"></div>
""", unsafe_allow_html=True)
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