import os
import smtplib

# Email settings - fill these in with your details
YOUR_EMAIL = "your_email@gmail.com"
YOUR_PASSWORD = "your_app_password"  # Use an app password if 2FA is enabled
BOSS_EMAIL = "boss@example.com"

def create_key():
    """Generate a random 32-byte key"""
    return os.urandom(32)

def encrypt_file(data, key):
    """Simple XOR encryption"""
    encrypted = bytearray()
    for i in range(len(data)):
        encrypted.append(data[i] ^ key[i % len(key)])
    return bytes(encrypted)

def send_email(filename):
    """Send an email notification"""
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(YOUR_EMAIL, YOUR_PASSWORD)
            
            message = f"""From: {YOUR_EMAIL}
To: {BOSS_EMAIL}
Subject: Secret File: {filename}

The secret file has been secured!
"""
            server.sendmail(YOUR_EMAIL, BOSS_EMAIL, message)
        print("Message sent successfully!")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

def main():
    print("=== Secret File Encryptor ===")
    file_path = input("Enter file path: ")
    
    if not os.path.exists(file_path):
        print("Error: File not found")
        return
    
    # Generate and save key
    key = create_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key saved to secret.key")
    
    # Encrypt file
    with open(file_path, "rb") as f:
        original = f.read()
    
    encrypted = encrypt_file(original, key)
    encrypted_path = file_path + ".enc"
    with open(encrypted_path, "wb") as f:
        f.write(encrypted)
    print(f"File encrypted and saved as {encrypted_path}")
    
    # Send notification
    if send_email(os.path.basename(file_path)):
        print("Mission complete!")
    else:
        print("Mission failed - email not sent")

if __name__ == "__main__":
    main()