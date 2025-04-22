import os
from Crypto.Cipher import AES

def decrypt_file(encrypted_file_path, key_file_path):
    # Check if files exist
    if not os.path.exists(encrypted_file_path):
        print("[ERROR] Encrypted file not found.")
        return

    if not os.path.exists(key_file_path):
        print("[ERROR] Key file not found.")
        return

    # Read the key
    with open(key_file_path, 'rb') as key_file:
        key = key_file.read()

    # Read the encrypted file
    with open(encrypted_file_path, 'rb') as encrypted_file:
        data = encrypted_file.read()

    nonce = data[:16]
    tag = data[16:32]
    ciphertext = data[32:]

    # Decrypt
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    try:
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        # Overwrite the encrypted file with the original content
        with open(encrypted_file_path, 'wb') as decrypted_file:
            decrypted_file.write(plaintext)
        print("[✓] File successfully decrypted and restored.")
    except Exception as e:
        print(f"[ERROR] Decryption failed: {e}")

def main():
    print("[?] Enter path to the key.bin file:")
    key_path = input().strip()

    print("[?] Enter path to the encrypted file you want to decrypt:")
    file_path = input().strip()

    decrypt_file(file_path, key_path)

if __name__ == "__main__":
    main()
