from cryptography.fernet import Fernet

# Generate a random key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt data using the generated key
def encrypt_data(key, data):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Decrypt data using the key
def decrypt_data(key, encrypted_data):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data