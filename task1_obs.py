import os
from docx import Document as xQ42

k9p3 = r"C:\Users\omara\OneDrive\Desktop\coursework-cyber fund\file.log"
zT78 = input("Location to examine: ").strip()

def rN21(a1, b2):
    return os.path.join(a1, b2)

with open(k9p3, 'w') as fX99:
    for dW45, _, qR33 in os.walk(zT78):
        for vP09 in qR33:
            mL66 = rN21(dW45, vP09)
            try:
                if vP09.endswith('.txt'):
                    with open(mL66, 'r') as tK44:
                        fX99.write(f"{mL66}\n{tK44.read()}\n\n")
                elif vP09.endswith('.docx'):
                    jH87 = xQ42(mL66)
                    fX99.write(f"{mL66}\n")
                    fX99.write('\n'.join(g.text for g in jH87.paragraphs) + '\n\n')
            except:
                fX99.write(f"{mL66} [ACCESS DENIED]\n\n")