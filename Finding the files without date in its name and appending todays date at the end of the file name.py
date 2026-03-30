#Finding the files without date in its name and appending todays date at the end of the file name 

from datetime import datetime
import re 

path='abfss://hymaa_practice_2026@onelake.dfs.fabric.microsoft.com/lh_raw.Lakehouse/Files/'

today=datetime.today()
req_format=today.strftime('%d%m%Y')
print(req_format)

ls=mssparkutils.fs.ls(path+'Databricks/')
for i in ls:
    match_str=re.search(r'\d{2}\d{2}\d{4}',i.name)
    if match_str==None:
        iname=i.name.split('.')[0]+'_'+req_format+'.'+i.name.split('.')[1]
        mssparkutils.fs.mv(path+'Databricks/'+i.name,path+'Databricks/'+iname,True,True)
    else:
       print(i.name,match_str.group())