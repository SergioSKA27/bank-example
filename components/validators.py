from .mysql_client import MySQLClient
import bcrypt


class Validator:
    def __init__(self, db_client: MySQLClient):
        self.db_client = db_client

    def validate_user(self, mail: str, password: str) -> bool:
        encrypted_password = self.db_client.get_user_password(mail)
        
        return bcrypt.checkpw(password.encode('utf-8'), encrypted_password.encode('utf-8'))