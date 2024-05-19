import streamlit as st
import pandas as pd
import plotly.express as px

def transaction_card(transactions):
    st.divider()
    st.subheader("Transacciones")

    colums = [
        "ID Transaccion",
        "ID Cuenta Origen",
        "ID Cuenta Destino",
        "Tipo de Transaccion",
        "Monto",
        "Fecha de Transaccion",
    ]
    df = pd.DataFrame(transactions, columns=colums)
    st.write(df)
    
    fig = px.line(df, x="Fecha de Transaccion", y="Monto", title="Transacciones")
    st.plotly_chart(fig)
    
    circlechart = px.pie(df, names="Tipo de Transaccion", title="Transacciones")
    st.plotly_chart(circlechart, use_container_width=True)
    
    
    
    
    

def session_card(sessions):
    st.divider()
    st.subheader("Sesiones")

    colums = [
        "ID Sesion",
        "ID Usuario",
        "Fecha de Inicio",
        "Direccion IP",
        "Agente de Usuario",
    ]
    df = pd.DataFrame(sessions, columns=colums)
    st.write(df)
    
    fig = px.histogram(df, x="Fecha de Inicio", title="Sesiones")
    st.plotly_chart(fig, use_container_width=True)
                  
    

def history():
    st.subheader("Historial")
    
    sessions = st.session_state.session.get_all_sessions()
    transactions = st.session_state.session.get_user_transactions()
    c1, c2 = st.columns(2)
    with c1:
        session_card(sessions)
    with c2:
        transaction_card(transactions)
