import streamlit as st

from components import SessionHandler


def navbar(session: SessionHandler):

    container = st.container(border=False)
    cols = container.columns([2, 1, 1, 1, 1, 1, 1])

    with cols[0]:
        st.markdown(
            """
                    <style>
                    .logo-nav {
                        font-size: 25px;
                        font-weight: bold;
                        color: #1E90FF;
                        text-align: center;
                        display: flex;
                        justify-content: left;
                        align-items: left;
                        margin: 0 0 0 0;
                    }
                    </style>
                    """,
            unsafe_allow_html=True,
        )

        if session.is_active():
            st.markdown(f":blue[{session.get_session_owner()}]", unsafe_allow_html=True)
        else:
            st.markdown("<p class='logo-nav'>UniBank</p>", unsafe_allow_html=True)

        if session.is_active():
            with cols[3]:
                st.page_link("pages/home.py", icon="🏠", label="Inicio")

            with cols[4]:
                st.page_link("pages/register.py", icon="📈", label="Historial")

            with cols[5]:
                st.page_link("pages/register.py", label="Ver Perfil", icon="👤")

            with cols[-1]:
                if st.button("Salir🚪", use_container_width=True, type="primary"):
                    session.close()
                    st.switch_page("pages/login.py")
        else:
            with cols[-3]:
                st.page_link("app.py", icon="🏠", label="Inicio")

            with cols[-1]:
                st.page_link("pages/login.py", icon="🔒", label="Login")
            with cols[-2]:
                st.page_link("pages/register.py", icon="📝", label="Registro")
