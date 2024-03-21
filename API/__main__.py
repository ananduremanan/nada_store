from flask import Flask, jsonify, request
from supaClient import supabase
from cryptography.fernet import Fernet
from cryptData import encrypt_data, generate_key

app = Flask(__name__)
KEY = generate_key()

@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.json
    return data

@app.route('/api/login', methods=['POST'])
def login():
    loginData = request.json
    return jsonify(loginData)

@app.route('/api/signup', methods=['POST'])
def signUp():
    signUpData = request.json
    # Encrypt data using the generated key
    email = encrypt_data(KEY, signUpData["email"])
    userName = encrypt_data(KEY, signUpData["userName"])
    password = encrypt_data(KEY, signUpData["password"])
    password = encrypt_data(KEY, signUpData["phone"])
    userAddress = encrypt_data(KEY, signUpData["userAddress"])
    userAvatar = encrypt_data(KEY, signUpData["userAvatar"])

    # Construct user data dictionary
    signUpData = {
        "is_Active" : "0",
        "is_Delete": "0",
        "email": email.decode(),
        "user_Name": userName.decode(),
        "user_Password": password.decode(),
        "user_Phone": password.decode(),
        "user_Address": userAddress.decode(),
        "user_Avatar": userAvatar.decode()
    }
    
    data, count = supabase.table('dbo.userTable').insert(signUpData).execute()
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)