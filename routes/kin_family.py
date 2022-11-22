from flask import Blueprint, request, jsonify, abort

kin = Blueprint('kin', __name__)

@kin.route('/parentesco')
def parentesco():
    pass