from streamlit import secrets, session_state

import views
from components import MySQLClient, SessionHandler
from elements import navbar

client = MySQLClient(
    host="localhost", user="root", password=secrets["PASS"], database="unibank"
)

client.connect()

if "session" not in session_state:
    # Create a new session handler
    session_state.session = SessionHandler(client)

navbar(session_state.session)
views.registration(client=client)
