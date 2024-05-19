import pandas as pd
import streamlit as st

from views.accont_creator import create_account
from views.deposit_maker import deposit_maker

from .retiros import retiros
from .transfer_maker import transfer_maker


def transaction_card(transactions):
    st.divider()
    st.subheader("Transacciones")

    _, cl, _ = st.columns([1, 4, 1])
    colums = [
        "ID Transaccion",
        "ID Cuenta Origen",
        "ID Cuenta Destino",
        "Tipo de Transaccion",
        "Monto",
        "Fecha de Transaccion",
    ]
    df = pd.DataFrame(transactions, columns=colums)
    cl.write(df)


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

            transf = st.button("Transferir", use_container_width=True)
            if transf:
                transfer_maker(st.session_state.session.client)

            ret = st.button("Retirar", use_container_width=True)
            if ret:
                retiros(st.session_state.session.client)

        if st.button("Actualizar Informacion", use_container_width=True):
            st.session_state.session.update()

    with c2:
        if len(accounts) < 1:
            st.warning("No tienes cuentas registradas")
        else:
            for account in accounts:
                account_card(account)

        addacc = st.button("Agregar Cuenta", use_container_width=True)
        if addacc:
            create_account(st.session_state.session.client)

    transactions = st.session_state.session.get_user_transactions()
    if len(transactions) > 0:
        transaction_card(transactions)
