import time
import streamlit as st
from components import MySQLClient

@st.experimental_dialog(title="Depositos",width="large")
def deposit_maker(client: MySQLClient):
    accounts = client.get_accounts(st.session_state.session.user_info()[0][0])
    accs = [f"{account[2]} - {account[0]}" for account in accounts]
    acc = st.selectbox("Selecciona la cuenta a la que deseas depositar", accs)
    amount = st.number_input("Cantidad a depositar",min_value=1.0)
    deposit = st.button("Depositar",use_container_width=True,key="depositpersonal")
    if deposit:
        acc_id = acc.split("-")[1].strip()
        data = client.make_depositer(cuenta=acc_id,monto=amount)
        if data:
            st.success("Deposito realizado exitosamente")
            time.sleep(3)
            st.rerun()
        else:
            st.error("Fallo al realizar deposito, sus fondos no fueron afectados")
