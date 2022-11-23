from conexion import conexion_mongo
from datetime import datetime
class Diagnosi:
    
    def __init__(self,email, fecha_diagnostico, factores, prob_diagnostico):
        self.email = email
        self.fecha_diagnostico = fecha_diagnostico
        self.factores = factores
        self.prob_diagnostico = prob_diagnostico
    
    def insert_sintomas(self):
        try:
            collect = conexion_mongo.bd_conexion[0].diagnosis
            collect.insert_one({
                "email": self.email, 
                "fecha_diagnostico": self.fecha_diagnostico,
                "prob_diagnostico": self.prob_diagnostico, 
                "factores": self.factores
                })
            print("diagnostocp agregado")
        except Exception as e:
            print(f"error {e}")
    
    @classmethod
    def query_diagnosis(self, email=None, fecha = None):
        try:
            if fecha is None and email is None:
                return None
            filtro_fecha ={"$gt" : datetime.fromisoformat(fecha)}
            busqueda = conexion_mongo.bd_conexion[0].diagnosis.find({
                'email':email,
                "fecha_diagnostico":filtro_fecha
                },
                {
                'factores':0,
                'email':0
                })
            historial_diag = []
            
            for i in busqueda:
                i['_id'] = str(i['_id'])
                i['fecha_diagnostico'] = i['fecha_diagnostico'].strftime("%Y-%m-%d")
                historial_diag.append(i)
            busqueda.close()
            return historial_diag
        
        except Exception as e:
            print(e)
            return None
        
    @classmethod
    def query_sintomas(self, id):
        try:
            if id is None:
                return None
            busqueda = conexion_mongo.bd_conexion[0].diagnosis.find({
                '_id':id
                },
                {
                'factores':1,
                '_id':0
                })
            historial_sint = []
            for i in busqueda:
                historial_sint.append(i)
            
            busqueda.close()
            return historial_sint
        except Exception as e:
            print(e)
            return None
