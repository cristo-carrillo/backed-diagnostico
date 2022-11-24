from model.kin_model import Kin
from utils.emails_diagnosis import send_email

def insert_kin_family(dict_kin):
    kin_one = format_kin(dict_kin)
    parent = kin_one.family_exist()
    if len(parent)>0:
        return {"msg":"El familiar ya estaba asociado"}
    msg = send_email(dict_kin['user_second'], dict_kin['name_main'])
    if msg['cod'] == '00':
        dict_kin_two = determinate_kin(dict_kin)
        kin_two = format_kin(dict_kin_two)
        kin_two.insert_kin_many(kin_one)
        return {'msg':'Familiar agregado correctamente'}
    return {'msg':'Ups algo salio mal'}

def format_kin(dict_kin):
    
    return Kin(dict_kin['user_main'],
                dict_kin['name_main'],
                dict_kin['user_second'], 
                dict_kin['name_second'],
                dict_kin['parentesco'])

def determinate_kin(dict_kin):
    kin_fam = {'Abuelo':'Nieto',
                'Padre':'Hijo',
                'Nieto':'Abuelo',
                'Hijo':'Padre'}
    return {'user_main':dict_kin['user_second'],
            'name_main':dict_kin['name_second'],
            'user_second':dict_kin['user_main'],
            'name_second':dict_kin['name_main'],
            'parentesco':kin_fam[dict_kin['parentesco']]}
    

def search_familiar_con(email):
    cant_kin = Kin.search_familiar_mod(email)
    if cant_kin is None:
        return []
    if len(cant_kin) == 0:
        return []
    
    return calculate_original(cant_kin)

def calculate_original(cant_kin):
    relacion_nombre = {}
    for i in cant_kin:
        relacion_nombre[i['user_second']] = [i['name_second'],i['parentesco']]
    return Kin.query_as_diagnosis(relacion_nombre)

def search_family_sta(email):
    query_family = Kin.search_familiar_mod(email)
    if query_family is None:
        return []
    if len(query_family) == 0:
        return []
    return calculate_family(query_family)

def calculate_family(query_family):
    relacion_nombre = {}
    for i in query_family:
        relacion_nombre[i['user_second']] = [i['name_second'],i['parentesco']]
    return Kin.search_family_status(relacion_nombre)

def delete_family_con(user_main,user_second):
    return Kin.delete_family_mod(user_main,user_second)

def consult_kin_con(self, email):
    data = Kin.consult_kin(email)
    