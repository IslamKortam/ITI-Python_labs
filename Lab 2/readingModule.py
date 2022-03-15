from math import degrees
from re import X


def readInt(alertMsg):
    x = "string"
    while not x.isnumeric() :
        x = input(alertMsg)
    return int(x)


def readNonEmptyString(alertMsg) : 
    x = ""
    while not x : 
        x = input(alertMsg)
    return x


def readOneAlphapet(alertMsg) :
    x = ""
    while not (len(x) == 1 and x.isalpha()) :
        x = input(alertMsg)
    print(f"Enterd: {x}")
    return x