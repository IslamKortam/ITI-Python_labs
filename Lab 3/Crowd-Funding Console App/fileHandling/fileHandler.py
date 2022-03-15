from operator import truediv
from UsersPk.userModule import *
from projectsPK.ProjectModule import *
import os


projectPath = os.path.dirname(os.path.realpath('__file__'))

usersFilePath =    projectPath + "/Data/users.txt"
projectsFilePath = projectPath + "/Data/projects.txt"

def isUniqueEmail(email):
    try:
        userseFile = open(usersFilePath, 'r')
    except Exception as e:
        print(e)
        #raise Exception("Users file isn't accessible or not found")
    else:
        line = userseFile.readline()
        while line != "\n" and line != "":
            user = User.fromJSONtoUser(line.strip("\n"))
            if user.email == email:
                userseFile.close()
                return False #not unique
            line = userseFile.readline()
        userseFile.close()
        return True #unique


def validateLoginAttempt(email, password):
    try:
        userseFile = open(usersFilePath, 'r')
    except Exception as e:
        print(e)
        #raise Exception("Users file isn't accessible or not found")
    else:
        line = userseFile.readline()
        while line != "\n" and line != "":
            user = User.fromJSONtoUser(line.strip("\n"))
            if user.email == email and user.password == password:
                userseFile.close()
                return user #User Found
            line = userseFile.readline()
        userseFile.close()
        return None  #User Not Found


def appendUser(user):
    try:
        userseFile = open(usersFilePath, 'a')
    except Exception as e:
        print(e)
        #raise Exception("Users file isn't accessible or not found")
    else:
        userseFile.write(user.toJson())
        userseFile.write("\n")

def getMaxUserId():
    try:
        userseFile = open(usersFilePath, 'r')
    except Exception as e:
        print(e)
        raise Exception("Users file isn't accessible or not found")
    else:
        usersLines = userseFile.readlines()
        #print(usersLines)
        if len(usersLines) == 0:
            return  -1
        maxId = User.fromJSONtoUser(usersLines.pop().strip("\n") ).id
        return  maxId

def appendProject(project):
    print(project)
    print(type(project))
    try:
        projectFile = open(projectsFilePath, 'a')
    except Exception as e:
        print(e)
        #raise Exception("Users file isn't accessible or not found")
    else:
        projectFile.write(project.toJson())
        projectFile.write("\n")


def getProjects():
    try:
        projectFile = open(projectsFilePath, 'r')
    except Exception as e:
        print(e)
        #raise Exception("Users file isn't accessible or not found")
    else:
        projectsLines = projectFile.readlines()
        projectList = []
        for project in projectsLines:
            projectList.append(Project.fromJSONtoProject(project.strip("\n")))
        projectFile.close()
        return  projectList

def setProjects(projectsList):
    try:
        projectFile = open(projectsFilePath, 'w')
    except Exception as e:
        print(e)
        #raise Exception("Users file isn't accessible or not found")
    else:
        for project in projectsList:
            projectString = Project.toJson(project)
            projectFile.write(projectString)
            projectFile.write("\n")
        projectFile.close()



def getMaxProjectID():
    try:
        projectsFile = open(projectsFilePath, 'r')
    except Exception as e:
        print(e)
        raise Exception("Projects file isn't accessible or not found")
    else:
        projectsLines = projectsFile.readlines()
        if len(projectsLines) == 0:
            return  -1
        maxId = Project.fromJSONtoProject(projectsLines.pop().strip("\n")).id
        return  maxId

"""

#(self, id, title, details, target, startDate, endDate, ownerID)
project1 = Project(1, "This is a tittle 1", "these are details 1", 1500, "sadas", "adsds", 1 )
project2 = Project(2, "This is a tittle 2", "these are details 2", 100, "sadas", "adsds", 2 )
project3 = Project(3, "This is a tittle 3", "these are details 3", 200, "sadas", "adsds", 3 )

appendProject(project1)
appendProject(project2)
appendProject(project3)
"""
