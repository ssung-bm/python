import pickle
import base64
from Crypto.Cipher import AES

# ⚠️ 
def load_user_session(session_data):
    # VULN: Pickle deserialization of untrusted data
    try:
        data = base64.b64decode(session_data)
        return pickle.loads(data)
    except Exception as e:
        return None

# ⚠️ 
def encrypt_password(password):
    # VULN: Using MD5 for password hashing
    import hashlib
    return hashlib.md5(password.encode()).hexdigest()

# ⚠️ ECB 
def encrypt_data(data, key):
    # VULN: AES in ECB mode (insecure)
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(data)
