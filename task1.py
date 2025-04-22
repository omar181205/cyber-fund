import os
from docx import Document

log_path = r"C:\Users\omara\OneDrive\Desktop\coursework-cyber fund\file.log"
directory = input("Directory to scan: ").strip()

with open(log_path, 'w') as f:
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            try:
                if file.endswith('.txt'):
                    with open(path, 'r') as txt:
                        f.write(f"{path}\n{txt.read()}\n\n")
                elif file.endswith('.docx'):
                    doc = Document(path)
                    f.write(f"{path}\n")
                    f.write('\n'.join(p.text for p in doc.paragraphs) + '\n\n')
            except:
                f.write(f"{path} [READ ERROR]\n\n")