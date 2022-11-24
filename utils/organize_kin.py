def organization(data):
    {'Abuelo':'Nieto',
    'Padre':'Hijo',
    'Hijo':'Padre',
    'Nieto':'Abuelo'}
    data_abuelo=[]
    data_nieto = []
    data_padre = []
    data_hijo = []
    for i in data:
        if i['parentesco'] == 'Nieto':
            data_abuelo.append({'label':'Abuelo',
                                'data':{'name':i['name_second'],'avatar':''}})
        if i['parentesco'] == 'Hijo':
            data_padre.append({'label':'Padre',
                                'data':{'name':i['name_second'],'avatar':''}})
        if i['parentesco'] == 'Padre':
            data_hijo.append({'label':'Hijo',
                                'data':{'name':i['name_second'],'avatar':''}})
        if i['parentesco'] == 'Abuelo':
            data_hijo.append({'label':'Nieto',
                                'data':{'name':i['name_second'],'avatar':''}})
    #if len()