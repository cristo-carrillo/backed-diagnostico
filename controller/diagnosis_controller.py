from datetime import datetime
from model.diagnosis_model import Diagnosi


def insert_diagnosis(sintomas_paciente, result_diagnosis):
    diagnosis_mo = Diagnosi(sintomas_paciente['email'], datetime.now(),
                            sintomas_paciente['factores'], result_diagnosis['probability'])
    diagnosis_mo.insert_sintomas()


def query_sintomas(email):
    historial_diag = Diagnosi()
    # Diagnosi().query_sintomas(email)

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
