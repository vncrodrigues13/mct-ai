from flask import Flask, Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from services.user.user_services import  UserServices


bluePrint = Blueprint('user', __name__, url_prefix='/user')

services = UserServices.get_instance()

@bluePrint.get('/')
@jwt_required()
def get_users():
    users = UserServices().get_users()
    # users = UserServices.get_instance().
    users_dict = [user.to_dict() for user in users]
    return jsonify(users_dict)


@bluePrint.post('/')
@jwt_required()
def save_user():
    userJson = request.get_json()
    print(userJson)
    user = UserServices.get_instance().save_user(userJson)
    return jsonify(user.to_dict())
