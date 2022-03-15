from ConsoleReading.readers import *
from fileHandling.fileHandler import *
def login():
    email = readEmail("Enter your email: ")
    password = readNonEmptyString("Enter password: ")
    user = validateLoginAttempt(email, password)
    return user


