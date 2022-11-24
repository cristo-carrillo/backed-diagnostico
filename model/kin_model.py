from conexion import conexion_mongo
import pymongo

class Kin:

    def __init__(self, user_main, name_main, user_second, name_second, parentesco):
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

    def family_exist(self):
        busqueda = conexion_mongo.bd_conexion[0].kin.find({
            '$and':[{'user_main':self.user_main},{'user_second':self.user_second},{'parentesco':self.parentesco}]
        },{'parentesco':1})
        return  [i for i in busqueda]
    
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
    def search_familiar_mod(self, email):
        try:
            if email is None:
                return None
            busqueda = conexion_mongo.bd_conexion[0].kin.find({
                'user_main': email,
            },
                {
                'user_second': 1,
                'name_second': 1,
                'parentesco': 1,
                '_id': 0
            })
            cant_kin = []

            for i in busqueda:
                cant_kin.append(i)
            busqueda.close()
            return cant_kin

        except Exception as e:
            print(e)
            return None

    @classmethod
    def query_as_diagnosis(self, email):
        try:
            family = []
            for i,name in email.items():
                busqueda = conexion_mongo.bd_conexion[0].diagnosis.find({
                    'email': i},
                    {'email': 1,
                    "prob_diagnostico": 1,
                    "fecha_diagnostico":1,
                    '_id': 0}
                ).sort('fecha_diagnostico',pymongo.DESCENDING).limit(1)
                data_bus = [i for i in busqueda if len(i)>0]
                if len(data_bus) > 0:
                    data_bus[0]['family_name'] = name[0]
                    data_bus[0]['parentesco'] = name[1]
                    data_bus[0]['fecha_diagnostico'] = data_bus[0]['fecha_diagnostico'].strftime("%Y-%m-%d")
                    family.append(data_bus[0])
                busqueda.close()
            return family
        except Exception as e:
            print(e)
            return None
    
    @classmethod
    def search_family_status(self, email):
        try:
            family = []
            for i,name in email.items():
                busqueda = conexion_mongo.bd_conexion[0].diagnosis.find({
                    'email': i},
                    {'email': 1,
                    '_id': 0}
                ).sort('fecha_diagnostico',pymongo.DESCENDING).limit(1)
                data_bus = [j for j in busqueda if len(j)>0]
                if len(data_bus) > 0:
                    data_bus[0]['family_name'] = name[0]
                    data_bus[0]['parentesco'] = name[1]
                    data_bus[0]['status'] = True
                    family.append(data_bus[0])
                else:
                    family.append({'email':i,'family_name':name[0],'parentesco':name[1],'status':False})
                busqueda.close()
            return family
        except Exception as e:
            print(e)
            return None
    @classmethod
    def delete_family_mod(self,user_main,user_second):
        try:
            deletecount = conexion_mongo.bd_conexion[0].kin.delete_many({
            '$or':[{
                '$and':[{'user_main':user_main},{'user_second':user_second}]},
                {'$and':[{'user_main':user_second},{'user_second':user_main}]}]})
            return deletecount.deleted_count
        except Exception as e:
            print(e)
            return 0