#global vars and imports
import base
global curr_db
import pickle
buffer = None

# functionalities
def createDatabase(db):
    base.createDirectory(db)
    print("database created")
    
def useDatabase(db):
    global curr_db
    if base.checkDirectory(db):
        curr_db = db
        print("database changed succesfully")
    else:
        curr_db = None
        print("database doesn't exist")
    
def createTable(tablename,attr,key=None):
    # assuming primary key vars are given
    if curr_db == None:
        print("no database selected")
    else:
        if key == None:
            key = attr[0]
        base.createFile(f"{curr_db}/{tablename}_set")
        base.createFile(f"{curr_db}/{tablename}")
        info = [key, attr, len(attr)]
        base.writeFile(info,f"{curr_db}/{tablename}_set")
        print("table overwritten/created")
        
def describeTable(tablename):
    if base.checkFile(f"{curr_db}/{tablename}_set") and curr_db != None:
        base.showData([base.readFile(f"{curr_db}/{tablename}_set")],["key","attributes","cols"])
    else:
        print("no table found in the current database")    
    input("press any key to continue...")
    



# createDatabase("students")
# useDatabase("students")
# createTable("attendance",["sno","regno","name","status"],"regno")
# describeTable("attendance")


