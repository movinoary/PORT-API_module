from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import os
import response
import base64
import json
import random
import string
import jwt

app = Flask(__name__)
path = '/api/v-1'
CORS(app)
load_dotenv()

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def custom_id(length):
    random_segment = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
    return random_segment


@app.route("/")
def home():
    return "WELCOME TO VO MODULE"

@app.route(f'{path}/')
def wellcome():
    return response.res_success("Hello") 

@app.route(f'{path}/uuid/<string:element>', methods=['POST'])
def generate_uuid(element):
    code=element.upper()
    id=f"VO{code}-3010-{custom_id(5)}-8246{custom_id(3)}-{custom_id(10)}-{custom_id(5)}"
    return response.res_success(id) 

@app.route(f'{path}/encode-jwt', methods=['POST'])
def encodeJWT():
    data = request.json.get('jwt', '')
    token=jwt.encode(
        data,
        os.getenv("SECRET_KEY"),
        algorithm="HS256"
    )
    return response.res_success(token)

@app.route(f'{path}/decode-jwt', methods=['POST'])
def decodeJWT():
    token = request.json.get('token', '')
    try:
        decode = jwt.decode(
            token, 
            os.getenv("SECRET_KEY"),
            algorithms=["HS256"]
        )
        return response.res_success(decode)
    except jwt.ExpiredSignatureError:
        return response.res_error( "Token has expired")
    except  jwt.InvalidTokenError: 
        return response.res_error("Invalid token")
        
    
@app.route(f'{path}/encode', methods=['POST'])
def encode():
    data = request.json.get('encode', '')
    if not isinstance(data, str):
        data = json.dumps(data)    
    # Encode the data to Base64
    double_encoded_data = base64.b64encode(data.encode("utf-8")).decode()
    result_encoded=double_encoded_data
    return response.res_success(result_encoded)

@app.route(f'{path}/decode', methods=['POST'])
def decode():
    encoded_data = request.json.get('decode', '')
    if not isinstance(encoded_data, str):
        return response.res_error()
    
    try:
        decoded_data = base64.b64decode(encoded_data).decode('utf-8')
        result_decode = decoded_data
        return response.res_success(result_decode)
    except (base64.binascii.Error, UnicodeDecodeError):
        return response.res_error()

@app.route(f'{path}/get-photo/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route(f'{path}/upload-photo/<string:element>', methods=['POST'])
@cross_origin(origins=["http://localhost:3000"])
def upload_file(element):
    if 'file' not in request.files:
        return response.res_error()

    file = request.files['file']
    if file.filename == '':
        return response.res_error()

    if file:
        filename = element+"-"+secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        return response.res_success(f'{path}/get-photo/{filename}')

    return response.res_error()