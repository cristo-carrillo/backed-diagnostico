from flask import Blueprint, request, jsonify, abort
from utils.emails_diagnosis import send_email
from controller.kin_controller import insert_kin_family

kin = Blueprint('kin', __name__)


@kin.route('/add_parentesco')
def add_parentesco():
    data_parentesco = request.get_json()
    print(data_parentesco)
    insert_kin_family(data_parentesco)
    return send_email(data_parentesco['user_second'])