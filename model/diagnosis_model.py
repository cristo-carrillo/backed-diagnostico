from conexion import bd_conexion

def insert_sintomas(sintomas):
    try:
        collect = bd_conexion.diagnosis
        collect.insert_one(sintomas)
        print("registro agregado")
    except Exception as e:
        print(f"error {e}")
