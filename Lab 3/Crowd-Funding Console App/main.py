from operator import imod
from signUpPk.signUp import *
from loginPk.login import *
from fileHandling.fileHandler import *
from quiriesPK.viewProjects import *
from quiriesPK.deleteProject import deleteProject
from quiriesPK.insertProject import insertProject
from quiriesPK.updateProject import updateProject
import os
import datetime


def loggedInMenu(currentUser):
    print("""Press 
    1) Create new project
    2) View all projects
    3) Edit your projects
    4) delete a project
    5) Search for a project
    6) logout
    7) Exit
    """)
    choice = input("Choose a number: ")
    if choice == "1":
        # Create new project
        insertProject(currentUser)
        pass
    elif choice == "2":
        # View all projects
        viewAllProjects()
        pass
    elif choice == "3":
        updateProject(currentUser)
        # Edit your projects
        pass
    elif choice == "4":
        # delete a project
        deleteProject(currentUser)
    elif choice == "5":
        # Search for a project
        pass
    elif choice == "6":
        # logout
        currentUser = None
        return
    elif choice == "7":
        # Exit
        quit()
    else:
        print("Wrong Choice! try again")
    loggedInMenu(currentUser)


def mainMenu():
    print("Press \n1) for login and \n2) for sign-up \n3)Exit.")
    choice = input("Choice: ")
    if choice == "1":
        user = login()
        if user != None:
            # loggend in successfully
            print(f"Hello, {user.fname} {user.lname}")
            loggedInMenu(user)
        else:
            print("Wrong Email or password! try again or signup")
    elif choice == "2":
        signUp()
    elif choice == "3":
        quit()
    else:
        print("Wrong Choice! try again")
    mainMenu()




mainMenu()


