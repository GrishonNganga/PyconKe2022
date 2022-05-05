from art_factory import generate_unique_nft
from flask import Flask, request, make_response, jsonify, current_app
from flask_cors import CORS
from functools import wraps
from ipfs import upload
from blockchain import create_account
from datetime import datetime, timedelta
import jwt

# nft = generate_unique_nft()
# response = upload(nft)
# print(response)

app = Flask(__name__)
app.config["APP_SECRET"] = "KSiJ65bGtapUEQeg" 
app.config["DEBUG"] = True
CORS(app, origins=["http://localhost:3000"], supports_credentials = True)


@app.route('/auth', methods=['POST'])
def signup():
    post_data = request.get_json(force=True)  
    private_key = None
    if post_data and "private_key" in post_data:
        private_key = post_data["private_key"] 
    if private_key:
        public_key = create_account(private_key = private_key)       
        response = {'status': 'success', 'message':'Account created successfully', "key": public_key}
        response = make_response(jsonify(response), 200)
        response.set_cookie("public_key", value=public_key, httponly=True, samesite="None", secure=True)  
    else:
        public_key, private_key = create_account(private_key = private_key)        
        response = {'status': 'success', 'message':'Account loaded successfully', "key": {'public': public_key, 'private': private_key}}
        response = make_response(jsonify(response), 200)
        response.set_cookie("public_key", value=public_key, httponly=True, samesite="None", secure=True) 
    return response


@app.route('/refresh_session')
def refresh_token():
    if request.cookies and "public_key" in request.cookies:
        public_key = request.cookies.get("public_key") 
        response = {'status': 'success', 'message':'Admin signin successful','user': public_key}    
        response = make_response(jsonify(response), 200)
    else:
        response = {'status': 'error', 'message': 'Authentication failed'}
        response = make_response(jsonify(response), 400)

    return response


if __name__ == '__main__':
    app.run()