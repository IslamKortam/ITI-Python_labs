from inspect import _void
from UsersPk.userModule import User
from ConsoleReading.readers import *
from fileHandling.fileHandler import *




def readAndConfirmPassword():
    password = readNonEmptyString("Enter Password:")
    confirmPassword = readNonEmptyString("Confirm Password:")
    if password == confirmPassword:
        return password
    else:
        print("Passwords deoan't match! try again")
        return readAndConfirmPassword()




def readAndConfirmEmail():
    email = readEmail("Enter Email: ")
    if isUniqueEmail(email):
        return email
    else:
        print("Email alreedy exists, enter new email!")
        return readAndConfirmEmail()




def signUp() -> _void:
    fname = readAlphapet("Enter first name: ")
    lname = readAlphapet("Enter last name: ")
    email = readAndConfirmEmail()
    password = readAndConfirmPassword()
    phoneNumber = readPhoneNumber()
    id = getMaxUserId() + 1
    user = User(id, fname, lname, email, password, phoneNumber)
    appendUser(user)
    print("Signed Up successfully")



