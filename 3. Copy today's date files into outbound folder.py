#Copy today's date files into outbound folder

#Import datetime module
from datetime import datetime 

#Get today's date in ddmmyyyy format
dt = datetime.today()
today=dt.strftime('%d%m%Y')

#Check if folder exist or not and create
if not notebookutils.fs.exists(path+'Outbound'):
   notebookutils.fs.mkdirs(path+'Outbound')

#Get all files list from the path
ls=notebookutils.fs.ls(path+'Databricks/')

#Loops through files list
for file in ls:
    if file.isFile and today in file.name: #Check whether file exist in folder or not
        notebookutils.fs.cp(path+'Databricks/'+file.name,path+'Outbound/',False)

print('Execution completed')
