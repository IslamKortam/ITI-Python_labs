from ConsoleReading.readers import *
from fileHandling.fileHandler import getProjects

def getProjectID(projectList, operationType):
    #This user's project list
    print(f"Choose a project id to {operationType}: ")
    for project in projectList:
        print(project)
    id = readIntorCancel("Choose a project: ")
    if id == None:
        #User choosed cancel
        return None
    projectIDs = [p.id for p in projectList ]
    if id in projectIDs:
        return  id
    else:
        return getProjectID(projectList, operationType)

def getProjectsOfUser(user, allPorjects):
    projectList = [project for project in allPorjects if project.ownerID == user.id]
    return  projectList