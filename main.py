from flask import Flask, request
import response
import base64
import json
import random
import string

app = Flask(__name__)
path = '/api/v-1'

def custom_id(length):
    random_segment = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
    return random_segment

@app.route(f'{path}/uuid/<string:element>', methods=['POST'])
def generate_uuid(element):
    code=element.upper()
    id=f"VO{code}-3010-{custom_id(5)}-8246{custom_id(3)}-{custom_id(10)}-{custom_id(5)}"
    return response.res_success(id) 
    
@app.route(f'{path}/encode', methods=['POST'])
def encode():
    data = request.json.get('encode', '')
    if not isinstance(data, str):
        data = json.dumps(data)    
    # Encode the data to Base64
    encoded_data = base64.b64encode(data.encode('utf-32-be')).decode()
    double_encoded_data = base64.b64encode(encoded_data.encode("utf-8")).decode()
    result_encoded=double_encoded_data
    return response.res_success(result_encoded)

@app.route(f'{path}/decode', methods=['POST'])
def decode():
    encoded_data = request.json.get('decode', '')
    if not isinstance(encoded_data, str):
        return response.res_error()
    
    try:
        decoded_data = base64.b64decode(encoded_data).decode('utf-8')
        double_decoded_data = base64.b64decode(decoded_data).decode('utf-32-be')
        result_decode = double_decoded_data
        return response.res_success(result_decode)
    except (base64.binascii.Error, UnicodeDecodeError):
        return response.res_error()