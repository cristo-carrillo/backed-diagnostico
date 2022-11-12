from flask import Blueprint, request, jsonify
from algoritmo_diagnostico import diagnosticate
from controller.diagnosis_controller import insert_diagnosis, adapt_sintomas,query_sintomas

diagnosis = Blueprint('diagnosis', __name__)


@diagnosis.route("/diagnostico", methods=['GET', 'POST'])
def diagnostico():
    sintomas_paciente = request.get_json()
    print(f"2: {sintomas_paciente}")
    result_diagnosis = diagnosticate(adapt_sintomas(sintomas_paciente['factores']))
    insert_diagnosis(sintomas_paciente, result_diagnosis)
    return jsonify(result_diagnosis)

@diagnosis.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@diagnosis.route('/historial')
def historial():
    print(request.args.get('email'))
    query_sintomas(request.args.get('email'))
    return jsonify({"code": "ok"})