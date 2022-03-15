from fileHandling.fileHandler import *
from fileHandling.fileHandler import *
from ConsoleReading.readers import *

def insertProject(currentUser):
    project = readProjectData(None, currentUser.id)
    if project != None:
        appendProject(project)
        print("Project created successfuly with id: " + str(project.id))
    else:
        return


def readProjectData(projectId, projectOwnerId):
    if projectId == None:
        projectId = getMaxProjectID() + 1
    title = readNonEmptyString("Enter Project Title: ")
    details = input("Enter Project details: ")
    target = readPositiveInteger("Enter Target(Positive Integer): ")
    startDate = readDate("Enter Start Date: ")
    endDate = readEndDate(startDate)
    project = Project(projectId, title, details, target, startDate, endDate, projectOwnerId)
    return project



