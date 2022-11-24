from flask import Blueprint, request, jsonify, abort
from utils.emails_diagnosis import send_email
from controller.kin_controller import insert_kin_family, search_familiar_con,search_family_sta,delete_family_con

kin = Blueprint('kin', __name__)


@kin.route('/add_parentesco',methods=['POST'])
def add_parentesco():
    data_parentesco = request.get_json()
    print(data_parentesco)
    if insert_kin_family(data_parentesco) == 0:
        return jsonify({"msg":"El familiar ya estaba asociado"})
    return send_email(data_parentesco['user_second'], data_parentesco['name_main'])

@kin.route('/add_parentesco',methods=['GET'])
def add_parentesco_con():
    email = request.args.get('email')
    if email is None:
        return jsonify({'error':'Email is required'})
    result_bus = search_family_sta(email)
    if result_bus is None:
        return jsonify({'error':'Ups algo salio mal'})
    return jsonify(result_bus)

@kin.route('/search_familiar/<email>')
def search_familiar(email):
    result_bus = search_familiar_con(email)
    if result_bus is None:
        return jsonify({'error':'Ups algo salio mal'})
    return jsonify(result_bus)

@kin.route('/delete_familiar', methods=['DELETE'])
def eliminar_familiar():
    user_main = request.args.get('user_main')
    user_second = request.args.get('user_second')
    if user_main is None or user_second is None:
        return jsonify({'error':'User required'})
    return jsonify({'msg':delete_family_con(user_main, user_second)})
    