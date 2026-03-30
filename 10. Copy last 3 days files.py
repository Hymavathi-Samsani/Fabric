#Copy last 3 days files only
path='abfss://hymaa_practice_2026@onelake.dfs.fabric.microsoft.com/lh_raw.Lakehouse/Files/'

#import datetime and timedelta modules
from datetime import datetime
from datetime import timedelta

#Get last 3 days
last3days=[]
today=datetime.now()

for i in range(3):
    last3days.append((today-timedelta(days=i+1)).strftime('%d%m%Y'))
    
#Get all files info
ls=notebookutils.fs.ls(path+'Databricks/')

if not notebookutils.fs.exists(path+'Last 3 Days/'):
    notebookutils.fs.mkdirs(path+'Last 3 Days/')

#Loop through files list
for file in ls:
    for i in last3days:#Loop through last 3 days
       if file.isFile and i in file.name: #Check whether date exists in file name
           notebookutils.fs.cp(path+'Databricks/'+file.name,path+'Last 3 Days/'+file.name) #Copy file from databricks directory to Outbound directory


print('Execution completed')
