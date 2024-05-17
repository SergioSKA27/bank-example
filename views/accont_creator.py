import streamlit as st
from components import MySQLClient

@st.experimental_dialog(title="Crear Cuenta",width="large")
def create_account(client: MySQLClient):
    types = ['corriente', 'ahorros']
    acc_type = st.selectbox("Tipo de Cuenta", types,format_func=lambda x: x.capitalize())
    create = st.button("Crear Cuenta")
    if create:
        acont = {
            'ID_Usuario': st.session_state.session.user_info()[0][0],
            'TipoCuenta': acc_type,
            'SaldoActual': 0,
            
        }
        client.insert_account(acont)
        st.success("Cuenta creada exitosamente")
        st.stop()
    st.stop()