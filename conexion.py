from pymongo import MongoClient 
import os
from dotenv import load_dotenv

load_dotenv()
# print(f"mongodb+srv://{os.getenv('USER_DB')}:{os.getenv('PASSWORD_DB')}{os.getenv('CLUSTER')}/{os.getenv('NAME_DB')}?retryWrites=true&w=majority")
class conexion_mongo:
    
    bd_conexion = []
    def __init__(self):
        conexion_bd = MongoClient(f"mongodb+srv://{os.getenv('USER_DB')}:{os.getenv('PASSWORD_DB')}{os.getenv('CLUSTER')}/?retryWrites=true&w=majority")
        conexion_mongo.bd_conexion = [conexion_bd[os.getenv('NAME_DB')]]

