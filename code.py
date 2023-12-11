#imports
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring

#global varibles intialize
global YourChoice
global ProjectsDetails
global AvWorkers
YourChoice = 0
ProjectsDetails = []
AvWorkers = 100

#window select function define.
def WinSelect():
    #Add Project - function call.
    if(YourChoice == 1):
        addProject()

    #Remove Completed Project - function call.
    elif(YourChoice == 2):
        rProject()

    #Add new workers - function call.
    elif(YourChoice == 3):
        AddWorkers()

    #Update Project Details - function call.
    if(YourChoice == 4):
        UpProject()

    #Project Statistics - function call.
    if(YourChoice == 5):
        pStats()

    #Exit the program - function call.
    elif(YourChoice == 6):
        result = messagebox.askyesno('Confirm', 'Do you want to exit the application')#ask confirmation
        if result:
            exit()

#change project status function define.
def changeStat():
    #to check and change the on hold status to on going status

    #variables for the function.
    global ProjectsDetails
    global AvWorkers
    ProjectCode = 0
    ClientsName = ""
    StartDate = ""
    ExEndDate = ""
    NumberOfWorkers = 0
    ProjectStat = ""
    ProjectDetails = []
    index = 0
    projectStatus = ''
    actualenddate = ''

    #process for the function - using the for loop code checks for a projects with on hold status and change status if there are enough free workers
    for index in range(len(ProjectsDetails)):
        if ("on hold" in ProjectsDetails[index]):
            ProjectCode = ProjectsDetails[index][0]
            ClientsName = ProjectsDetails[index][1]
            StartDate = ProjectsDetails[index][2]
            ExEndDate = ProjectsDetails[index][3]
            NumberOfWorkers = ProjectsDetails[index][4]
            if (NumberOfWorkers <= AvWorkers):#check whether there are enough workers to change the projects status
                #if there ara enough workers this code will execute and change the project status to ongoing
                del ProjectsDetails[index]
                ProjectStat = 'ongoing'
                AvWorkers -= NumberOfWorkers
                ProjectDetails = [ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat]
                ProjectsDetails.insert(index, ProjectDetails)
                print(ProjectsDetails)
                message1 = "Project status for project code ("+ str(ProjectCode) +") set to ongoing."
                messagebox.showinfo("show info", message1)

