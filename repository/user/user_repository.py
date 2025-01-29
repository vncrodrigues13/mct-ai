from models.user.user_model import User
from services.user.i_user_services import IUserServices
from typing import List



class UserRepository(IUserServices):
    
    instance = None
    
    def save_user(self, user : User) -> User:
        return user.save()
    
    def get_users(self) -> List[User]:
        users = User.objects()
        return users

    def get_user_by_id(self, userId : str) -> User:
        return User.objects(uuid=userId).first()
    
    def get_user_by_username(self, username : str) -> User:
        return User.objects(username=username).first()

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()

        return cls.instance