from model.kin_model import Kin

def insert_kin_family(dict_kin):
    kin_one = format_kin(dict_kin)
    dict_kin_two = determinate_kin(dict_kin)
    kin_two = format_kin(dict_kin_two)
    kin_two.insert_kin_many(kin_one)

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