#Copy CSV files from given path to CSV path

path='abfss://hymaa_practice_2026@onelake.dfs.fabric.microsoft.com/lh_raw.Lakehouse/Files/'

mssparkutils.fs.mkdirs(path+'CSV') # Create directory with name CSV 

ls=mssparkutils.fs.ls(path) # Get all files info

for i in ls: #Loop through all files
    if i.isFile and i.name.endswith('.csv'): #Check whether file is csv file or not
        mssparkutils.fs.cp(i.path,path+'CSV/') # Copy csv file to CSV folder
