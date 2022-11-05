from flask import Blueprint, request
from main import diagnosticate
from controller.diagnosis_controller import insert_diagnosis

diagnosis = Blueprint('diagnosis', __name__)

@diagnosis.route("/diagnostico", methods=['GET', 'POST'])
def diagnostico():
    sintomas_paciente = request.get_json()
    print(sintomas_paciente)
    insert_diagnosis(sintomas_paciente)
    return diagnosticate(sintomas_paciente)

@diagnosis.route("/")
def pio():
    return '{"prueba":12}'