from mongoengine import *
import uuid
import crypt
import datetime
import json

COLLECTION_NAME = 'user'

class User(Document):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4, binary= False)
    username = StringField(required=True, max_length=15)
    firstName = StringField(required=True, max_length=15)
    lastName = StringField(required=True, max_length=15)
    password = StringField(required=True, max_length=200)
    createdAt = DateTimeField(required=True, default=datetime.datetime.utcnow)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if kwargs.get('username') is None or kwargs.get('username') == '':
            raise ValueError('username is required')
        
        if kwargs.get('firstName') is None or kwargs.get('firstName') == '':
            raise ValueError('firstName is required')
        
        if kwargs.get('lastName') is None or kwargs.get('lastName') == '':
            raise ValueError('lastName is required')
        
        if kwargs.get('password') is None or kwargs.get('password') == '':
            raise ValueError('password is required')
        


    def to_json(self):
        return json.dumps(self)
            
    def to_dict(self):
        return {
            "uuid": str(self.uuid),
            "firstName": self.firstName,
            "lastName": self.lastName,
            "password": self.password,
            "createdAt": self.createdAt.isoformat()
        }