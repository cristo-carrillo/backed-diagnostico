from conexion import conexion_mongo

class Kin:
    
    def __init__(self,user_main, name_main,user_second,name_second,parentesco):
        self.user_main = user_main
        self.name_main = name_main
        self.user_second = user_second
        self.name_second = name_second
        self.parentesco = parentesco
    
    def insert_kin(self):
        collect = conexion_mongo.bd_conexion[0].kin
        collect.insert_one({
                "user_main": self.user_main, 
                "name_main": self.name_main,
                "user_second": self.user_second, 
                "name_second": self.name_second,
                "parentesco": self.parentesco
                })
    def insert_kin_many(self, kin_one):
        collect = conexion_mongo.bd_conexion[0].kin
        collect.insert_many([{
                "user_main": kin_one.user_main, 
                "name_main": kin_one.name_main,
                "user_second": kin_one.user_second, 
                "name_second": kin_one.name_second,
                "parentesco": kin_one.parentesco
                },
                {
                "user_main": self.user_main, 
                "name_main": self.name_main,
                "user_second": self.user_second, 
                "name_second": self.name_second,
                "parentesco": self.parentesco
                }])
    
    @classmethod
    def search_familiar_mod(self,email):
        try:
            if email is None:
                return None
            busqueda = conexion_mongo.bd_conexion[0].kin.find({
                'user_main':email,
                },
                {
                'user_second':1,
                'name_second':1,
                '_id':0
                })
            cant_kin = []
            
            for i in busqueda:
                cant_kin.append(i)
            busqueda.close()
            return cant_kin
        
        except Exception as e:
            print(e)
            return None
    
