from art_factory import generate_unique_nft
from flask import Flask, request, make_response, jsonify, current_app
from flask_cors import CORS
from functools import wraps
from ipfs import upload
from blockchain import create_account, get_eth_balance, mint_price, purchase_nft, nfts_for_user
from datetime import datetime, timedelta

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
        nfts = nfts_for_user(public_key)
        print(nfts)
        response = {'status': 'success', 'message':'Admin signin successful','user': public_key, 'nfts': nfts}    
        response = make_response(jsonify(response), 200)
    else:
        response = {'status': 'error', 'message': 'Authentication failed'}
        response = make_response(jsonify(response), 400)

    return response

@app.route('/get_user_balance')
def get_user_balance():
    if request.cookies and "public_key" in request.cookies:
        public_key = request.cookies.get("public_key") 
        balance = get_eth_balance(public_key)
        response = {'status': 'success','balance': balance}    
        response = make_response(jsonify(response), 200)
    else:
        response = {'status': 'error', 'message': 'User not provided'}
        response = make_response(jsonify(response), 400)
    
    return response

@app.route('/get_nft_price')
def get_price():
    price = mint_price()
    response = {'status': 'success','price': price}    
    response = make_response(jsonify(response), 200)
    return response


@app.route('/generate_nft', methods=['POST'])
def generate_nft():
    post_data = request.get_json(force=True) 
    if not request.cookies or "public_key" not in request.cookies or not post_data or "private_key" not in post_data:
        response = {'status': 'error', 'message': 'Provide all details'}
        response = make_response(jsonify(response), 400)
        return response
    
    public_key = request.cookies.get("public_key") 
    private_key = post_data["private_key"]
    match_public_key = create_account(private_key)

    if match_public_key != public_key:
        response = {'status': 'error', 'message': 'Provide correct details'}
        response = make_response(jsonify(response), 400)
        return response


    if get_eth_balance(public_key) < mint_price():
        response = {'status': 'error', 'message': 'Insufficient balance to generate NFT'}
        response = make_response(jsonify(response), 400)
        return response
    
    nft = generate_unique_nft()
    response = upload(nft)
    if response:
        IpfsHash = response['IpfsHash']
        nft, message = purchase_nft(IpfsHash, public_key, private_key)
        if nft:
            response = {'status': 'error', 'message': 'NFT created successfully'}
            response = make_response(jsonify(response), 200)
            return response
        else:
            response = {'status': 'error', 'message': message}
            response = make_response(jsonify(response), 400)
            return response

if __name__ == '__main__':
    app.run()