#add project function define.
def addProject():
    #gui setup for add project window
    addproject = Toplevel(mainmenu)
    addproject.geometry("700x370")
    addproject.title("Add a new project")
    
    #entry field variables
    pc = IntVar()
    cn = StringVar()
    sd = StringVar()
    ed = StringVar()
    nw = IntVar()
    
    #gui lables
    label1 = Label(addproject, text="XYZ Company", font=("arial",20,"bold", "italic")).pack()
    label2 = Label(addproject, text="Add a new project", font=("arial",16)).pack()
    label3 = Label(addproject, text="Project Code", font=("arial",10)).place(x=50,y=100)
    label4 = Label(addproject, text="**Enter '0' to Project Code to exit.", font=("arial",10)).place(x=275,y=100)
    label5 = Label(addproject, text="Clients Name", font=("arial",10)).place(x=50,y=130)
    label6 = Label(addproject, text="Start date", font=("arial",10)).place(x=50,y=160)
    label7 = Label(addproject, text="Expected end date", font=("arial",10)).place(x=50,y=190)
    label8 = Label(addproject, text="Number of workers", font=("arial",10)).place(x=50,y=220)
    label9 = Label(addproject, text="Project status", font=("arial",10)).place(x=50,y=250)

    dash1 = Label(addproject, text="-", font=("arial",10)).place(x=250,y=100)
    dash2 = Label(addproject, text="-", font=("arial",10)).place(x=250,y=130)
    dash3 = Label(addproject, text="-", font=("arial",10)).place(x=250,y=160)
    dash4 = Label(addproject, text="-", font=("arial",10)).place(x=250,y=190)
    dash5 = Label(addproject, text="-", font=("arial",10)).place(x=250,y=220)
    dash6 = Label(addproject, text="-", font=("arial",10)).place(x=250,y=250)

    #entry fields for getting inputs
    entry1 = Entry(addproject, textvariable = pc).place(x=525,y=100)
    entry2 = Entry(addproject, textvariable = cn).place(x=525,y=130)
    entry3 = Entry(addproject, textvariable = sd).place(x=525,y=160)
    entry4 = Entry(addproject, textvariable = ed).place(x=525,y=190)
    entry5 = Entry(addproject, textvariable = nw).place(x=525,y=220)

    #list for project status selection
    listbox1 = Listbox(addproject,width=10,height=2, selectmode=SINGLE)
    listbox1.insert(1, "ongoing")
    listbox1.insert(2, "completed")
    listbox1.place(x=525,y=250)

    #code to execute after submit button press 
    def submitb():
        #variables for the function.
        global ProjectsDetails
        global AvWorkers
        stat = listbox1.curselection()
        ProjectCode = 0
        ClientsName = ""
        StartDate = ""
        ExEndDate = ""
        NumberOfWorkers = 0
        ProjectStat = ""
        ProjectDetails = []
        actualenddate = ''
        index = 0
        try:
            #error handelling - check whether the user inputed the correct data type
            ProjectCode = pc.get()
            ClientsName = cn.get()
            StartDate = sd.get()
            ExEndDate = ed.get()
            NumberOfWorkers = nw.get()
            ProjectStat = listbox1.get(stat[0])
        except:
            #code to execute if there are erros
            messagebox.showerror("error", "Project code must be a valid natural number")
            addproject.destroy()
            addProject()
        else:
            #code to execute if there are no erros
            if (ProjectCode == 0):#check whether user input 0 for the project code
                addproject.destroy()#if the project code is 0 - close the add project window
            else:
                #code to execute if the project code is not 0
                if(len(ClientsName) > 0 and len(StartDate) >0 and len(ExEndDate) > 0 and len(ProjectStat)):#check whether user inputed all the string values
                    if(ProjectCode > 0 and NumberOfWorkers > 0):#check whether user inputed valid int values
                        result = messagebox.askyesno('Save details', 'Do you want to save the project')#ask to save the project from the user
                        if result:
                            #if user said yes, this code will execute
                            for index in range(len(ProjectsDetails)):#this for loop checks whether there is another project with the same project code
                                if ProjectCode in ProjectsDetails[index]:
                                    #if there is another project wit the same project code this will execute
                                    messagebox.showerror("error", "Project Code allready exits")
                                    addproject.destroy()
                                    addProject()
                                    break
                            else:#this will execute if the project code hasn't used before
                                if(ProjectStat == "completed"):#code to execute if the user want to input details about a completed project
                                    actualenddate = askstring("Actual end date", "Actual end date of the project")
                                    while actualenddate == None or len(actualenddate) == 0:
                                        actualenddate = askstring("Actual end date", "Enter the actual end date of the project to save")
                                    ProjectDetails = [[ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat, actualenddate]]
                                    ProjectsDetails.extend(ProjectDetails)
                                    messagebox.showinfo("show info", "Project saved")
                                    print(ProjectsDetails)
                                    addproject.destroy()
                                elif(ProjectStat == "ongoing" and NumberOfWorkers <= AvWorkers):#code to execute if the user wants to input an ongoing project and there are enough workers 
                                    ProjectDetails = [[ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat]]
                                    ProjectsDetails.extend(ProjectDetails)
                                    AvWorkers -= NumberOfWorkers
                                    messagebox.showinfo("show info", "Project saved")
                                    print(ProjectsDetails)
                                    addproject.destroy()
                                elif(ProjectStat == "ongoing"):#code to execute if the user wants to input an ongoing project and there are no enough workers
                                    messagebox.showerror("error", "There is no enough workers, project status set to on hold\nThe project status will be updated to ongoing once sufficient number of workers become available")
                                    ProjectStat = "on hold"
                                    ProjectDetails = [[ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat]]
                                    ProjectsDetails.extend(ProjectDetails)
                                    messagebox.showinfo("show info", "Project saved")
                                    print(ProjectsDetails)
                                    addproject.destroy()
                        else:#if user said no, this code will execute
                            messagebox.showinfo("show info", "Project details did not saved")
                            addproject.destroy()
                            addProject()
                    else:#if the user inputed wrong int values this code will execute
                        messagebox.showwarning("error", "Number of workers and project must be a valid counting number")
                        addproject.destroy()
                        addProject()
                else:#if the user didn't input all the requird string values this code will execute
                    messagebox.showerror("error", "all fields are required")
                    addproject.destroy()
                    addProject()
                

    submit = Button(addproject, text="submit", font=("arial",8), width=7, command=submitb).place(x=600,y=320)#button to submit user inputed data to the program

