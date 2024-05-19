import time
import streamlit as st 

from components import MySQLClient

@st.experimental_dialog("Retiro de fondos",width="large")
def retiros(client: MySQLClient):
    money = st.number_input("Monto a retirar",min_value=1.0,step=1.0)
    cuentas = client.get_accounts(st.session_state.session.user_info()[0][0])
    cuenta = st.selectbox("Selecciona la cuenta de la que deseas retirar", [f"{cuenta[0]}" for cuenta in cuentas])
    retirar = st.button("Retirar",key="retirar")
    if retirar:
        cuenta_id = int(cuenta)
        if client.make_withdrawal(cuenta_id,money):
            st.success("Retiro exitoso")
            time.sleep(3)
            st.rerun()
        else:
            st.error("No se pudo realizar el retiro")
            st.stop()
    