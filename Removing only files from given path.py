#Removing only files from given path

path='abfss://hymaa_practice_2026@onelake.dfs.fabric.microsoft.com/lh_raw.Lakehouse/Files/'

ls=mssparkutils.fs.ls(path+'Databricks/')
for i in ls:
    if i.isFile:
        mssparkutils.fs.rm(i.path,True)