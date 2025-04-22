import os
import requests

def make_secret_code():
    # Generate a 256-byte secret code using os.urandom
    return os.urandom(256)

def lock_file(data, code):
    # XOR each byte of data with corresponding byte in code (repeating code as needed)
    locked_data = bytearray()
    code_length = len(code)
    for i in range(len(data)):
        locked_data.append(data[i] ^ code[i % code_length])
    return bytes(locked_data)

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