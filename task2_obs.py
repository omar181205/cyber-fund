import os as _0x
from Crypto.Cipher import AES as _1A
from Crypto.Random import get_random_bytes as _2B

def _4D(_5E, _6F):
    _7G = _1A.new(_6F, _1A.MODE_GCM)
    with open(_5E, 'rb') as _8H:
        _9I = _8H.read()
    _0J, _1K = _7G.encrypt_and_digest(_9I)
    with open(_5E, 'wb') as _2L:
        _2L.write(_7G.nonce + _1K + _0J)

def _3M(_4N, _3C="key.bin"):
    if not _0x.path.exists(_4N):
        print("[ERROR] Target not found")
        return

    _0x.makedirs(_0x.path.dirname(_3C) or ".", exist_ok=True)
    _5O = _2B(32)

    with open(_3C, 'wb') as _7Q:
        _7Q.write(_5O)

    try:
        _4D(_4N, _5O)
        print(f"[✓] Log file encrypted. Key saved to: {_3C}")
    except Exception as _8R:
        print(f"[FAILURE] {str(_8R)}")
