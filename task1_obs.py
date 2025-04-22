import os as _0x
from docx import Document as xQ42

def rN21(a1, b2):
    return _0x.path.join(a1, b2)

def X99(zT78, k9p3):
    print(f"[DEBUG] Scanning folder: {zT78}")
    found = False
    with open(k9p3, 'w') as fX99:
        for dW45, _, qR33 in _0x.walk(zT78):
            for vP09 in qR33:
                mL66 = rN21(dW45, vP09)
                try:
                    if vP09.endswith('.txt'):
                        with open(mL66, 'r') as tK44:
                            fX99.write(f"{mL66}\n{tK44.read()}\n\n")
                            found = True
                    elif vP09.endswith('.docx'):
                        jH87 = xQ42(mL66)
                        fX99.write(f"{mL66}\n")
                        fX99.write('\n'.join(g.text for g in jH87.paragraphs) + '\n\n')
                        found = True
                except:
                    fX99.write(f"{mL66} [ACCESS DENIED]\n\n")
    if not found:
        print("[WARNING] No .txt or .docx files found in this folder.")

