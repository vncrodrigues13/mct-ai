from models.user.user_model import User
from services.user.i_user_services import IUserServices
from typing import List



class UserRepository(IUserServices):
    
    instance = None
    
    def save_user(self, user : dict) -> User:
        
        user_obj = User(firstName = user["firstName"], lastName = user["lastName"], password = user["password"])
        return user_obj.save()
    
    def get_users(self) -> List[User]:
        users = User.objects()
        return users

    def get_user_by_id(self, userId : str) -> User:
        return User.objects(uuid=userId).first()

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()

        return cls.instance