import os
from mongoengine import connect



def start_connection():
    db_name = os.getenv('DB_NAME')
    db_host = os.getenv('DB_HOST')
    db_port = int(os.getenv('DB_PORT'))
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')

    connect(db=db_name, 
            host=db_host, 
            port=db_port, 
            username=db_user, 
            password=db_password, 
            serverSelectionTimeoutMS=5000, 
            connectTimeoutMS=5000)