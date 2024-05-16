import views
from components import MySQLClient
from streamlit import secrets

client = MySQLClient(host="localhost",
                    user="root",
                    password=secrets["PASS"],
                    database="unibank")

client.connect()


views.registration(client=client)

