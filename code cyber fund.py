import os

def collect_files(directory):
    for root, dirs ,files in os.walk(directory):
        for file in files:
            if file.endswith((".txt", ".jpg", ".docx")):
                print(os.path.join(root, file))

try:
    path = input("spectify the path to use: ")
    collect_files(path)
except FileNotFoundError:
    print("file does not exist")    