#remove completed project function define.
def rProject():
    #gui setup for remove completed project window
    rproject = Toplevel(mainmenu)
    rproject.geometry("700x200")
    rproject.title("Remove Completed Project")

    #entry field variables
    sb = IntVar()

    #gui lables
    label1 = Label(rproject, text="XYZ Company", font=("arial",20,"bold", "italic")).pack()
    label2 = Label(rproject, text="Remove Completed Project", font=("arial",16)).pack()
    label3 = Label(rproject, text="Project Code", font=("arial",10)).place(x=50,y=100)

    dash1 = Label(rproject, text="-", font=("arial",10)).place(x=250,y=100)

    #entry fields for getting inputs
    entry1 = Entry(rproject, textvariable = sb).place(x=525,y=100)

    #function to execute when the submit button is pressed
    def submitb():
        #variables for the function.
        global ProjectsDetails
        ProjectCode = 0
        try:#error handelling - check whether the user inputed the correct data type
            ProjectCode = sb.get()
        except:#code to execute if there are erros
            messagebox.showerror("error", "Project code must be a valid natural number")
            rproject.destroy()
            rProject()
        else:#code to execute if there are no erros
            if (ProjectCode > 0):
                for index in range(len(ProjectsDetails)):#for loop to find the index of the project code from the list
                    if ProjectCode in ProjectsDetails[index]:
                        if (ProjectsDetails[index][5] == 'completed'):#check wheather the project status is set to completed
                            result = messagebox.askyesno('Confirm', 'Do you want to remove the project')#ask confirmation
                            if result:
                                #if the user confirms this will execute
                                del ProjectsDetails[index]
                                messagebox.showinfo("show info", "Project Removed")
                                print(ProjectsDetails)
                                rproject.destroy()
                            else:
                                #if the user select no this will execute
                                rproject.destroy()
                        else:
                            #if the project status is not set to completed this wiil execute
                            messagebox.showerror("error", "project status is not set to completed")
                            rproject.destroy()
                        break
                else:
                    #if the for loop was unable to fing the user inputed project code this will execute
                    messagebox.showerror("error", "project code not found")
                    rproject.destroy()
                    rProject()
            else:
                #if the usere didn't input a valid int this will execute
                messagebox.showerror("error", "Please enter a valid project code")
                rproject.destroy()
                rProject()
    
    def des():#function to execute when the exit button is pressed
        rproject.destroy()

    submit = Button(rproject, text="submit", font=("arial",8) , width=7, command=submitb).place(x=600,y=150)#data submit button
    Exit = Button(rproject, text="exit", font=("arial",8), command=des).place(x=25,y=150)#exit button

