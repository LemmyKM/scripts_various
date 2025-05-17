# replace folder name or change text in file
from pathlib import Path
import os


#print(os.getcwd())
#path = '/Volumes/Expansion1/'

# filereplace("file where to look in", "text to look for", "text to replace with")
path = Path.home() /'film'
list =  os.listdir(path)
if '[YTS.mx]' in list:
    os.remove('YTS.MX')
#    if '[YTS.mx]' in a:
        
