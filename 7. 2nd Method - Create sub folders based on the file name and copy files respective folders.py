#2nd Method - Create sub folders based on the file name and copy files respective folders
import re

#Check if folder exist or not and create
if not notebookutils.fs.exists(path+'Outbound'):
   notebookutils.fs.mkdirs(path+'Outbound')

ls=notebookutils.fs.ls(path+'Databricks/')

#Loop through all files
for file in ls :
    if file.isFile: #Check file or not
       i=re.search(r'\d{2}\d{2}\d{4}',file.name) #Get date from file name
       if i != None: #If date is found
          path_str=file.name.split(i.group())[0].replace('_','/') #Replace delimeter with slash
          notebookutils.fs.mkdirs(path+'Outbound/'+path_str) # Create folders
          notebookutils.fs.cp(path+'Databricks/'+file.name,path+'Outbound/'+path_str+file.name) # Copy files in respective folders

   
print('Execution completed')
