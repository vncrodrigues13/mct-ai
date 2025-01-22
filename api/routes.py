from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required, unset_access_cookies, get_jwt_identity
from api.User import user_api

users = {'vinicius': 'rodrigues','asd': 'dsa'}

routes = Blueprint('routes', __name__, url_prefix='/')

routes.register_blueprint(user_api.bluePrint)


@routes.post('/login')
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username in users and users[username] == password:
        access_token = create_access_token(identity=username)
        response = jsonify({"msg": "Login sucessfull", "access_token": access_token})
        set_access_cookies(response, access_token)
        print(response.location)
        return response, 200
    else:
        return jsonify({"msg": "Credenciais inválidas"}), 401
    

@routes.get('/logout')
@jwt_required()
def logout():
    current_user = get_jwt_identity()
    res = jsonify({"msg": "Logout sucessfull", "user": current_user})
    unset_access_cookies(res)
    return res, 200