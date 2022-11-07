from pymongo import MongoClient 
import os
from dotenv import load_dotenv

load_dotenv()
# print(f"mongodb+srv://{os.getenv('USER_DB')}:{os.getenv('PASSWORD_DB')}{os.getenv('CLUSTER')}/{os.getenv('NAME_DB')}?retryWrites=true&w=majority")
conexion_bd = MongoClient(f"mongodb+srv://{os.getenv('USER_DB')}:{os.getenv('PASSWORD_DB')}{os.getenv('CLUSTER')}/?retryWrites=true&w=majority")

bd_conexion = conexion_bd[os.getenv('NAME_DB')]

def close_sesion():
    conexion_bd.close()
