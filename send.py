import os
from itertools import cycle  
import requests
import hashlib

def make_secret_code():
    return hashlib.sha256(os.urandom(256)).digest()

def lock_file(data, code):
    return bytes(a ^ b for a, b in zip(data, cycle(code)))

file_path = input("Enter file to send: ")
secret_code = make_secret_code()

# Save the key
with open("secret_key.bin", 'wb') as f:
    f.write(secret_code)

# Lock and send file
with open(file_path, 'rb') as f:
    locked_data = lock_file(f.read(), secret_code)

try:
    requests.post("http://localhost:8080", data=locked_data)
    print("File sent to secret server!")
except:
    print("Server not found - did you start spy_server.py?")