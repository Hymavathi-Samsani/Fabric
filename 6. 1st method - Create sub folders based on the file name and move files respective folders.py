#1st method - Create sub folders based on the file name and move files respective folders
import re

#Check if folder exist or not and create
if not notebookutils.fs.exists(path+'Outbound'):
   notebookutils.fs.mkdirs(path+'Outbound')

ls=notebookutils.fs.ls(path+'Databricks/')

#Loop through all files
for file in ls :
    if file.isFile: #Check file or not
        dirs=file.name.split('_') #Split file name with underscore delimeter
        path_str='' #save path temporary string

        for i in dirs: # Loop through all splitted strings
            if re.search(r'\d{2}\d{2}\d{4}',i) == None: # Check if string is not date and not directory already exist
                path_str=path_str+i+'/' # update path string

        if not notebookutils.fs.exists(path+'Outbound/'+path_str+i): # Create directory if not available
            notebookutils.fs.mkdirs(path+'Outbound/'+path_str)

        notebookutils.fs.cp(path+'Databricks/'+file.name,path+'Outbound/'+path_str+file.name) # Copy files in respective folders

print('Execution completed')
