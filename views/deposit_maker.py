import streamlit as st
from components import MySQLClient

@st.experimental_dialog(title="Depositos",width="large")
def deposit_maker(client: MySQLClient):
    accounts = client.get_accounts(st.session_state.session.user_info()[0][0])
    accs = [f"{account[2]} - {account[0]}" for account in accounts]
    acc = st.selectbox("Selecciona la cuenta a la que deseas depositar", accs)
    amount = st.number_input("Cantidad a depositar",min_value=0.0)
    deposit = st.button("Depositar")
    if deposit:
        acc_id = acc.split("-")[1].strip()
        
        client.make_deposit()
        st.success("Deposito realizado exitosamente")
        st.stop()
    st.stop()