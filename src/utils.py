from time import strftime
from os.path import abspath
from os.path import split as SplitPath
from os.path import join as JoinPath

def getTime():
    return strftime("%S:%M:%H")

def getAbsPath():
    return SplitPath(abspath("__file__"))[0]

def createFilename(file, formatFile):
    time = getTime().replace(":", "-")
    return JoinPath(getAbsPath(), "output", file + time + formatFile)