import re

emailRegex = "^[a-zA-Z]([a-zA-Z0-9]|\.|_)*@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$"

def validateEmail(email):
    if isinstance(email, str):
        x = re.search(emailRegex, email)
        if x:
            return True
        else:
            return False
    else:
        raise Exception("email must be a string")