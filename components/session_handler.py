from .mysql_client import MySQLClient


class SessionHandler:
    def __init__(self, client: MySQLClient):
        self.client = client
        self.session = None
        self.active = False
        
    def start_session(self, email: str):
        self.session = self.client.get_user(email)
        self.active = True
        
        
    
    def get_session_owner(self):
        return self.session[0][1]
    
    def is_active(self):
        return self.active