#updat project details function define
def UpProject():
    #gui setup for update project details window
    upproject = Toplevel(mainmenu)
    upproject.geometry("700x400")
    upproject.title("Upate project details")

    #entry field variables
    pc = IntVar()
    cn = StringVar()
    sd = StringVar()
    ed = StringVar()
    nw = IntVar()

    #gui lables
    label1 = Label(upproject, text="XYZ Company", font=("arial",20,"bold", "italic")).pack()
    label2 = Label(upproject, text="Update Project Details", font=("arial",16)).pack()
    label3 = Label(upproject, text="Project Code", font=("arial",10)).place(x=50,y=100)
    label4 = Label(upproject, text="**Enter '0' to Project Code to exit.", font=("arial",10)).place(x=275,y=100)
    label5 = Label(upproject, text="Clients Name", font=("arial",10)).place(x=50,y=160)
    label6 = Label(upproject, text="Start date", font=("arial",10)).place(x=50,y=190)
    label7 = Label(upproject, text="Expected end date", font=("arial",10)).place(x=50,y=220)
    label8 = Label(upproject, text="Number of workers", font=("arial",10)).place(x=50,y=250)
    label9 = Label(upproject, text="Project status", font=("arial",10)).place(x=50,y=280)

    dash1 = Label(upproject, text="-", font=("arial",10)).place(x=250,y=100)
    dash2 = Label(upproject, text="-", font=("arial",10)).place(x=250,y=160)
    dash3 = Label(upproject, text="-", font=("arial",10)).place(x=250,y=190)
    dash4 = Label(upproject, text="-", font=("arial",10)).place(x=250,y=220)
    dash5 = Label(upproject, text="-", font=("arial",10)).place(x=250,y=250)
    dash6 = Label(upproject, text="-", font=("arial",10)).place(x=250,y=280)

    #entry fields for getting inputs
    entry1 = Entry(upproject, textvariable = pc).place(x=525,y=100)
    entry2 = Entry(upproject, textvariable = cn).place(x=525,y=160)
    entry3 = Entry(upproject, textvariable = sd).place(x=525,y=190)
    entry4 = Entry(upproject, textvariable = ed).place(x=525,y=220)
    entry5 = Entry(upproject, textvariable = nw).place(x=525,y=250)

    #list for project status selection
    listbox1 = Listbox(upproject,width=15,height=2, selectmode=SINGLE)

    listbox1.insert(1, "ongoing/on hold")
    listbox1.insert(2, "completed")
    listbox1.place(x=525,y=280)

    #function to execute when the submit button is pressed
    def submitb():
        #variables for the function.
        global ProjectsDetails
        projectStatus = ''
        index = 0
        
        #function to execute when the update button is pressed
        def updateb():
            #variables for the function.
            global ProjectsDetails
            global AvWorkers
            stat = listbox1.curselection()
            ProjectCode = 0
            ClientsName = ""
            StartDate = ""
            ExEndDate = ""
            NumberOfWorkers = 0
            ProjectStat = ""
            actualenddate = ''
            ProjectDetails = []
            try:
                #error handelling - check whether the user inputed the correct data type
                ProjectCode = pc.get()
                ClientsName = cn.get()
                StartDate = sd.get()
                ExEndDate = ed.get()
                NumberOfWorkers = nw.get()
                ProjectStat = listbox1.get(stat[0])
            except:
                #code to execute if there are erros
                messagebox.showerror("error", "error in inputs, please check again")
                upproject.destroy()
                UpProject()
            else:
                #code to execute if there are no erros
                if(len(ClientsName) > 0 and len(StartDate) >0 and len(ExEndDate) > 0 and len(ProjectStat)):#check whether user inputed all the string values
                    if(ProjectCode > 0 and NumberOfWorkers > 0):#check whether user inputed valid int values
                        result = messagebox.askyesno('Update details', 'Do you want to update the project')#ask to save the project from the user
                        if result:
                            #if user said yes, this code will execute
                            if(ProjectsDetails[index][5] == 'ongoing'):
                                AvWorkers += ProjectsDetails[index][4]
                            del ProjectsDetails[index]
                            if(ProjectStat == "completed"):
                                #code to execute if the user want to update details about a completed project
                                actualenddate = askstring("Actual end date", "Actual end date of the project")
                                while actualenddate == None or len(actualenddate) == 0:
                                    actualenddate = askstring("Actual end date", "Enter the actual end date of the project to save")
                                ProjectDetails = [ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat, actualenddate]
                                ProjectsDetails.insert(index, ProjectDetails)
                                messagebox.showinfo("show info", "Project details updated.")
                                print(ProjectsDetails)
                                upproject.destroy()
                                changeStat()
                            elif(ProjectStat == 'ongoing/on hold' and NumberOfWorkers <= AvWorkers):
                                #code to execute if the user want to update details about a ongoing project
                                ProjectStat = "ongoing"
                                AvWorkers -= NumberOfWorkers
                                ProjectDetails = [ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat]
                                ProjectsDetails.insert(index, ProjectDetails)
                                messagebox.showinfo("show info", "Project details updated.")
                                print(ProjectsDetails)
                                upproject.destroy()
                            else:
                                #code to execute if the user wants to update an ongoing project and there are no enough workers
                                messagebox.showerror("error", "There is no enough workers, project status set to on hold\nThe project status will be updated to ongoing once sufficient number of workers become available")
                                ProjectStat = "on hold"
                                ProjectDetails = [ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat]
                                ProjectsDetails.insert(index, ProjectDetails)
                                changeStat()
                                messagebox.showinfo("show info", "Project details updated.")
                                print(ProjectsDetails)
                                upproject.destroy()
                        else:
                            #if user said no, this code will execute
                            messagebox.showinfo("show info", "Project details did not updated.")
                            upproject.destroy()
                    else:
                        #if user input ivalid inputs for project code or available workers this will execute
                        messagebox.showwarning("error", "Number of workers and project code must be a valid counting number")
                        upproject.destroy()
                        UpProject()
                else:
                    #if the user didn't fill out all entry fieilds this will execute
                    messagebox.showerror("error", "all fields are required")
                    upproject.destroy()
                    UpProject()
        try:
            ProjectCode = pc.get()#error handelling - check whether the user inputed the correct data type for project code
        except:
            #code to execute if there are erros
            messagebox.showerror("error", "Project code must be a valid natural number")
            upproject.destroy()
            upproject()
        else:
            #code to execute if there are no erros
            if (ProjectCode == 0):
                upproject.destroy()
            else:
                for index in range(len(ProjectsDetails)):#this for loops checks and find the projects code from saved projects
                    if ProjectCode in ProjectsDetails[index]:
                        projectStatus = ProjectsDetails[index][5]
                        if(projectStatus == 'ongoing' or projectStatus == 'on hold'):#check whether the projects status is ongoing or on hold
                            #show saved project details in the entry fields
                            listbox1.select_set(0)
                            cn.set(ProjectsDetails[index][1])
                            sd.set(ProjectsDetails[index][2])
                            ed.set(ProjectsDetails[index][3])
                            nw.set(ProjectsDetails[index][4])
                            update = Button(upproject, text="update", font=("arial",8), width=7, command=updateb).place(x=600,y=350)#update project details button
                        else:
                            #this will execute if the project is not on hold or ongoing
                            messagebox.showerror("error", "you can only update details on ongoing/onhold projects")
                            upproject.destroy()
                            UpProject()
                        break
                else:
                    #this will execute if there is no project code to be found
                    messagebox.showerror("error", "project code does not exits")
                    upproject.destroy()
                    UpProject()
    #submit data button
    submit = Button(upproject, text="submit", font=("arial",8), width=7, command=submitb).place(x=600,y=127)

