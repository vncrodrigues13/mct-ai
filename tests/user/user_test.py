import copy
import pytest
from models.user.user_model import User



def test_encrypt_password():
    old_user = {
        "firstName": "John",
        "lastName": "Doe",
        "password": "asd"
    }
    user = User(old_user)
        
    assert old_user["firstName"] == user.firstName
    assert old_user["lastName"] == user.lastName
    assert old_user["password"] != user.password