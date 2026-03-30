#Copy only todays data files into outbound folder
from datetime import datetime 

#Get today's date in ddmmyyyy format
dt = datetime.today()
today=dt.strftime('%d%m%Y')

#Check if folder exist or not and create
if not notebookutils.fs.exists(path+'Outbound'):
   notebookutils.fs.mkdirs(path+'Outbound')

#Get all files list from the path
ls=notebookutils.fs.ls(path+'Databricks/')

for file in ls:
    print(file.name, today in file.name)
    if file.isFile and today in file.name:
        notebookutils.fs.cp(path+'Databricks/'+file.name,path+'Outbound/',False)

print('Execution completed')