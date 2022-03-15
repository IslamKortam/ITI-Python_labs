import email
from readingModule import readNonEmptyString


from readingModule import *
import re

def isValidEmail(email) -> bool:
    emailRegex = "^[a-zA-Z]([a-zA-Z0-9]|\.|_)*@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$"
    x = re.search(emailRegex, email)
    #print(x)
    if x : 
        return True
    else:
        return False



def readName():
    name = "1232"
    while not name.isalpha():
        name = readNonEmptyString("Enter a non Empty Name: ")
    return name
    
def readEmail():
    email = ""
    while True:
        email = readNonEmptyString("Enter an email: ")
        if isValidEmail(email) :
            break
    return email


def readData():
    name = readName()
    email = readEmail()
    print(f"Name: {name}, Email : {email}")



readData()