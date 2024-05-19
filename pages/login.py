from views.login import login
from components import MySQLClient,SessionHandler
from streamlit import set_page_config, secrets,session_state
from elements import navbar



set_page_config(page_title="UniBank", page_icon=":bank:", layout="wide")

client = MySQLClient(host="localhost",
                    user="root",
                    password=secrets["PASS"],
                    database="unibank")

client.connect()

if 'session' not in session_state:
    # Create a new session handler
    session_state.session = SessionHandler(client)


navbar(session_state.session)
login(client=client)