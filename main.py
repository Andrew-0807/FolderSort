import os
import shutil

Dpath = "C:/Users/andre/Downloads" 
os.chdir(Dpath)
def sort(file, extenxion):
    #
    # !creates folder for file type
    folder = f"type-{extenxion}"
    # print (folder)
    try:
        os.mkdir(folder)
    except:
        pass
    
    try:
        shutil.move(Dpath+"/"+file, Dpath+"/"+folder)
    except:
        pass
 
files = os.listdir("C:/Users/andre/Downloads")
for file in files:
    if file.startswith("type"): 
        continue
    extension = file.split(".")[-1]
    if os.path.isdir(extension):
        extension = "folder"
    sort(file, extension)