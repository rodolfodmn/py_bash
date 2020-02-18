import contents
import os, sys, json



def write_files_folders(root, tree):
    if root != '':
        if item[1]['type'] == "dir":
            print("./"+moduleDir+"/"+root+"/"+item[0])
            os.mkdir("./"+moduleDir+"/"+root+"/"+item[0])
            if item[1]["sub"] :
                write_files_folders(item[0], item[1]["sub"])
                print(item[1]["sub"])
        else:
            f = open("./"+moduleDir+"/"+root+"/"+item[0], "x")
            f.write('arquivo teste')
            f.close()
    else:
        if item[1]['type'] == "dir":
            os.mkdir("./"+moduleDir+"/"+item[0])
            if item[1]["sub"] :
                write_files_folders(item[0], item[1]["sub"])
                print(item[1]["sub"])
        else:
            f = open("./"+moduleDir+"/"+item[0], "x")
            f.write('arquivo teste')
            f.close()
    

moduleDir = input("informe o nome do seu módulo:")

json_folders = json.loads(contents.folders_json)

os.mkdir(moduleDir)

for item in json_folders.items() : 
    write_files_folders('', item)



# for folder in contents.folders:
#     if folder.find("/") != -1:
#         os.mkdir("./"+moduleDir+"/"+folder)
#     else:
#         f = open("./"+moduleDir+"/"+folder, "x")
#         f.write('arquivo teste')
#         f.close()

# teste = f"""funk maroto
#     {moduleDir}
#     aaa muleke"""
