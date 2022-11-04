import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier

data_diabetes = pd.read_csv('DATOS_TABULADOS.csv', delimiter=",")
knn = KNeighborsClassifier(n_neighbors=3)
X = data_diabetes[['edad',	'sexo',	'IMC',	'herencia', 'verduras',	'frutas',	'frecuencia_estres',	'frecuencia_ejercicio',	'tiempo_dormir', 'frecuencia_orina', 'frecencia_cabeza', 'cansancio',
                   'perder_peso', 'infecciones_frecuentes', 'mareos', 'piel_reseca', 'cicatrizar', 'dificultad_mirar']]
y = data_diabetes[['DIABETES']]
knn.fit(X, y)


def respuestas_frecuencia():
    return """  
    1:No sabe
    2:Nunca
    3:Rara vez
    4:Algunas veces
    5:Casi Siempre
    6:Siempre\n"""


def solicitar_sintomas():
    sintomas_paciente = {}
    sintomas_paciente['edad'] = [int(input('1. ¿Cuántos años tiene? '))]
    sintomas_paciente['sexo'] = [
        int(input('2 ¿Cuál es su sexo? \n  1:hombre\n  2:mujer \n'))]
    altura = float(input('3 ¿Cuál es su altura en metros? '))
    peso = int(input('4 ¿Cuál es su peso en kg? '))
    sintomas_paciente['IMC'] = [int(peso/(altura**2))]
    sintomas_paciente['herencia'] = [int(input(
        '5. ¿Le han diagnosticado diabetes a alguno de sus familiares ?\n  1:No sabe\n  2:No\n  3:Si \n'))]
    sintomas_paciente['verduras'] = [
        int(input(f'6. ¿Qué tan frecuente consumes verduras? {respuestas_frecuencia()}'))]
    sintomas_paciente['frutas'] = [
        int(input(f'7. ¿Qué tan frecuente consumes frutas? {respuestas_frecuencia()}'))]
    sintomas_paciente['frecuencia_estres'] = [
        int(input(f'8. ¿Qué tan frecuente te estresas ? {respuestas_frecuencia()}'))]
    sintomas_paciente['frecuencia_ejercicio'] = [
        int(input(f'9. ¿Qué tan frecuente hace ejercicio? {respuestas_frecuencia()}'))]
    sintomas_paciente['tiempo_dormir'] = [int(input(
        '10. ¿Cuántas horas duerme al día ? \n  1:No sabe\n  2:Menos de 8 horas\n  3:Mas de 8 horas\n'))]
    sintomas_paciente['frecuencia_orina'] = [
        int(input(f'11.  ¿Qué tan frecuente orina al día? {respuestas_frecuencia()}'))]
    sintomas_paciente['frecencia_cabeza'] = [int(
        input(f'12. ¿Qué tan frecuente le duele la cabeza? {respuestas_frecuencia()}'))]
    sintomas_paciente['cansancio'] = [int(input(
        f'13. ¿Al hacer alguna actividad te cansas fácilmente? {respuestas_frecuencia()}'))]
    sintomas_paciente['perder_peso'] = [int(input(
        f'14. ¿Qué tan frecuente pierdes peso sin causa aparente? {respuestas_frecuencia()}'))]
    sintomas_paciente['infecciones_frecuentes'] = [
        int(input(f'15. ¿Te aparecen infecciones frecuentes? {respuestas_frecuencia()}'))]
    sintomas_paciente['mareos'] = [int(input(
        f'16. ¿Qué tan frecuente te mareas sin causa aparente? {respuestas_frecuencia()}'))]
    sintomas_paciente['piel_reseca'] = [int(input(
        f'17. ¿Tu piel se te reseca sin causa aparente? {respuestas_frecuencia()}'))]
    sintomas_paciente['cicatrizar'] = [int(input(
        f'18. ¿Qué tan frecuente tus llagas o heridas tardan en cicatrizar? {respuestas_frecuencia()}'))]
    sintomas_paciente['dificultad_mirar'] = [int(input(
        f'19. ¿Tiene dificultades para mirar algún objeto? {respuestas_frecuencia()}'))]
    return sintomas_paciente


def validar_datos(data):
    if data == 100.00:
        return 85.00
    return data


def data_prueba():
    return {'edad': [58],
            'sexo': [1],
            'IMC': [24],
            'herencia': [3],
            'verduras': [3],
            'frutas': [3],
            'frecuencia_estres': [3],
            'frecuencia_ejercicio': [2],
            'tiempo_dormir': [2],
            'frecuencia_orina': [2],
            'frecencia_cabeza': [5],
            'cansancio': [2],
            'perder_peso': [4],
            'infecciones_frecuentes': [4],
            'mareos': [3],
            'piel_reseca': [3],
            'cicatrizar': [3],
            'dificultad_mirar': [3]}


# sintomas_paciente = data_prueba()

# sintomas_paciente = data_prueba()
def diagnosticate(sintomas_paciente):
    prediccion = knn.predict_proba(pd.DataFrame(sintomas_paciente))
    return f"Usted tiene un {validar_datos(round(prediccion[0][1]*100,2))}% de probabilidad de padecer diabetes"
