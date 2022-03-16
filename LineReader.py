def readFromFile(url):
    infile = open(url, 'r')
    line = infile.readline()
    return line
