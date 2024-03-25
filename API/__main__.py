from flask import Flask, jsonify, request
from supaClient import supabase
from cryptography.fernet import Fernet
from cryptData import encrypt_data, decrypt_data, generate_key

app = Flask(__name__)
KEY = generate_key()

@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.json
    return data

@app.route('/api/login', methods=['POST'])
def login():
    loginData = request.json
    try:
        userName = loginData["userName"]
        password = loginData["password"]
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/signup', methods=['POST'])
def signUp():
    signUpData = request.json
    try:
        # Encrypt data using the generated key
        userName = encrypt_data(KEY, signUpData["userName"])
        password = encrypt_data(KEY, signUpData["password"])
        phone = encrypt_data(KEY, signUpData["phone"])
        userAddress = encrypt_data(KEY, signUpData["userAddress"])
        userAvatar = encrypt_data(KEY, signUpData["userAvatar"])

        # Construct user data dictionary
        userData = {
            "is_Active" : "0",
            "is_Delete": "0",
            "email": signUpData["email"],
            "user_Name": userName.decode(),
            "user_Password": password.decode(),
            "user_Phone": phone.decode(),
            "user_Address": userAddress.decode(),
            "user_Avatar": userAvatar.decode()
        }

        # Check if the provided username already exists in the database
        existing_user = supabase.table('dbo.userTable').select('id').eq('email', userData["email"]).execute()

        if len(existing_user.data) > 0:
            return jsonify({"status": "user already exists"}), 400
        else:
            # Insert user data into the database table
            data = supabase.table('dbo.userTable').insert(userData).execute()
            
            # Extract relevant data for response
            if data.data:
                inserted_data = data.data[0]
                return jsonify({"data": inserted_data, "status": "user created successfully"})
            else:
                return jsonify({'error': 'No data returned from the database.'}), 400
        
    except Exception as e:
        # Return an error response with status code 400 Bad Request
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)