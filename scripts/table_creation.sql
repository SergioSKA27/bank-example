USE unibank;
CREATE TABLE Usuarios (
    ID_Usuario INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    CorreoElectronico VARCHAR(100),
    Contraseña VARCHAR(100),
    FechaRegistro DATE,
    Pais VARCHAR(50)
);
CREATE TABLE Cuentas (
    ID_Cuenta INT AUTO_INCREMENT PRIMARY KEY,
    ID_Usuario INT,
    TipoCuenta ENUM('corriente', 'ahorros'),
    SaldoActual DECIMAL(10, 2),
    FechaCreacion DATE,
    FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuario)
);
CREATE TABLE Transacciones (
    ID_Transaccion INT AUTO_INCREMENT PRIMARY KEY,
    ID_Cuenta_origen INT,
    ID_Cuenta_destino INT,
    TipoTransaccion ENUM('retiro', 'transferencia'),
    Monto DECIMAL(10, 2),
    FechaHoraTransaccion TIMESTAMP,
    FOREIGN KEY (ID_Cuenta_origen) REFERENCES Cuentas(ID_Cuenta),
    FOREIGN KEY (ID_Cuenta_destino) REFERENCES Cuentas(ID_Cuenta)
);
CREATE TABLE Beneficiarios (
    ID_Beneficiario INT AUTO_INCREMENT PRIMARY KEY,
    ID_Usuario INT,
    NombreBeneficiario VARCHAR(100),
    NumeroCuentaBeneficiario VARCHAR(50),
    BancoBeneficiario VARCHAR(100),
    FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuario)
);
CREATE TABLE HistorialSesiones (
    ID_Sesion INT AUTO_INCREMENT PRIMARY KEY,
    ID_Usuario INT,
    FechaHoraInicio TIMESTAMP,
    DireccionIP VARCHAR(45),
    AgenteUsuario VARCHAR(255),
    FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuario)
);
