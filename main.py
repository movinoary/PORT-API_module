from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
import response
import base64
import json
import random
import string

app = Flask(__name__)
path = '/api/v-1'

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def custom_id(length):
    random_segment = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
    return random_segment

@app.route(f'{path}/')
def wellcome():
    return response.res_success("Hello") 

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

@app.route(f'{path}/get-photo/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route(f'{path}/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return response.res_error()

    file = request.files['file']
    if file.filename == '':
        return response.res_error()

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        return response.res_success(f'{path}/get-photo/{filename}')

    return response.res_error()