import tabulate
import time
import pickle
import os
    
def writeFile(data,path) -> bool:
    try:
        if ".dat" not in path:
            path += ".dat"
        f = open(path,"wb")
        pickle.dump(data, f)
        f.close()
        return True
    except:
        return False

def readFile(path):   
    try:
        if ".dat" not in path:
            path += ".dat"
        f = open(path,"rb")
        record = pickle.load(f)
        return record
    except Exception as e:
        return False 

def createDirectory(dirname)->bool:
    try:
        os.system(f"mkdir {dirname}")
        return True
    except:
        return False

def checkDirectory(dirname,relative='./')->bool:
    ls = os.listdir(relative)
    if dirname in ls:
        return True
    else:
        return False

def removeDirectory(dirname):
    x = os.system(f"rmdir {dirname}")
    if x == 0:
        return True
    else:
        return False

def createFile(path)->bool:
    if ".dat" not in path:
            path += ".dat"
    try:
        os.system(f"type nul > {path}")
        return True
    except:
        return False

def checkFile(rel_path) -> bool:
    pathls = rel_path.split("/")
    path = pathls[1]
    relative = pathls[0]
    if ".dat" not in path:
        path += ".dat"
    ls = os.listdir(relative)
    if path in ls:
        return True
    else:
        return False

def removeFile(path)->bool:
    if ".dat" not in path:
            path += ".dat"
    try:
        os.remove(path)
        return True
    except:
        return False

def showData(data, header):
    # load header and file data
    print(tabulate.tabulate(data,header,tablefmt="fancy_grid"))

