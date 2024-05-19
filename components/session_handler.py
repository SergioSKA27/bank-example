from .mysql_client import MySQLClient


class SessionHandler:
    def __init__(self, client: MySQLClient):
        self.client = client
        self.session = None
        self.active = False

    def start_session(self, email: str):
        self.session = self.client.get_user(email)
        self.register_session(email)
        self.active = True

    def register_session(self, email: str):
        user = self.client.get_user(email)[0][0]
        ip = "127.0.0.1"
        agent = "Mozilla/5.0"
        s = {"ID_Usuario": user, "DireccionIP": ip, "AgenteUsuario": agent}
        self.client.insert_session(s)

    def get_session_owner(self):
        return self.session[0][1]

    def get_accounts(self):
        return self.client.get_accounts(self.session[0][0])

    def get_user_transactions(self):
        return self.client.list_transactions_user(self.session[0][0])

    def is_active(self):
        return self.active

    def user_info(self):
        return self.session

    def get_all_accounts(self):
        return self.client.get_all_accounts()

    def close(self):
        self.active = False
        self.session = None

    def get_all_sessions(self):
        return self.client.get_user_sessions(self.session[0][0])

    def update(self):
        self.client.close()
        self.client.connect()
