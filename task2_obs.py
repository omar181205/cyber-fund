import os as _0x
from Crypto.Cipher import AES as _1A
from Crypto.Random import get_random_bytes as _2B

# Obfuscated configuration
_3C = r"C:\Users\omara\OneDrive\Desktop\coursework-cyber fund"

def _4D(_5E, _6F):
    """Obfuscated encryption function"""
    _7G = _1A.new(_6F, _1A.MODE_GCM)
    with open(_5E, 'rb') as _8H:
        _9I = _8H.read()
    _0J, _1K = _7G.encrypt_and_digest(_9I)
    with open(_5E, 'wb') as _2L:
        _2L.write(_7G.nonce + _1K + _0J)

def _3M():
    # Obfuscated main function
    _4N = input("[INPUT] Provide target path: ").strip()
    
    if not _0x.path.exists(_4N):
        print("[ERROR] Target not found")
        return
    
    # Create output directory
    _0x.makedirs(_3C, exist_ok=True)
    
    # Generate random key
    _5O = _2B(32)
    _6P = _0x.path.join(_3C, "k3y.b1n")
    with open(_6P, 'wb') as _7Q:
        _7Q.write(_5O)
    
    # Execute encryption
    try:
        _4D(_4N, _5O)
        print("[STATUS] Operation completed")
        print(f"[KEY] Stored at: {_6P}")
    except Exception as _8R:
        print(f"[FAILURE] {str(_8R)}")

if __name__ == "__main__":
    _3M()