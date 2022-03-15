
import re
from datetime import datetime

emailRegex = "^[a-zA-Z]([a-zA-Z0-9]|\.|_)*@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$"
phoneNumberRegex = "^01([0-2]|5)[0-9]{8}$"

dateRegix = "^2[0-9]{3}\-(0[0-9])"

def readNonEmptyString(alertMsg = "") -> str:
    if not isinstance(alertMsg, str):
        raise TypeError(f"Expected string, found {type(alertMsg)}")
    
    string = input(alertMsg)
    if string != "":
        return string
    else:
        return readNonEmptyString(alertMsg)


def readAlphapet(alertMsg = "") -> str:
    if not isinstance(alertMsg, str):
        raise TypeError(f"Expected string, found {type(alertMsg)}")
    
    string = readNonEmptyString(alertMsg)
    if string.isalpha() :
        return string
    else:
        return readAlphapet(alertMsg)

def readInt(alertMsg = "") -> int:
    if not isinstance(alertMsg, str):
        raise TypeError(f"Expected string, found {type(alertMsg)}")

    string = readNonEmptyString(alertMsg)
    if string.isnumeric() :
        return int(string)
    else:
        return readInt(alertMsg)


def readIntorCancel(alertMsg="") -> int:
    if not isinstance(alertMsg, str):
        raise TypeError(f"Expected string, found {type(alertMsg)}")

    string = readNonEmptyString(alertMsg)
    if string.isnumeric():
        return int(string)
    elif string.lower() == "cancel":
        return None
    else:
        return readIntorCancel(alertMsg)


def readPhoneNumber(alertMsg = "Enter phone Number: ") -> str:
    if not isinstance(alertMsg, str):
        raise TypeError(f"Expected string, found {type(alertMsg)}")
    
    phoneNumber = readNonEmptyString(f"Enter phone number in format:'01xxxxxxxxx': ")
    x = re.search(phoneNumberRegex, phoneNumber)
    if x : 
        return phoneNumber
    else:
        print("Wrong phoneNumber")
        return readPhoneNumber(alertMsg)



def readEmail(alertMsg = "") -> str:
    if not isinstance(alertMsg, str):
        raise TypeError(f"Expected string, found {type(alertMsg)}")
    
    email = readNonEmptyString(alertMsg)
    x = re.search(emailRegex, email)
    #print(x)
    if x : 
        return email
    else:
        print("wrong email! try again")
        return readEmail(alertMsg)

def readPositiveInteger(alertMsg = ""):
    if not isinstance(alertMsg, str):
        raise TypeError(f"Expected string, found {type(alertMsg)}")

    x = readInt(alertMsg)
    if x > 0:
        return x
    else:
        print("Not a positive Integer! try again")
        return  readPositiveInteger(alertMsg)


def readDate(alertMsg = ""):
    if not isinstance(alertMsg, str):
        raise TypeError(f"Expected string, found {type(alertMsg)}")
    print("Date format is: yyyy-mm-dd")
    d = readNonEmptyString(alertMsg)
    d = d.strip(" \n")
    d = d.split("-")
    try:
        d = datetime(int(d[0]), int(d[1]), int(d[2]), 0, 0, 0)
        return d
    except:
        print("Wrong Date format! try again")
        return  readDate(alertMsg)

def readEndDate(startDate):
    endDate = readDate(f"Enter End date (not before + {startDate}): ")
    if endDate >= startDate:
        return endDate
    else:
        print("Error, End date cannot be before start date! try againg")
        return  readEndDate(startDate)
