import glob,os,json

def getdata(path):
    data = []
    for filename in glob.iglob(path + '**/**', recursive=True):
        data.append(filename)
    return data

def createjsonlog(path):   
    """Creates a json file with an array that contains the names of all the content in the given path."""
    with open("file-log.json", "w") as write_file:
        json.dump(getdata(path), write_file)


def checkjsonlog(path):
    """Compares the names of the files and folders in the path to the ones in the json log."""
    with open("file-log.json", "r") as read_file:
        jsondata = json.load(read_file)
    localdata = getdata(path)
    return True if localdata == jsondata else False


