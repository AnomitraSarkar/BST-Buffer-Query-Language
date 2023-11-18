import server
import base
import os
r = None
ls = []
global tablename

class Node:
    def __init__(self, prkey, lsdata):
        self.val = prkey
        self.left = None
        self.right = None
        self.lsdata = lsdata

def insert(root, key, lsdata):
    if root is None:
        return Node(key,lsdata)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key,lsdata)
        else:
            root.left = insert(root.left, key,lsdata)
    return root
 
def search(root, key):
    if root is None or root.val == key:
        return root
 
    if root.val < key:
        return search(root.right, key)
 
    return search(root.left, key)


def deleteNode(root, k):
    if root is None:
        return root
 
    if root.val > k:
        root.left = deleteNode(root.left, k)
        return root
    elif root.val < k:
        root.right = deleteNode(root.right, k)
        return root
 
    if root.left is None:
        temp = root.right
        del root
        return temp
    elif root.right is None:
        temp = root.left
        del root
        return temp
 
    else:
 
        succParent = root
 
        succ = root.right
        while succ.left is not None:
            succParent = succ
            succ = succ.left
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right
 
        root.val = succ.val
 
        del succ
        return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, root.lsdata, end=" ")
        inorder(root.right)
        


def load(file):
    global tablename
    tablename = file
    global r
    if ".dat" not in file:
        file += ".dat"
    file = f"{server.curr_db}/{file}"
    if base.checkFile(file):
        lsd = base.readFile(file)
        if lsd != False:
            for i in lsd:
                r = insert(r,i[0],i[1])
        else:
            r = None
        print("buffer loaded")
def inorder_list_addition(root):
    if root:
        inorder_list_addition(root.left)
        ls.append([root.val, root.lsdata])
        inorder_list_addition(root.right)

def save(file):
    global ls
    ls = []
    inorder_list_addition(r)
    base.writeFile(ls,f"{server.curr_db}/{file}")
    print("buffer saved")
    
def insertion(datals):
    global r
    header = base.readFile(f"{server.curr_db}/{tablename}_set")
    datakey = header[0]
    k = header[1].index(datakey)
    insertkeydata = datals[k]
    r = insert(r,insertkeydata,datals)
    print("inserted")
    
def deletion(key):
    global r
    r = deleteNode(r,key)
    print("deleted key", key)
    
def searching(key):
    global r
    ro = search(r,key)
    if ro is None:
        print(key, "not found")
    else:
        print(key,"found")
    
def showBufferData():
    print("\n")
    global ls
    ls = []
    inorder_list_addition(r)
    header = base.readFile(f"{server.curr_db}/{tablename}_set")[1]
    proc = []
    for i in ls:
        proc.append(i[1])
    base.showData(proc,header)
    

    
def parseAndAnalyse_File(filename):
    os.system("cls")
    f = open(filename,"r")
    lines = f.readlines()
    for i in range(len(lines)):
        print(i+1, end= ">")
        parseAndAnalyse_Snippet(lines[i])
    

def parseAndAnalyse_Snippet(code):
    code = code.lower()
    if "create" in code and "table" not in code:
        dbname = code.split()[-1]
        server.createDatabase(dbname)
    elif "create" in code and "table" in code:
        code = code.split("=")
        tbname = code[0].split()[-1]
        cols = code[1].split()
        key = code[-1].split()[-1]
        server.createTable(tbname,cols,key)
    elif "use" in code:
        dbname = code.split()[-1]
        server.useDatabase(dbname)
    elif "load" in code:
        tbname = code.split()[-1]
        load(tbname)
    elif "save" in code:
        tbname = code.split()[-1]
        save(tbname)
    elif "show" in code:
        showBufferData()
    elif "desc" in code:
        tbname = code.split()[-1]
        server.describeTable(tbname)
    elif "insert" in code:
        code = code.split(" ")
        code.remove("insert")
        insertion(code)
    elif "delete" in code:
        key = code.split()[-1]
        deletion(key)
    elif "search" in code:
        key = code.split()[-1]
        searching(key)
        
parseAndAnalyse_File("code.bbql")