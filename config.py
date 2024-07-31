import os

class Config:
    SECRET_KEY = os.urandom(24)
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'tu_usuario_mysql'
    MYSQL_PASSWORD = 'tu_contraseña_mysql'
    MYSQL_DB = 'tu_base_de_datos'