from models.user.user_model import User
from services.user.i_user_services import IUserServices
from repository.user.user_repository import UserRepository
from typing import List
import crypt


class UserServices(IUserServices):

    instance = None

    def __init__(self):
        self.userRepository = UserRepository.get_instance()

    def save_user(self, user : dict) -> User:
        user["password"] = crypt.crypt(user["password"])
        return self.userRepository.save_user(user)

    def get_users(self) -> List[User]:
        return self.userRepository.get_users()

    def get_user_by_id(self, userId : int) -> User:
        return self.userRepository.get_user_by_id(userId)

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()

        return cls.instance