#add new workers function define
def AddWorkers():
    #gui setup for add new workers
    addworkers = Toplevel(mainmenu)
    addworkers.geometry("700x200")
    addworkers.title("Add new workers")

    sb = IntVar()#entry field variable

    #gui lables
    label1 = Label(addworkers, text="XYZ Company", font=("arial",20,"bold", "italic")).pack()
    label2 = Label(addworkers, text="Add new workers", font=("arial",16)).pack()
    label3 = Label(addworkers, text="Number of workers to add -", font=("arial",10)).place(x=50,y=100)
    entry1 = Entry(addworkers, textvariable = sb).place(x=525,y=100)#entry field for getting input

    def submitb():
        #variables for the function.
        WorkersToAdd = 0
        global AvWorkers

        try:
            #error handelling - check whether the user inputed the correct data type for project code
            WorkersToAdd = sb.get()
        except:
            #code to execute if there are erros
            messagebox.showerror("error", "Please enter a valid number of workers to add")
            addworkers.destroy()
            addworkers()
        else:
            #code to execute if there are no erros
            if (WorkersToAdd > 0):#check whether the user wants to add a valid number of workers
                result = messagebox.askyesno('confirm', 'Do you want to add')#ask users confirmation
                if result:
                    #if user select yes this will execute
                    AvWorkers += WorkersToAdd
                    messagebox.showinfo("show info", "new workers added")
                    addworkers.destroy()
                    changeStat()
                else:
                    #if user select no this will execute
                    addworkers.destroy()
                    addworkers()
            else:
                #if the user didn't input a valid number of workers to add this will execute
                messagebox.showerror("error", "Please enter a valid number of workers to add")
                addworkers.destroy()
                addworkers()

    def des():#this will execute if the exit button get pressed
        rproject.destroy()

    submit = Button(addworkers, text="submit", font=("arial",8), width=7, command=submitb).place(x=600,y=150)#submit data button
    Exit = Button(addworkers, text="exit", font=("arial",8), command=des).place(x=25,y=150)#exit button

