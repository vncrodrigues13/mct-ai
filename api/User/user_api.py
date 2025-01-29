from flask import Flask, Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.user.user_services import  UserServices


bluePrint = Blueprint('user', __name__, url_prefix='/user')

services = UserServices.get_instance()

@bluePrint.get('/')
@jwt_required()
def get_users():
    users = UserServices.get_instance().get_users()
    # users = UserServices.get_instance().
    users_dict = [user.to_dict() for user in users]
    return jsonify(users_dict)


@bluePrint.post('/')
def create_user():
    userJson = request.get_json()
    user = UserServices.get_instance().save_user(userJson)
    return jsonify(user.to_dict())


@bluePrint.put('/')
@jwt_required()
def update_user():
    userJson = request.get_json()
    user = UserServices.get_instance().update_user(userJson)
    return jsonify(user.to_dict())