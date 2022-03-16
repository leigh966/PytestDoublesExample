import os

def readFromFile(url):
    infile = open(url, 'r')
    if not os.path.exists(url):
        raise Exception("file does not exist")
    line = infile.readline()
    return line
