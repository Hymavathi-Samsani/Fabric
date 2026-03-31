#Delete the files greater than 3 days
path='abfss://hymaa_practice_2026@onelake.dfs.fabric.microsoft.com/lh_raw.Lakehouse/Files/'

#import datetime and timedelta modules
from datetime import datetime
from datetime import timedelta
import re

#Get last 3 days
last3days=[]
today=datetime.now()

for i in range(3):
    last3days.append((today-timedelta(days=i+1)).strftime('%d%m%Y'))
    
#Get all files info
ls=notebookutils.fs.ls(path+'Test/Databricks/')

print(last3days)

#Loop through files list
for file in ls:
       dt=re.search(r'\d{2}\d{2}\d{4}',file.name)
       if file.isFile and (dt != None and dt.group() not in last3days): #Check whether file more than 3 days
           print(file.name)
           notebookutils.fs.rm(path+'Test/Databricks/'+file.name) #Copy file from databricks directory to Outbound directory
           

print('Execution completed')
