#Copy yesterday's files only
path='abfss://hymaa_practice_2026@onelake.dfs.fabric.microsoft.com/lh_raw.Lakehouse/Files/'

#import datetime and timedelta modules
from datetime import datetime
from datetime import timedelta

#Get yestersday
today=datetime.now()
previous_day=today-timedelta(days=1)

#format date
prev_date_formatted=previous_day.strftime('%d%m%Y')

#Get all files info
ls=notebookutils.fs.ls(path+'Databricks/')

#Loop through files list
for file in ls:
    if file.isFile and prev_date_formatted in file.name: #Check whether previous date exists in file name
        notebookutils.fs.cp(path+'Databricks/'+file.name,path+'Outbound/'+file.name) #Copy file from databricks directory to Outbound directory

print('Execution completed')
