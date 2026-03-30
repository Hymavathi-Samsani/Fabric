#Removing only files from given path

path='abfss://hymaa_practice_2026@onelake.dfs.fabric.microsoft.com/lh_raw.Lakehouse/Files/'

ls=mssparkutils.fs.ls(path+'Databricks/') # Get all files list

for i in ls: # Loop through files
    if i.isFile: # Check whether file or not
        mssparkutils.fs.rm(i.path,True) # Remove from the path
