from quiriesPK.commonMethods import *
from fileHandling.fileHandler import setProjects
from projectsPK.ProjectModule import Project

def updateProject(user):
    allProjects = getProjects()
    usersProjects = getProjectsOfUser(user, allProjects)
    if usersProjects:
        projectToUpdate = getProjectID(usersProjects, "update")
        if projectToUpdate == None:
            return False
        else:
            oldProject = None
            for p in allProjects:
                if p.id == projectToUpdate:
                    oldProject = p
                    break

            newProject = getUpdatedProject(oldProject)
            for i in range(len(allProjects)):
                if allProjects[i].id == newProject.id:
                    allProjects[i] = newProject
                    break

            setProjects(allProjects)
            print("Project Updated successfully")
            print("enter any key to coninue...")
            return True
    else:
        print("You have no projects yet...")
        input("Enter any key to coninue...")
        return True

def updateOrContinue(varName):
    print(f"Do you want to update {varName}?")
    x = input("input y or Y to update it, or any other key to ignore: ")
    if x in "yY" :
        return True
    else:
        return False


def getUpdatedProject(oldproject):
    title = oldproject.title
    details = oldproject.details
    target = oldproject.target
    startDate = oldproject.startDate
    endDate = oldproject.endDate
    print("Your project Title: " + title)
    if updateOrContinue("Title"):
        title = readNonEmptyString("Input new title: ")
    print("Your project Details: " + details)
    if updateOrContinue("Details"):
        details = input("Enter new Details: ")
    print("Your project Target : " + str(target))
    if updateOrContinue("Target"):
        target = readPositiveInteger("Enter new Target: ")
    print("Your project Start Date: " + str(startDate))
    if updateOrContinue("Start Date"):
        startDate = readDate("Enter New Start Date")
    if endDate < startDate:
        print("End date cannot be before start Date, Enter new End Date")
        endDate = readEndDate(startDate)
    elif updateOrContinue("End Date"):
        endDate = readEndDate(startDate)

    newProject = Project(oldproject.id, title, details, target, startDate, endDate, oldproject.ownerID)
    return newProject