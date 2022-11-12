from conexion import bd_conexion


class Diagnosi:
    def __init__(self):
        print('hola')
    
    def __init__(self,email, fecha_diagnostico, factores, prob_diagnostico):
        self.email = email
        self.fecha_diagnostico = fecha_diagnostico
        self.factores = factores
        self.prob_diagnostico = prob_diagnostico
    
    def insert_sintomas(self):
        try:
            collect = bd_conexion.diagnosis
            collect.insert_one({"email": self.email, "fecha_diagnostico": self.fecha_diagnostico,
                                "prob_diagnostico": self.prob_diagnostico, "factores": self.factores})
            print("diagnostocp agregado")
        except Exception as e:
            print(f"error {e}")
    
    def query_sintomas(self, email):
        busqueda = bd_conexion.diagnosis.find({'email':email})
        for i in busqueda:
            print(i)
