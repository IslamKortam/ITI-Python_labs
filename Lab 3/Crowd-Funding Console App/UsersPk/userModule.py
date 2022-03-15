from json import JSONEncoder
import json



class UserEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, User):
            return object.__dict__
        else:
            raise Exception("Not a User!")

def as_User(userDct):
    return User(userDct["id"], userDct["fname"], userDct["lname"], userDct["email"], userDct["password"], userDct["mobilePhone"])



class User:
    @classmethod
    def fromJSONtoUser(cls, jssonString):
        return json.loads(jssonString ,object_hook=as_User)

    def __init__(self, id, fname, lname, email, password, mobliePhone) -> None:
        self.id = id
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.mobilePhone = mobliePhone

    def __str__(self) -> str:
        return str(self.id) + ":" + self.fname + ":" + self.email + ":" + self.mobilePhone

    def toJson(self):

        return UserEncoder().encode(self)




""" s1 = User(1, "islam", "kortam", "imkortam@gmail.com", "pswword", "01016090464")
s2 = User.fromJSONtoUser(s1.toJson())

s1.fname = "rofida"

print(s1)
print(s2) """

""" 
s1 = User(1, "Islam", "Kortam", "imkortam@gmail.com", "password", "01016090464")

s = UserEncoder().encode(s1)

s5 = json.loads(s,object_hook=as_User)

print(f"Object = {s}")
print(s1)
print(s5) """


