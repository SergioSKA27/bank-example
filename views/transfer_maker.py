import time
import streamlit as st
from components import MySQLClient


@st.experimental_dialog("Transfer Maker",width="large")
def transfer_maker(client: MySQLClient):
    st.subheader("Transferencias")
    accounts = st.session_state.session.get_all_accounts()
    ids = [account[0] for account in accounts]
    
    selected_account = st.selectbox("Selecciona la cuenta origen", ids)
    selected_destiny = st.selectbox("Selecciona la cuenta destino", ids)
    if selected_account == selected_destiny:
        st.error("No puedes transferir a la misma cuenta")
        return  
    
    amount = st.number_input("Monto a transferir", min_value=1.0, step=1.0)
    
    res = st.button("Transferir", use_container_width=True, key="transfer")
    if res:
        res = client.make_transfer(selected_account, selected_destiny, amount)
        if res:
            st.success("Transferencia realizada exitosamente")
            time.sleep(2)
            st.rerun()
        else:
            st.error("Fallo al realizar transferencia, tus fondos no fueron afectados")