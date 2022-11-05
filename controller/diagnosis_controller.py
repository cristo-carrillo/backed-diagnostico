
from conexion import conexion_bd, close_sesion

def insert_diagnosis(sintomas):
    collection_db = conexion_bd.diagnosis
    print(collection_db)
    # 
    # close_sesion()
    collection_db.insert_one({'pio':'pio'})
    