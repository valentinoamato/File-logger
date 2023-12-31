import glob,os,json
filepath = os.path.dirname(os.path.realpath(__file__))
run = True


def getdata(path):   
    """Returns a list with the names of all folders and files in a path"""
    data = []
    for filename in glob.iglob(path + '**/**', recursive=True):
        data.append(filename.replace(path+"/",""))
    if "" in data:
        data.remove("")
    return data

def createjsonlog(path):   
    """Creates a json file with an array that contains the names of all the content in the given path."""
    data = getdata(path)
    if data:
        with open(f"{path}/file-log.json", "w") as write_file:
            json.dump(getdata(path), write_file)
        print("\nLog created with success!")
    else:
        print("\nInvalid path.")

def changes(jsondata,localdata):
    """Prints the differences between the json data and the local data."""
    for i in jsondata.copy():    #Removes the shared elements between the two lists, leaving the 'additions' in localdata and the 'deletions' in jsondata.

        if i in localdata:
            jsondata.remove(i)
            localdata.remove(i)

    print("\nAdditions:\n")
    for i in localdata:
        print(f"    - {i}")

    print("\nDeletions:\n")
    for i in jsondata:
        print(f"    - {i}")

def checkjsonlog(path):
    """Compares the names of the files and folders in the path to the ones in the json log."""
    try:
        with open(f"{path}/file-log.json", "r") as read_file:
            jsondata = json.load(read_file)
        localdata = getdata(path)
        if localdata == jsondata:
            print("\n\nThe data in the log and in the path match.\n\n")
        else:
            print("\n\nThe data in the log and in the path doesn't match.")
            print("The differences are the following.")
            changes(jsondata,localdata)

    except FileNotFoundError:
        print("\nInvalid path.")



print("Welcome to File-logger!! ")
while run:
    print("\nChoose an option:")
    print("1-Create log.")
    print("2-Check log.")
    print("3-Exit.")
    answer = input("(1-2-3): ")
    if answer not in ["1","2","3"]:
        print("\nInvalid input.")
        continue
    if answer == "3":
        break
    path = input("\nEnter path or enter '.': ")
    if path == ".":
        path = filepath
    if answer == "1":
        createjsonlog(path)
    elif answer == "2":
        checkjsonlog(path)

print("\nThanks for using the program!!")
print("More info at: https://github.com/valentinoamato/File-logger.")

