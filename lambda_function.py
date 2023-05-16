import json
from app.service.GeneratePassword import PasswordGenerator
from app.models.PasswordModel import RequestPassword
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def lambda_handler():
    json_data = request.get_json()

    request_password = RequestPassword(
        email=json_data['email'],
        password=json_data['password'],
        max_views=json_data['max_views'],
        valid_days=json_data['valid_days'],
        use_symbols=json_data['use_symbols'],
        use_numbers=json_data['use_numbers'],
        use_words=json_data['use_words'],
        length=json_data['length']
    )
    
    p = PasswordGenerator()
    password_data = p.generate_password_data(request_password=request_password)
    
    if password_data:
        return jsonify(
			message='Password criado com sucesso',
			response= 'ok'
		)
    else:
        return jsonify(
			message='Problema ao criar password',
			response= ''
		)
    

