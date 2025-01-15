from mongoengine import *
import uuid
import crypt
import datetime
import json

COLLECTION_NAME = 'user'

class User(Document):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4, binary= False)
    firstName = StringField(required=True, max_length=200)
    lastName = StringField(required=True, max_length=200)
    password = StringField(required=True, max_length=200)
    createdAt = DateTimeField(required=True, default=datetime.datetime.utcnow)


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