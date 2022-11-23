from flask import Blueprint, request, jsonify, abort
from utils.emails_diagnosis import send_email
from controller.kin_controller import insert_kin_family, search_familiar_con

kin = Blueprint('kin', __name__)


@kin.route('/add_parentesco')
def add_parentesco():
    data_parentesco = request.get_json()
    print(data_parentesco)
    if insert_kin_family(data_parentesco) == 0:
        return jsonify({"msg":"el familiar ya estaba asociado"})
    return send_email(data_parentesco['user_second'])

@kin.route('/search_familiar/<email>')
def search_familiar(email):
    return jsonify(search_familiar_con(email))