import pytest
from models.user.user_model import User
from services.user.user_services import UserServices



user = {
    "username": "john.doe",
    "firstName": "John",
    "lastName": "Doe",
    "password": "asd"
}

def test_empty_username():
    with pytest.raises(ValueError, match="username is required") : 
        User(username = "", firstName = user["firstName"], lastName = user["lastName"], password = user["password"])

def test_empty_first_name():
    
    with pytest.raises(ValueError, match="firstName is required") : 
        User(username = user["username"], firstName = "", lastName = user["lastName"], password = user["password"])   

def test_empty_last_name():
    
    with pytest.raises(ValueError, match="lastName is required") : 
        User(username = user["username"], firstName = user["firstName"], lastName = "", password = user["password"])


def test_empty_password():
    with pytest.raises(ValueError, match="password is required") : 
        User(username = user["username"], firstName = user["firstName"], lastName = user["lastName"], password = "")