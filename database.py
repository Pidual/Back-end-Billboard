from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

uri = "mongodb+srv://spidual:cVov8ftrCrgMbIli@cluster0.cotjptw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

ca = certifi.where() #ni idea que hace esto

def dbConnection():
    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client['music']
    except ConnectionError:
        print('Error de conexion con la base de datos')
    return db

