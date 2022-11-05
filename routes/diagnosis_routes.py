from flask import Blueprint, request
from main import diagnosticate

diagnosis = Blueprint('diagnosis', __name__)

@diagnosis.route("/diagnostico", methods=['GET', 'POST'])
def diagnostico():
    sintomas_paciente = request.get_json()
    print(sintomas_paciente)
    return diagnosticate(sintomas_paciente)