import glob,os,json


def createjsonlog(path):   
    """Creates a json file with an array that contains the names of all the content in the given path."""
    data = []
    for filename in glob.iglob(path + '**/**', recursive=True):
        data.append(filename)
    with open("file-log.json", "w") as write_file:
        json.dump(data, write_file)


