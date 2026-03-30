#Getting file information from given path

path='abfss://hymaa_practice_2026@onelake.dfs.fabric.microsoft.com/lh_raw.Lakehouse/Files/'

ls=mssparkutils.fs.ls(path) #Get files details from the path

for i in ls: # Loop through files list array
    print(i.name,i.path,i.size,i.isDir,i.isFile,i.modifyTime) # Print file info
