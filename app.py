from flask import Flask, request, jsonify
from config import Config
from models import mysql, init_db, create_user, authenticate_user
import hashlib

# Crear la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)

# Inicializar MySQL
init_db(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = hashlib.sha256(data['password'].encode()).hexdigest()
    
    # Verificar si el usuario ya existe
    user = authenticate_user(username, password)
    if user:
        return jsonify({'error': 'User already exists'}), 400
    
    # Crear un nuevo usuario
    create_user(username, password)
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = hashlib.sha256(data['password'].encode()).hexdigest()
    
    # Verificar si las credenciales son correctas
    user = authenticate_user(username, password)
    if user:
        return jsonify({'message': 'Authentication successful'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)