import datetime
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from infra.db.setup import start_connection as start_db_connection
from api.routes import routes
import os
import debugpy

start_db_connection()
datetime.timezone(datetime.timedelta(hours=-3))

app = Flask(__name__)
app.register_blueprint(routes)

app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_SECURE"] = False  # Set to True in production (for HTTPS)
app.config["JWT_ACCESS_COOKIE_NAME"] = "access_token_cookie"
app.config['JWT_SECRET_KEY'] = 'ed87f88d8fa44dca79a2a164de51df29e4a6c228e64ba00d9655d2e091b4af7e3445f26fe76e532f6df87a359304e5f55c5fbcea7751e45e281b7b1dc56e7548'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=1)


jwt = JWTManager(app)


@app.get('/')
def home():
    return jsonify({'message': 'Hello Server'})

if __name__ == '__main__':
    app.run(host=os.getenv('APP_HOST'),debug=True)
    debugpy.listen((os.getenv('APP_HOST'), 5678))
    print('Server running ')
    
    