from flask import Blueprint, request, jsonify, abort
from algoritmo_diagnostico import diagnosticate
from controller.diagnosis_controller import insert_diagnosis, adapt_sintomas, query_diagnosis, query_sintomas

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
    email = request.args.get('email')
    fecha = request.args.get('fecha')
    if email is None:
        return jsonify({'error':'email is required'})
    if fecha is None or fecha=='':
        return jsonify({'error':'date is required'})
    if fecha.count('-') < 2:
        return jsonify({'error':'format date incorrect'})
    historial_diagnosis = query_diagnosis(email=email, fecha=fecha)
    if historial_diagnosis is None:
        return abort(500)
    return jsonify(historial_diagnosis)

@diagnosis.route('/historial/pie/<id>')
def historial_pie(id):
    result_query = query_sintomas(id)
    if result_query is None:
        return abort(500)
    return jsonify(result_query)