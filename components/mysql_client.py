import mysql.connector


class MySQLClient:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
        
    
    def insert_user(self, user):
        query = """INSERT INTO Usuarios (Nombre, Apellido, CorreoElectronico, Contraseña, FechaRegistro)
                    VALUES (%s, %s, %s, %s, NOW());
                """
        values = (user['Nombre'], user['Apellido'], user['CorreoElectronico'], user['Contraseña'])
        
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    
    def list_tables(self):
        query = "SHOW TABLES"
        return self.execute(query)