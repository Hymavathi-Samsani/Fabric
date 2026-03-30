# Create date folder based on the file name and copy files into respective folders
path='abfss://hymaa_practice_2026@onelake.dfs.fabric.microsoft.com/lh_raw.Lakehouse/Files/'

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
          notebookutils.fs.mkdirs(path+'Outbound/'+i.group()) # Create folder
          notebookutils.fs.cp(path+'Databricks/'+file.name,path+'Outbound/'+i.group()+'/'+file.name) # Copy files in respective folders

   
print('Execution completed')
