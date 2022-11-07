from flask import Blueprint, request, jsonify
from algoritmo_diagnostico import diagnosticate
from controller.diagnosis_controller import insert_diagnosis

diagnosis = Blueprint('diagnosis', __name__)

@diagnosis.route("/diagnostico", methods=['GET', 'POST'])
def diagnostico():
    sintomas_paciente = request.get_json()
    print(f"1: {sintomas_paciente}")
    insert_diagnosis(sintomas_paciente)
    print(f"2: {sintomas_paciente}")
    return diagnosticate(sintomas_paciente)

@diagnosis.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})