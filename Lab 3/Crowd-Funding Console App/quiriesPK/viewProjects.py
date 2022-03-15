from fileHandling.fileHandler import *

def viewAllProjects():
    projectsList = getProjects()
    if projectsList:
        viewSpicificProjects(projectsList)
        print("_______________________________________")
        input("enter anything to continue...")
    else:
        print("No projects yet!")
        input("enter anything to continue...")




def viewSpicificProjects(projectsList):
    print(f"Projects Count = {len(projectsList)}: " )
    print("Output format:\nid:title:details:target:startDate:endDate:OwnerID")
    for project in projectsList:
        print(project)
