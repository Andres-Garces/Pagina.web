from flask import Flask, request, jsonify
from models import db, User
import hashlib

# Crear la aplicación Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secret!'
db.init_app(app)

# Ruta para registrar un nuevo usuario
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = hashlib.sha256(data['password'].encode()).hexdigest()
    
    # Verificar si el usuario ya existe
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists'}), 400
    
    # Crear un nuevo usuario
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

# Ruta para el inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = hashlib.sha256(data['password'].encode()).hexdigest()
    
    # Verificar si las credenciales son correctas
    user = User.query.filter_by(username=username, password=password).first()
    
    if user:
        return jsonify({'message': 'Authentication successful'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

# Inicializar la base de datos
with app.app_context():
    db.create_all()

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
