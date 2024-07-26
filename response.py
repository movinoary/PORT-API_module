from flask import jsonify

def res_success(data):
    return jsonify({'status':200,'message': "Success", 'data': data}), 200

def res_error():
    return jsonify({'status':400,'message': "Error"}), 400