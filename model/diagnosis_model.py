from conexion import gha, close_sesion

def insert_sintomas(sintomas):
    try:
        collect = gha.diagnosis
        collect.insert_one(sintomas)
        close_sesion()
        print("registro agregado")
    except Exception as e:
        print(f"error {e}")
        pass