#project statistics.
def pStats():
    #variables for the function.
    global ProjectsDetails
    global AvWorkers
    #gui setup for project statistics
    projectstat = Toplevel(mainmenu)
    projectstat.geometry("700x300")
    projectstat.title("Project Statistics")

    OP = 0
    HP = 0
    CP = 0

    for index in range(len(ProjectsDetails)):#this for loop go through all the saved projects count ongoing, on hold, completed projects  
        if ("ongoing" in ProjectsDetails[index]):
            OP += 1
        elif ("on hold" in ProjectsDetails[index]):
            HP += 1
        elif ('completed' in ProjectsDetails[index]):
            CP +=1
    
    #gui lables
    label1 = Label(projectstat, text="XYZ Company", font=("arial",20,"bold", "italic")).pack()
    label2 = Label(projectstat, text="Project Statistics", font=("arial",16)).pack()
    label3 = Label(projectstat, text="Number of ongoing projects", font=("arial",10)).place(x=50,y=100)
    label4 = Label(projectstat, text="Number of completed projects", font=("arial",10)).place(x=50,y=130)
    label5 = Label(projectstat, text="Number of on hold projects", font=("arial",10)).place(x=50,y=160)
    label6 = Label(projectstat, text="Number of available workers to assign", font=("arial",10)).place(x=50,y=190)

    dash1 = Label(projectstat, text="-", font=("arial",10)).place(x=300,y=100)
    dash2 = Label(projectstat, text="-", font=("arial",10)).place(x=300,y=130)
    dash3 = Label(projectstat, text="-", font=("arial",10)).place(x=300,y=160)
    dash4 = Label(projectstat, text="-", font=("arial",10)).place(x=300,y=190)
    
    #gui lables for outputs
    data1 = Label(projectstat, text=OP, font=("arial",10)).place(x=525,y=100)
    data2 = Label(projectstat, text=CP, font=("arial",10)).place(x=525,y=130)
    data3 = Label(projectstat, text=HP, font=("arial",10)).place(x=525,y=160)
    data4 = Label(projectstat, text=AvWorkers, font=("arial",10)).place(x=525,y=190)
    
    label8 = Label(projectstat, text="Do you want to add a project", font=("arial",10)).place(x=50,y=250)

    def yeS():#code to execute if user select yes
        projectstat.destroy()
        addProject()
    def des():#code to execute if user select no
        projectstat.destroy()

    yEs = Button(projectstat, text="Yes", font=("arial",8), width=5, command=yeS).place(x=535,y=250)#yes button
    nO = Button(projectstat, text="No", font=("arial",8), width=5, command=des).place(x=585,y=250)#no button

#main menu
#gui setup for main menu
mainmenu = Tk()
mainmenu.geometry("700x370")
mainmenu.title("Main Menu")

yc = IntVar()#entry field variable

#gui lables
label1 = Label(mainmenu, text="XYZ Company", font=("arial",20,"bold", "italic")).pack()
label2 = Label(mainmenu, text="Main Menu", font=("arial",16)).pack()
label3 = Label(mainmenu, text="1. Add a new project to existing projects.", font=("arial",10)).place(x=50,y=100)
label4 = Label(mainmenu, text="2. Remove a completed project from existing projects.", font=("arial",10)).place(x=50,y=130)
label5 = Label(mainmenu, text="3. Add new workers to available workers group.", font=("arial",10)).place(x=50,y=160)
label6 = Label(mainmenu, text="4. Update details on ongoing projects.", font=("arial",10)).place(x=50,y=190)
label7 = Label(mainmenu, text="5. Project Statistics", font=("arial",10)).place(x=50,y=220)
label8 = Label(mainmenu, text="6. Exit", font=("arial",10)).place(x=50,y=250)
label9 = Label(mainmenu, text="Your Choice:", font=("arial",10)).place(x=440,y=280)

def submitb():#code to execute when submit button is pressed
    #variables for the function.
    global YourChoice
    try:
        #error handelling - check whether the user inputed the correct data type for project code
        YourChoice = yc.get()
    except:
        #code to execute if there are erros
        messagebox.showerror("error", "Please enter a valid integer selected from main menu")
    else:
        #code to execute if there are no erros
        if YourChoice in range (1,7):#check whether user's input is in the coreect range
            WinSelect()
        else:
            messagebox.showerror("error", "Please enter a valid number selected from main menu")#if the users input is not in correct range this will execute

entry1 = Entry(mainmenu, textvariable = yc).place(x=525,y=280)#entry field for getting input

submit = Button(mainmenu, text="submit", font=("arial",8) , width=7, command=submitb).place(x=600,y=320)#submit button

mainloop()