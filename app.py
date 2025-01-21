from pymongo import MongoClient
from mongoengine import connect
from flask import Flask, jsonify, request, Blueprint
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
import datetime
import os
from api.User import user_api

app = Flask(__name__)

app.register_blueprint(user_api.bluePrint)
app.config['JWT_SECRET_KEY'] = 'ed87f88d8fa44dca79a2a164de51df29e4a6c228e64ba00d9655d2e091b4af7e3445f26fe76e532f6df87a359304e5f55c5fbcea7751e45e281b7b1dc56e7548'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=1)

jwt = JWTManager(app)

db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_HOST')
db_port = int(os.getenv('DB_PORT'))
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

connect(db=db_name, host=db_host, port=db_port, username=db_user, password=db_password, serverSelectionTimeoutMS=5000, connectTimeoutMS=5000)


users = {
    'vinicius': 'rodrigues',
    'asd': 'dsa'
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        # Gera o token de acesso
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Credenciais inválidas"}), 401


@app.get('/')
def home():
    return jsonify({'message': 'Hello Server'})



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    print('Server running ')
    