from abc import ABC, abstractmethod
from models.user.user_model import User
from typing import List

class IUserServices(ABC):

    @abstractmethod
    def save_user(self, user : dict) -> User :
        pass

    @abstractmethod
    def get_users(self) -> List[User] :
        pass

    @abstractmethod
    def get_user_by_id(self, userId : int) -> User:
        pass

    