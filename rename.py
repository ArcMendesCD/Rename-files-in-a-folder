import os

directory = 'item'

for filename in os.listdir(directory):

    newname = filename.lower().replace("-","_").replace(" ","")

    print(filename + ' -> '+ newname) 

    os.rename(directory+'/'+filename,  newname)