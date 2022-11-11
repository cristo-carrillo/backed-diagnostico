
from model.diagnosis_model import insert_sintomas

def insert_diagnosis(sintomas):
    insert_sintomas(sintomas.copy())


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
