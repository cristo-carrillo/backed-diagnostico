from conexion import gha, close_sesion

def insert(sintomas):
    try:
        collect = gha.diagnosis
        collect.insert_one(sintomas)
        close_sesion()
    except Exception:
        pass