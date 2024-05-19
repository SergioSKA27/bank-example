import streamlit as st

from views.accont_creator import create_account
from views.deposit_maker import deposit_maker

st.markdown(
    """
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
""",
    unsafe_allow_html=True,
)


def user_card(user):
    with st.container(border=True):
        st.write(f"Nombre: {user[1]} {user[2]}")
        st.write(f"Correo: {user[3]}")
        st.write(f"Fecha de Registro: {user[5]}")
        st.write(f"ID: {user[0]}")


def account_card(account):
    with st.container(border=True):
        st.write(f"Tipo de Cuenta: {account[2]}")
        st.write(f"Saldo Actual: {account[3]}")
        st.write(f"Fecha de Creacion: {account[4]}")
        st.write(f"ID: {account[0]}")


def home():
    user = st.session_state.session.user_info()
    accounts = st.session_state.session.get_accounts()
    c1, c2 = st.columns([0.3, 0.7])
    with c1:
        user_card(user[0])

        if len(accounts) > 0:
            deposit = st.button("Depositar", use_container_width=True)
            if deposit:
                deposit_maker(st.session_state.session.client)

    with c2:
        if len(accounts) < 1:
            st.warning("No tienes cuentas registradas")
        else:
            for account in accounts:
                account_card(account)

        addacc = st.button("Agregar Cuenta", use_container_width=True)
        if addacc:
            create_account(st.session_state.session.client)


if __name__ == "__main__":
    if "session" not in st.session_state or not st.session_state.session.is_active():
        st.switch_page("pages/login.py")
    home()
