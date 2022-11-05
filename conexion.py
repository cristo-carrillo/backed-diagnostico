from pymongo import MongoClient 
import os
from dotenv import load_dotenv

load_dotenv()

conexion_bd = MongoClient(f"mongodb+srv://{os.getenv('USER_DB')}:{os.getenv('PASSWORD_DB')}{os.getenv('CLUSTER')}/?retryWrites=true&w=majority")
# print(f"mongodb+srv://{os.getenv('USER_DB')}:{os.getenv('PASSWORD_DB')}{os.getenv('CLUSTER')}/{os.getenv('NAME_DB')}?retryWrites=true&w=majority")
gha = conexion_bd['diabetes']
dblist = gha['country']

def close_sesion():
    conexion_bd.close()
