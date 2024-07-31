from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app):
    mysql.init_app(app)

def create_user(username, password):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users(username, password) VALUES(%s, %s)", (username, password))
    mysql.connection.commit()
    cur.close()

def authenticate_user(username, password):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cur.fetchone()
    cur.close()
    return user