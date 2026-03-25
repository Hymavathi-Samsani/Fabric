#Getting file information from given path

path='abfss://hymaa_practice_2026@onelake.dfs.fabric.microsoft.com/lh_raw.Lakehouse/Files/'

ls=mssparkutils.fs.ls(path)

for i in ls:
    print(i.name,i.path,i.size,i.isDir,i.isFile,i.modifyTime)