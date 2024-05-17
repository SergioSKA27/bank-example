import streamlit as st
from views.accont_creator import create_account


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
    c1, c2 = st.columns([.3, .7])
    with c1:
        user_card(user[0])
    
    with c2:
        if len(accounts) < 1:
            st.warning("No tienes cuentas registradas")
        else:
            for account in accounts:
                account_card(account)
        
        addacc = st.button("Agregar Cuenta",use_container_width=True)
        if addacc:
            create_account(st.session_state.session.client)
        

if __name__ == '__main__':
    home()