from pymongo import MongoClient

#mongodb://admin:*****@localhost:27017/
connection_string = "mongodb://admin:asd@localhost:27017"
client = MongoClient(connection_string)


# Define the database and collection
_db_name = "banco"
_collection_name = "colecao"

db = client[_db_name]
collection = db[_collection_name]
