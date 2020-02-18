import os
import sys

def replace(folder_path, old, new):
    for path, subdirs, files in os.walk(folder_path):
        for name in files:
            print(name)
            if(old.lower() in name.lower()):
                file_path = os.path.join(path,name)
                new_name = os.path.join(path,name.lower().replace(old,new))
                os.rename(file_path, new_name)

path = input('Qual o path para o replce?')
old = input('Qual o nome antigo?')
new = input('Qual o nome novo?')

replace(path, old, new)
