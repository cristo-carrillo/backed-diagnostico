from pymongo import MongoClient 

ID_ARTICULO=""
DATOS_CONECTION={"CONEXION_URL":"mongodb+srv://user:password@cluster0.g2jumcx.mongodb.net/?retryWrites=true&w=majority"}
# DATOS_CONECTION={"CONEXION_URL":"mongodb://localhost:27017/","NAME_DATABASE":"tienda","NAME_COLLECTION":"articulos"}

client = MongoClient(DATOS_CONECTION["CONEXION_URL"])

try:
    print(client.server_info())
except Exception as e:
    print(e)
    print("Unable to connect to the server.")
    
client.close()