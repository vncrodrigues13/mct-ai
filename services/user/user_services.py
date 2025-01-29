from models.user.user_model import User
from services.user.i_user_services import IUserServices
from repository.user.user_repository import UserRepository
from typing import List
from utils.crypt.crypt_util import get_salt
import crypt


class UserServices(IUserServices):

    instance = None

    def __init__(self):
        self.userRepository = UserRepository.get_instance()

    def save_user(self, user : dict) -> User:
        salt = get_salt() 
        print(salt)
        user["password"] = crypt.crypt(user["password"], salt)
        user_obj = User(username = user["username"], firstName = user["firstName"], lastName = user["lastName"], password = user["password"])
        return self.userRepository.save_user(user_obj)

    def get_users(self) -> List[User]:
        return self.userRepository.get_users()
    
    def get_user_by_username(self, username : str) -> User:
        return self.userRepository.get_user_by_username(username)

    def get_user_by_id(self, userId : str) -> User:
        return self.userRepository.get_user_by_id(userId)


    def verify_password(self, stored_hash, password):
        print('stored' ,stored_hash) 
        print('password', password) 
        if crypt.crypt(password, stored_hash) == stored_hash:
            raise Exception("Credenciais inválidas")
        

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()

        return cls.instance