#intialize variables
global ProjectsDetails
global AvWorkers

YourChoice = 0
ProjectCode = 0
ClientsName = ""
StartDate = ""
ExEndDate = ""
NumberOfWorkers = 0
ProjectStat = ""
YesNo = ""
WorkersToAdd = 0
ProjectDetails = []
ProjectsDetails = []
index = 0
AvWorkers = 100

#main menu - function
def mainMenu():
    print("                               XYZ Company")
    print("                                Main Menu")
    print("")
    print("1. Add a new project to existing projects.")
    print("2. Remove a completed project from existing projects.")
    print("3. Add new workers to available workers group.")
    print("4. Update details on ongoing projects.")
    print("5. Project Statistics")
    print("6. Exit")
    print("")
    YourChoice = int(input("                                                Your Choice:  "))
    #Add a new project - function call.
    if(YourChoice == 1):
        addProject()

    #Remove Completed Project - function call.
    elif(YourChoice == 2):
        rProject()

    #Add new workers.
    elif(YourChoice == 3):
        AddWorkers()

    #Update Project Details.
    if(YourChoice == 4):
        UpProject()

    #Project Statistics.
    if(YourChoice == 5):
        pStats()

    #Exit the program
    elif(YourChoice == 6):
        exit()

#Add a new project - function.
def addProject():
    global AvWorkers
    print("                               XYZ Company")
    print("                             Add a new project")
    print("")
    ProjectCode = int(input("Project Code   -     **Enter '0' to Project Code to exit.  "))
    if(ProjectCode == 0):
        mainMenu()
    else:
        ClientsName = input("Clients Name      -  ")
        StartDate = input("Start date        -  ")
        ExEndDate = input("Expected end date -  ")
        NumberOfWorkers = int(input("Number of workers -  "))
        ProjectStat = input("Project status    -  ")
        print("")
        YesNo = input("Do you want to update the project details (Yes/No)? ")
        if(YesNo == "Yes" or YesNo == "yes"):
            if(NumberOfWorkers <= AvWorkers):
                ProjectDetails = [[ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat]]
                ProjectsDetails.extend(ProjectDetails)
                AvWorkers -= NumberOfWorkers
                print("project details updated")
            else:
                print("There is no enough workers")
            print("Opening main menu")
            mainMenu()
        elif(YesNo == "No" or YesNo == "no"):
            ProjectCode = 0
            ClientsName = ""
            StartDate = ""
            ExEndDate = ""
            NumberOfWorkers = 0
            ProjectStat = ""
            print("Opening main menu")
            mainMenu()

#Remove Completed Project - function.
def rProject():
    print("                               XYZ Company")
    print("                          Remove Completed Project")
    print("")
    ProjectCode = int(input("Project Code   -  "))
    print("")
    YesNo = input("Do you want to remove the project (Yes/No)? ")
    if(YesNo == "Yes" or YesNo == "yes"):
        for index in range(len(ProjectsDetails)+1):
            if ProjectCode in ProjectsDetails[index]:
                del ProjectsDetails[index]
                print('Project Removed')
                break
            else:
                print("error, project code not found.")
        print("Opening main menu")
        mainMenu()
    elif(YesNo == "No" or YesNo == "no"):
        print("Opening main menu")
        mainMenu()

#update project details - function.
def UpProject():
    print("                               XYZ Company")
    print("                           Update project Details")
    print("")
    ProjectCode = int(input("Project Code   -     **Enter '0' to Project Code to exit.  "))
    if(ProjectCode == 0):
        print("Opening main menu")
        mainMenu()
    else:
        ClientsName = input("Clients Name      -  ")
        StartDate = input("Start date        -  ")
        ExEndDate = input("Expected end date -  ")
        NumberOfWorkers = int(input("Number of workers -  "))
        ProjectStat = input("Project status    -  ")
        print("")
        YesNo = input("Do you want to update the project details (Yes/No)? ")
        if(YesNo == "Yes" or YesNo == "yes"):
            if(NumberOfWorkers <= AvWorkers):
                for index in range(len(ProjectsDetails)):
                    if ProjectCode in ProjectsDetails[index]:
                        AvWorkers += ProjectsDetails[index][4]
                        AvWorkers -= NumberOfWorkers
                        del ProjectsDetails[index]
                        ProjectDetails = [ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat]
                        ProjectsDetails.insert(index, ProjectDetails)
                        print('Project detail updated')
                        break
                    else:
                        print("error, project code not found.")
                print("Opening main menu")
                mainMenu()
            else:
                print("There is no enough workers")
                print("Opening main menu")
                mainMenu()
        elif(YesNo == "No" or YesNo == "no"):
            print("Opening main menu")
            ProjectCode = 0
            ClientsName = ""
            StartDate = ""
            ExEndDate = ""
            NumberOfWorkers = 0
            ProjectStat = ""
            mainMenu()  

#Add new workers - function.
def AddWorkers():
    print("                               XYZ Company")
    print("                             Add new Workers")
    print("")
    WorkersToAdd = int(input("Number workers to add   -  "))
    print("")
    YesNo = input("Do you want to add (Yes/No)? ")
    if(YesNo == "Yes" or YesNo == "yes"):
            AvWorkers += WorkersToAdd
            print("Workers added")
            print("Opening main menu")
            mainMenu()
    elif(YesNo == "No" or YesNo == "no"):
            print("Opening main menu")
            mainMenu()

#Project Statistics - function.
def pStats():
    #intializing local variables
    index = 0
    NumberOfOnProjects = 0
    NumberOfHolProjects = 0
    NumberOfComProjects = 0

    for index in range(len(ProjectsDetails)):
        if "ongoing" in ProjectsDetails[index]:
            NumberOfOnProjects += 1
        elif "on hold" in ProjectsDetails[index]:
            NumberOfHolProjects += 1
        elif "completed" in ProjectsDetails[index]:
            NumberOfComProjects += 1      

    print("                               XYZ Company")
    print("                             Project Statistics")
    print("")
    print("Number of ongoig projects  - ", NumberOfOnProjects)
    print("Number of completed projects  - ", NumberOfComProjects)
    print("Number of on hold projects  - ", NumberOfHolProjects)
    print("Number of availabel workers to assign  - ", AvWorkers)
    print("")
    YesNo = input("Do you want to add the project (Yes/No)? ")
    if(YesNo == "Yes" or YesNo == "yes"):
            addProject()
    elif(YesNo == "No" or YesNo == "no"):
            print("Opening main menu")
            mainMenu()

#main menu function call
mainMenu()