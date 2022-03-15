from ConsoleReading.readers import *
from fileHandling.fileHandler import getProjects
from fileHandling.fileHandler import setProjects
from quiriesPK.commonMethods import *



def deleteProject(user):
    allProjects = getProjects()
    usersProjects = getProjectsOfUser(user, allProjects)
    if usersProjects :
        projectToDelete = getProjectID(usersProjects, "delete")
        if projectToDelete == None:
            return False
        else:
            updatedProjectsList = [project for project in allProjects if project.id != projectToDelete]
            setProjects(updatedProjectsList)
            print("Project Deleted successfully")
            print("enter any key to coninue...")
            return True
    else:
        print("You have no projects yet...")
        input("Enter any key to coninue...")
        return  True