import os, sys, json, shutil


current_dir = os.getcwd().split('/')
current_dir = current_dir.pop()
module_dir = current_dir.split('-')
vendor_dir = '/var/www/html/stores/casa-made-bisws/vendor/BIS2BIS/'
formated_module_dir = ''

for name in module_dir:
   formated_module_dir += name.capitalize()
    
final_module_dir = vendor_dir+formated_module_dir

if(not os.path.exists(final_module_dir)):
    os.mkdir(final_module_dir, 0777)

if(os.path.exists(final_module_dir)):
    os.system('cp ' + os.getcwd() +'/* '+ final_module_dir +'/ -r')
    print('modulo '+formated_module_dir+' foi atualizado')
else:
    print('erro ao criar o folder do modulo')
