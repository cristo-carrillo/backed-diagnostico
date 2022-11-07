from flask import Blueprint, request, jsonify
from algoritmo_diagnostico import diagnosticate
from controller.diagnosis_controller import insert_diagnosis

diagnosis = Blueprint('diagnosis', __name__)

@diagnosis.route("/diagnostico", methods=['GET', 'POST'])
def diagnostico():
    sintomas_paciente = request.get_json()
    insert_diagnosis(sintomas_paciente)
    print(f"2: {sintomas_paciente}")
    header_req()
    return diagnosticate(sintomas_paciente)


def header_req():
    print(request.headers['Host'])

@diagnosis.route('/')
def index():
    header_req()
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})