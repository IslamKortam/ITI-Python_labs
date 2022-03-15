from json import JSONEncoder
import json
import re
from datetime import datetime

class ProjectEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Project):
            return object.__dict__
        else:
            raise Exception("Not a Project!")

def as_Project(projectDct):
    startDate = projectDct["startDate"].split(" ")[0].split("-")
    endDate = projectDct["endDate"].split(" ")[0].split("-")
    startDate = datetime(int(startDate[0]), int(startDate[1]), int(startDate[2]), 0, 0, 0)
    endDate = datetime(int(endDate[0]), int(endDate[1]), int(endDate[2]), 0, 0, 0)
    return Project(projectDct["id"], projectDct["title"], projectDct["details"], projectDct["target"], startDate, endDate, projectDct["ownerID"])



class Project:
    @classmethod
    def fromJSONtoProject(cls, jssonString):
        return json.loads(jssonString ,object_hook=as_Project)

    def __init__(self, id, title, details, target, startDate, endDate, ownerID) -> None:
        self.id = id
        self.title = title
        self.details = details
        self.target = target
        self.startDate = startDate
        self.endDate = endDate
        self.ownerID = ownerID
    
    def __str__(self) -> str:
        return str(self.id) + ":" + self.title + ":" + self.details + ":" + str(self.target) + ":" + str(self.startDate) + ":" + str(self.endDate)  + ":" + str(self.ownerID)

    def toJson(self):
        p = Project(self.id, self.title, self.details, self.target, str(self.startDate), str(self.endDate), self.ownerID)
        return ProjectEncoder().encode(p)



