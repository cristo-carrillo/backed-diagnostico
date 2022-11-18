from model.diagnosis_model import Diagnosi
from bson.objectid import ObjectId
from utils.dates import calculate_today

def insert_diagnosis(sintomas_paciente, result_diagnosis):
    if result_diagnosis['probability'] != -1:
        diagnosis_mo = Diagnosi(sintomas_paciente['email'], calculate_today(),
                                sintomas_paciente['factores'], result_diagnosis['probability'])
        diagnosis_mo.insert_sintomas()


def query_diagnosis(email=None,fecha=None):
    return Diagnosi.query_diagnosis(email=email, fecha=fecha)

def query_sintomas(id):
    sintomas = ['frecuencia_orina','frecencia_cabeza','cansancio','perder_peso','infecciones_frecuentes',
                'mareos','piel_reseca','cicatrizar','dificultad_mirar']
    try:
        resp_sintomas = Diagnosi.query_sintomas(ObjectId(id))
        if resp_sintomas is None:
            return None
        sintomas_may = {}
        for key,value in resp_sintomas[0].get('factores').items():
            if key in sintomas and value[0] > 3:
                sintomas_may[key] = value[0]
        return sintomas_may
    except Exception:
        return None

def adapt_sintomas(sintomas):
    return {
            'edad': sintomas['edad'],
            'sexo': sintomas['sexo'],
            'IMC': sintomas['IMC'],
            'herencia': sintomas['herencia'],
            'verduras': sintomas['verduras'],
            'frutas': sintomas['frutas'],
            'frecuencia_estres': sintomas['frecuencia_estres'],
            'frecuencia_ejercicio': sintomas['frecuencia_ejercicio'],
            'tiempo_dormir': sintomas['tiempo_dormir'],
            'frecuencia_orina': sintomas['frecuencia_orina'],
            'frecencia_cabeza': sintomas['frecencia_cabeza'],
            'cansancio': sintomas['cansancio'],
            'perder_peso': sintomas['perder_peso'],
            'infecciones_frecuentes': sintomas['infecciones_frecuentes'],
            'mareos': sintomas['mareos'],
            'piel_reseca': sintomas['piel_reseca'],
            'cicatrizar': sintomas['cicatrizar'],
            'dificultad_mirar': sintomas['dificultad_mirar']
            }
