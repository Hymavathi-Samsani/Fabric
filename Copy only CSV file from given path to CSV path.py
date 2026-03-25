#Copy only CSV file from given path to CSV path

path='abfss://hymaa_practice_2026@onelake.dfs.fabric.microsoft.com/lh_raw.Lakehouse/Files/'

mssparkutils.fs.mkdirs(path+'CSV')
ls=mssparkutils.fs.ls(path)
for i in ls:
    if i.isFile and i.name.endswith('.csv'):
        mssparkutils.fs.cp(i.path,path+'CSV/')