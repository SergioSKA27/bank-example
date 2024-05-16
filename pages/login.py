from views.login import login
from components import MySQLClient
from streamlit import set_page_config, secrets


set_page_config(page_title="UniBank", page_icon=":bank:", layout="wide")

client = MySQLClient(host="localhost",
                    user="root",
                    password=secrets["PASS"],
                    database="unibank")

client.connect()

login(client=client)