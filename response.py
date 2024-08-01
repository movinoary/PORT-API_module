from flask import jsonify

def res_success(data):
    return jsonify({'status':200,'message': "Success", 'data': data}), 200

def res_error(message):
    return jsonify({'status':400,'message': message}), 400