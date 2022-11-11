from flask import Blueprint, request, jsonify
from algoritmo_diagnostico import diagnosticate
from controller.diagnosis_controller import insert_diagnosis, adapt_sintomas

diagnosis = Blueprint('diagnosis', __name__)

@diagnosis.route("/diagnostico", methods=['GET', 'POST'])
def diagnostico():
    sintomas_paciente = request.get_json()
    insert_diagnosis(sintomas_paciente)
    print(f"2: {sintomas_paciente}")
    header_req()
    sintomas_copia = adapt_sintomas(sintomas_paciente)
    return jsonify(diagnosticate(sintomas_copia))


def header_req():
    print(request.remote_addr)

@diagnosis.route('/')
def index():
    header_req()
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})