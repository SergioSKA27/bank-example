import mysql.connector
import datetime


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
            database=self.database,
        )
        self.cursor = self.connection.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

    def insert_user(self, user):
        query = """INSERT INTO Usuarios (Nombre, Apellido, CorreoElectronico, Contraseña, FechaRegistro,Pais)
                    VALUES (%s, %s, %s, %s, %s,%s);
                """
        values = (
            user["Nombre"],
            user["Apellido"],
            user["CorreoElectronico"],
            user["Contraseña"],
            datetime.datetime.now(),
            user["Pais"],
        )

        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def get_user(self, email):
        # trunk-ignore(bandit/B608)
        query = f"SELECT * FROM Usuarios WHERE CorreoElectronico = '{email}'"
        return self.execute(query)

    def insert_account(self, account):
        sql = """INSERT INTO Cuentas (ID_Usuario, TipoCuenta, SaldoActual, FechaCreacion)
                    VALUES (%s, %s, %s, NOW());"""
        values = (
            account["ID_Usuario"],
            account["TipoCuenta"],
            account["SaldoActual"],
        )

        try:
            self.cursor.execute(sql, values)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def get_accounts(self, user_id):
        # trunk-ignore(bandit/B608)
        query = f"SELECT * FROM Cuentas WHERE ID_Usuario = {user_id}"
        return self.execute(query)

    def list_tables(self):
        query = "SHOW TABLES"
        return self.execute(query)

    def insert_transaction_transfer(self, transaction):
        # Transferencia de fondos entre cuentas
        # trunk-ignore(bandit/B608)
        query = f"""
        START TRANSACTION;

-- Supongamos que queremos transferir $100 de la cuenta con ID_Cuenta = 1 a la cuenta con ID_Cuenta = 2
-- Primero, verificamos si las cuentas existen y tienen suficientes fondos (para retiros).

-- Verificar fondos suficientes en la cuenta de origen
SELECT SaldoActual INTO @SaldoOrigen FROM Cuentas WHERE ID_Cuenta {transaction["ID_Cuenta_origen"]};

IF @SaldoOrigen >= 100 THEN
    -- Actualizar el saldo de la cuenta de origen (retiro)
    UPDATE Cuentas
    SET SaldoActual = SaldoActual - 100
    WHERE ID_Cuenta = {transaction["ID_Cuenta_origen"]};

    -- Actualizar el saldo de la cuenta de destino (depósito)
    UPDATE Cuentas
    SET SaldoActual = SaldoActual + 100
    WHERE ID_Cuenta = {transaction["ID_Cuenta_destino"]};

    -- Registrar la transacción
    INSERT INTO Transacciones (ID_Cuenta_origen, ID_Cuenta_destino, TipoTransaccion, Monto, FechaHoraTransaccion)
    VALUES ({transaction["ID_Cuenta_origen"]}, {transaction["ID_Cuenta_destino"]}, 'transferencia', {transaction["Monto"]},NOW());

    COMMIT;
ELSE
    -- Si no hay fondos suficientes, deshacer la transacción
    ROLLBACK;
END IF;


        """

        try:
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def list_users(self):
        query = "SELECT * FROM Usuarios"
        return self.execute(query)

    def run_transaction(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def make_depositer(self, cuenta, monto):
        # trunk-ignore(bandit/B608)
        query = f"SELECT * FROM Cuentas WHERE ID_Cuenta = {cuenta}"

        saldo = self.execute(query)[0][3]

        nsaldo = float(saldo) + monto

        # trunk-ignore(bandit/B608)
        update = f"UPDATE Cuentas SET SaldoActual = {nsaldo} WHERE ID_Cuenta = {cuenta}"

        try:
            self.cursor.execute(update)
            self.connection.commit()
            transaction = {
                "ID_Cuenta_origen": cuenta,
                "ID_Cuenta_destino": cuenta,
                "TipoTransaccion": "transferencia",
                "Monto": monto,
            }
            restrans = self.insert_transaction(transaction)
            if restrans:
                return True
            else:
                raise Exception
        except Exception as e:
            self.connection.rollback()
            print(e)
            return False

    def make_withdrawal(self, cuenta, monto):
        # trunk-ignore(bandit/B608)
        query = f"SELECT * FROM Cuentas WHERE ID_Cuenta = {cuenta}"

        saldo = self.execute(query)[0][3]

        if saldo < monto:
            return False
        else:
            nsaldo = float(saldo) - monto
            # trunk-ignore(bandit/B608)
            update = f"UPDATE Cuentas SET SaldoActual = {nsaldo} WHERE ID_Cuenta = {cuenta}"
            try:
                self.cursor.execute(update)
                self.connection.commit()
                transaction = {
                    "ID_Cuenta_origen": cuenta,
                    "ID_Cuenta_destino": cuenta,
                    "TipoTransaccion": "retiro",
                    "Monto": monto,
                }
                restrans = self.insert_transaction(transaction)
                if restrans:
                    return True
                else:
                    raise Exception
            except Exception as e:
                self.connection.rollback()
                print(e)
                return False

    def make_transfer(self, origen, destino, monto):
        # trunk-ignore(bandit/B608)
        query = f"SELECT * FROM Cuentas WHERE ID_Cuenta = {origen}"

        saldo_origen = self.execute(query)[0][3]

        if saldo_origen < monto:
            return False
        else:
            nsaldo_origen = float(saldo_origen) - monto
            # trunk-ignore(bandit/B608)
            update_origen = f"UPDATE Cuentas SET SaldoActual = {nsaldo_origen} WHERE ID_Cuenta = {origen}"
            try:
                self.cursor.execute(update_origen)
                self.connection.commit()
            except Exception as e:
                self.connection.rollback()
                print(e)
                return False

            # trunk-ignore(bandit/B608)
            query = f"SELECT * FROM Cuentas WHERE ID_Cuenta = {destino}"
            saldo_destino = self.execute(query)[0][3]
            nsaldo_destino = float(saldo_destino) + monto
            # trunk-ignore(bandit/B608)
            update_destino = f"UPDATE Cuentas SET SaldoActual = {nsaldo_destino} WHERE ID_Cuenta = {destino}"
            try:
                self.cursor.execute(update_destino)
                self.connection.commit()
            except Exception as e:
                self.connection.rollback()
                print(e)
                return False

            transaction = {
                "ID_Cuenta_origen": origen,
                "ID_Cuenta_destino": destino,
                "TipoTransaccion": "transferencia",
                "Monto": monto,
            }
            restrans = self.insert_transaction(transaction)
            if restrans:
                return True
            else:
                return False

    def insert_transaction(self, transaction):

        # trunk-ignore(bandit/B608)
        query = f"""INSERT INTO Transacciones (ID_Cuenta_origen, ID_Cuenta_destino, TipoTransaccion, Monto, FechaHoraTransaccion)
                    VALUES ({transaction["ID_Cuenta_origen"]}, {transaction["ID_Cuenta_destino"]}, '{transaction["TipoTransaccion"]}', {transaction["Monto"]}, NOW());
                """
        try:
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print(e)
            return False

    def list_transactions_user(self, user_id):
        # trunk-ignore(bandit/B608)
        query = f""" SELECT * FROM Transacciones
                    WHERE ID_Cuenta_origen IN (SELECT ID_Cuenta FROM Cuentas WHERE ID_Usuario = {user_id})
                    OR ID_Cuenta_destino IN (SELECT ID_Cuenta FROM Cuentas WHERE ID_Usuario = {user_id})
                    """
        return self.execute(query)


    def get_all_accounts(self):
        query = "SELECT * FROM Cuentas"
        return self.execute(query)

    def insert_session(self, session):
        query = """INSERT INTO HistorialSesiones (ID_Usuario, FechaHoraInicio, DireccionIP, AgenteUsuario)
                    VALUES (%s, NOW(), %s, %s);"""

        values = (
            session["ID_Usuario"],
            session["DireccionIP"],
            session["AgenteUsuario"],
        )

        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def get_user_sessions(self, user_id):
        # trunk-ignore(bandit/B608)
        query = f"SELECT * FROM HistorialSesiones WHERE ID_Usuario = {user_id}"
        return self.execute(query)
