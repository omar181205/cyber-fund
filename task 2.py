import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Configuration
OUTPUT_DIR = r"C:\Users\omara\OneDrive\Desktop\coursework-cyber fund"

def encrypt_file(filepath, key):
    """Encrypt and overwrite the file using AES-GCM"""
    cipher = AES.new(key, AES.MODE_GCM)
    with open(filepath, 'rb') as f:
        data = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(data)
    with open(filepath, 'wb') as f:
        f.write(cipher.nonce + tag + ciphertext)

def main():
    # 1. Get file to encrypt
    filepath = input("Enter full path of file to encrypt: ").strip()
    
    if not os.path.exists(filepath):
        print("Error: File does not exist")
        return
    
    # 2. Setup output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 3. Generate and save key
    key = get_random_bytes(32)  # AES-256
    key_path = os.path.join(OUTPUT_DIR, "key.bin")
    with open(key_path, 'wb') as f:
        f.write(key)
    
    # 4. Encrypt file
    try:
        encrypt_file(filepath, key)
        print(f"File encrypted successfully")
        print(f"Key saved to: {key_path}")
    except Exception as e:
        print(f"Encryption failed: {str(e)}")

if __name__ == "__main__":
    main()