from pymongo import MongoClient
from mongoengine import connect
from flask import Flask, jsonify, request, Blueprint
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
import datetime
from api.User import user_api

app = Flask(__name__)

app.register_blueprint(user_api.bluePrint)
app.config['JWT_SECRET_KEY'] = 'ed87f88d8fa44dca79a2a164de51df29e4a6c228e64ba00d9655d2e091b4af7e3445f26fe76e532f6df87a359304e5f55c5fbcea7751e45e281b7b1dc56e7548'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=1)

jwt = JWTManager(app)


connect(db='banco', host='localhost', port=27017, username='admin', password='asd')


users = {
    'vinicius': 'rodrigues',
    'asd': 'dsa'
}


@app.route('/print')
@jwt_required()
def test():
    superhero = {
        'name': 'Nick',
        'lastName': 'Fury'
    }
    return superhero


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






if __name__ == '__main__':
    app.run(debug=True)
    print('Server running ')
    