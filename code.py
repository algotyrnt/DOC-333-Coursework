from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring

global YourChoice
global ProjectsDetails
global AvWorkers

YourChoice = 0
ProjectsDetails = []
AvWorkers = 100

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
        exit()

#add project
def addProject():
    addproject = Toplevel(mainmenu)
    addproject.geometry("700x370")
    addproject.title("Add a new project")
    
    pc = IntVar()
    cn = StringVar()
    sd = StringVar()
    ed = StringVar()
    nw = IntVar()
    
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

    entry1 = Entry(addproject, textvariable = pc).place(x=525,y=100)
    entry2 = Entry(addproject, textvariable = cn).place(x=525,y=130)
    entry3 = Entry(addproject, textvariable = sd).place(x=525,y=160)
    entry4 = Entry(addproject, textvariable = ed).place(x=525,y=190)
    entry5 = Entry(addproject, textvariable = nw).place(x=525,y=220)
    listbox1 = Listbox(addproject,width=10,height=3, selectmode=SINGLE)

    listbox1.insert(1, "ongoing")
    listbox1.insert(2, "on hold")
    listbox1.insert(1, "completed")
    listbox1.place(x=525,y=250)

    
    def submitb():
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
        index = 0
        actualenddate = ''
        try:
            ProjectCode = pc.get()
        except:
            messagebox.showerror("error", "Project code must be a valid natural number")
            addproject.destroy()
            addProject()
        else:
            if (ProjectCode == 0):
                addproject.destroy()
            else:
                StartDate = sd.get()
                ExEndDate = ed.get()
                NumberOfWorkers = nw.get()
                try:
                    ClientsName = cn.get()
                    ProjectStat = listbox1.get(stat[0])
                except:
                    messagebox.showerror("error", "all fields are required")
                    addproject.destroy()
                    addProject()
                else:
                    if(len(ClientsName) > 0 and len(StartDate) >0 and len(ExEndDate0) > 0):
                        if(ProjectCode > 0 and NumberOfWorkers > 0):
                            result = messagebox.askyesno('Save details', 'Do you want to save the project')
                            if result:
                                if(len(ProjectsDetails) == 0):
                                    if(ProjectStat == "completed"):
                                        actualenddate = askstring("Actual end date", "Actual end date of the project")
                                        ProjectDetails = [[ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat, actualenddate]]
                                        ProjectsDetails.extend(ProjectDetails)
                                        messagebox.showinfo("show info", "Project saved")
                                        print(ProjectsDetails)
                                        addproject.destroy()
                                    elif(ProjectStat == "on hold"):
                                        ProjectDetails = [[ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat]]
                                        ProjectsDetails.extend(ProjectDetails)
                                        messagebox.showinfo("show info", "Project saved")
                                        print(ProjectsDetails)
                                        addproject.destroy()
                                    elif(ProjectStat == "ongoing" and NumberOfWorkers <= AvWorkers):
                                        ProjectDetails = [[ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat]]
                                        ProjectsDetails.extend(ProjectDetails)
                                        AvWorkers -= NumberOfWorkers
                                        messagebox.showinfo("show info", "Project saved")
                                        print(ProjectsDetails)
                                        addproject.destroy()
                                    else:
                                        messagebox.showwarning("warning", "There is no enough workers")
                                        addproject.destroy()
                                        addProject()
                                else:
                                    for index in range(len(ProjectsDetails)):
                                        if ProjectCode in ProjectsDetails[index]:
                                            messagebox.showwarning("warning", "Project Code allready exits")
                                            addproject.destroy()
                                            addProject()
                                            break
                                        else:
                                            if(ProjectStat == "completed"):
                                                actualenddate = askstring("Actual end date", "Actual end date of the project")
                                                ProjectDetails = [[ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat, actualenddate]]
                                                ProjectsDetails.extend(ProjectDetails)
                                                messagebox.showinfo("show info", "Project saved")
                                                print(ProjectsDetails)
                                                addproject.destroy()
                                            elif(ProjectStat == "on hold"):
                                                ProjectDetails = [[ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat]]
                                                ProjectsDetails.extend(ProjectDetails)
                                                messagebox.showinfo("show info", "Project saved")
                                                print(ProjectsDetails)
                                                addproject.destroy()
                                            elif(ProjectStat == "ongoing" and NumberOfWorkers <= AvWorkers):
                                                ProjectDetails = [[ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat]]
                                                ProjectsDetails.extend(ProjectDetails)
                                                AvWorkers -= NumberOfWorkers
                                                messagebox.showinfo("show info", "Project saved")
                                                print(ProjectsDetails)
                                                addproject.destroy()
                                            else:
                                                messagebox.showwarning("warning", "There is no enough workers")
                                                addproject.destroy()
                                                addProject()
                                            break
                            else:
                                addproject.destroy()
                                addProject()
                        else:
                            messagebox.showwarning("error", "Number of workers and project must be a valid counting number")
                            addproject.destroy()
                            addProject()
                    else:
                        messagebox.showerror("error", "all fields are required")
                        addproject.destroy()
                        addProject()
                

    submit = Button(addproject, text="Submit Data", font=("arial",8), command=submitb).place(x=585,y=320)

#remove completed project
def rProject():
    rproject = Toplevel(mainmenu)
    rproject.geometry("700x200")
    rproject.title("Remove Completed Project")

    sb = IntVar()

    label1 = Label(rproject, text="XYZ Company", font=("arial",20,"bold", "italic")).pack()
    label2 = Label(rproject, text="Remove Completed Project", font=("arial",16)).pack()
    label3 = Label(rproject, text="Project Code", font=("arial",10)).place(x=50,y=100)

    entry1 = Entry(rproject, textvariable = sb).place(x=525,y=100)

    dash1 = Label(rproject, text="-", font=("arial",10)).place(x=250,y=100)

    def submitb():
        global ProjectsDetails
        ProjectCode = 0
        try:
            ProjectCode = sb.get()
        except:
            messagebox.showerror("error", "Project code must be a valid natural number")
            addproject.destroy()
            addProject()
        else:
            if (ProjectCode > 0):
                for index in range(len(ProjectsDetails)):
                    if ProjectCode in ProjectsDetails[index]:
                        if 'completed' in ProjectsDetails[index]:
                            result = messagebox.askyesno('Confirm', 'Do you want to remove the project')
                            if result:
                                del ProjectsDetails[index]
                                messagebox.showinfo("show info", "Project Removed")
                                project.destroy()
                            else:
                                rproject.destroy()
                                rProject()
                        else:
                            messagebox.showerror("error", "project status is not set to completed")
                    else:
                        messagebox.showerror("error", "project code not found")
                result = messagebox.askyesno('Confirm', 'Do you want to remove the project')
            else:
                messagebox.showerror("error", "Please enter a valid project code")
                rproject.destroy()
                rProject()
    
    def des():
        rproject.destroy()

    submit = Button(rproject, text="Submit Data", font=("arial",8), command=submitb).place(x=585,y=150)
    Exit = Button(rproject, text="Exit", font=("arial",8), command=des).place(x=25,y=150)

#updat project details.
def UpProject():
    upproject = Toplevel(mainmenu)
    upproject.geometry("700x400")
    upproject.title("Upate project details")

    pc = IntVar()
    cn = StringVar()
    sd = StringVar()
    ed = StringVar()
    nw = IntVar()

    label1 = Label(upproject, text="XYZ Company", font=("arial",20,"bold", "italic")).pack()
    label2 = Label(upproject, text="Update Project Details", font=("arial",16)).pack()
    label3 = Label(upproject, text="Project Code", font=("arial",10)).place(x=50,y=100)
    label4 = Label(upproject, text="**Enter '0' to Project Code to exit.", font=("arial",10)).place(x=275,y=100)
    label5 = Label(upproject, text="Clients Name", font=("arial",10)).place(x=50,y=130)
    label6 = Label(upproject, text="Start date", font=("arial",10)).place(x=50,y=160)
    label7 = Label(upproject, text="Expected end date", font=("arial",10)).place(x=50,y=190)
    label8 = Label(upproject, text="Number of workers", font=("arial",10)).place(x=50,y=220)
    label9 = Label(upproject, text="Project status", font=("arial",10)).place(x=50,y=250)

    entry1 = Entry(upproject, textvariable = pc).place(x=525,y=100)
    entry2 = Entry(upproject, textvariable = cn).place(x=525,y=130)
    entry3 = Entry(upproject, textvariable = sd).place(x=525,y=160)
    entry4 = Entry(upproject, textvariable = ed).place(x=525,y=190)
    entry5 = Entry(upproject, textvariable = nw).place(x=525,y=220)

    listbox1 = Listbox(upproject,width=10,height=3, selectmode=SINGLE)

    dash1 = Label(upproject, text="-", font=("arial",10)).place(x=250,y=100)
    dash2 = Label(upproject, text="-", font=("arial",10)).place(x=250,y=130)
    dash3 = Label(upproject, text="-", font=("arial",10)).place(x=250,y=160)
    dash4 = Label(upproject, text="-", font=("arial",10)).place(x=250,y=190)
    dash5 = Label(upproject, text="-", font=("arial",10)).place(x=250,y=220)
    dash6 = Label(upproject, text="-", font=("arial",10)).place(x=250,y=250)

    listbox1.insert(1, "ongoing")
    listbox1.insert(2, "on hold")
    listbox1.insert(1, "completed")
    listbox1.place(x=525,y=250)

    def submitb():
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
        index = 0
        projectStatus = ''
        actualenddate = ''
        try:
            ProjectCode = pc.get()
        except:
            messagebox.showerror("error", "Project code must be a valid natural number")
            addproject.destroy()
            addProject()
        else:
            if (ProjectCode == 0):
                addproject.destroy()
            else:
                try:
                    ProjectCode = pc.get()
                    ClientsName = cn.get()
                    StartDate = sd.get()
                    ExEndDate = ed.get()
                    NumberOfWorkers = nw.get()
                    ProjectStat = listbox1.get(stat[0])
                except:
                    messagebox.showerror("error", "all fields are required")
                    addproject.destroy()
                    addProject()
                else:
                    for index in range(len(ProjectsDetails)):
                        if ProjectCode in ProjectsDetails[index]:
                            result = messagebox.askyesno('Update details', 'Do you want to update the project')
                            if result:
                                projectStatus = ProjectsDetails[index][5]
                                if(projectStatus == 'ongoing'):
                                    AvWorkers += ProjectsDetails[index][4]
                                del ProjectsDetails[index]
                                if(ProjectStat == "completed"):
                                    actualenddate = askstring("Actual end date", "Actual end date of the project")
                                    ProjectDetails = [[ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat, actualenddate]]
                                    ProjectsDetails.extend(cProjectDetails)
                                    messagebox.showinfo("show info", "Project details updated.")
                                    print(ProjectsDetails)
                                elif(ProjectStat == 'on hold'):
                                    ProjectDetails = [ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat]
                                    ProjectsDetails.insert(index, ProjectDetails)
                                    messagebox.showinfo("show info", "Project details updated.")
                                    print(ProjectsDetails)
                                elif(ProjectStat == 'ongoing' and NumberOfWorkers <= AvWorkers):
                                    AvWorkers -= NumberOfWorkers
                                    ProjectDetails = [ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat]
                                    ProjectsDetails.insert(index, ProjectDetails)
                                    messagebox.showinfo("show info", "Project details updated.")
                                    print(ProjectsDetails)
                                else:
                                    messagebox.showerror("error", "There is no enough workers")
                                    addproject.destroy()
                                    addProject()
                            else:
                                addproject.destroy()
                                addProject()
                            break
                        else:
                            messagebox.showerror("error", "project Code does not exits")
                            addproject.destroy()
                            addProject()
                            break
    
    submit = Button(upproject, text="Submit Data", font=("arial",8), command=submitb).place(x=585,y=320)

#add new workers
def AddWorkers():
    addworkers = Toplevel(mainmenu)
    addworkers.geometry("700x200")
    addworkers.title("Add new workers")

    sb = IntVar()

    label1 = Label(addworkers, text="XYZ Company", font=("arial",20,"bold", "italic")).pack()
    label2 = Label(addworkers, text="Add new workers", font=("arial",16)).pack()
    label3 = Label(addworkers, text="Number of workers to add -", font=("arial",10)).place(x=50,y=100)
    entry1 = Entry(addworkers, textvariable = sb).place(x=525,y=100)

    def submitb():
        
        WorkersToAdd = 0
        global AvWorkers

        WorkersToAdd = sb.get()
        if (WorkersToAdd > 0):
            result = messagebox.askyesno('confirm', 'Do you want to add')
            if result:
                AvWorkers += WorkersToAdd
            else:
                addworkers.destroy()
                addworkers()
        else:
            messagebox.showwarning("warning", "Please enter the amount of workers to add")
            addworkers.destroy()
            addworkers()

    submit = Button(addworkers, text="Submit Data", font=("arial",8), command=submitb).place(x=585,y=150)

#project statistics.
def pStats():
    global ProjectsDetails
    global AvWorkers
    projectstat = Toplevel(mainmenu)
    projectstat.geometry("700x300")
    projectstat.title("Project Statistics")

    OP = 0
    HP = 0
    CP = 0

    for index in range(len(ProjectsDetails)):
        if ("ongoing" in ProjectsDetails[index]):
            OP += 1
        elif ("on hold" in ProjectsDetails[index]):
            HP += 1
        elif ('completed' in ProjectsDetails[index]):
            CP +=1
    
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
    
    data1 = Label(projectstat, text=OP, font=("arial",10)).place(x=525,y=100)
    data2 = Label(projectstat, text=CP, font=("arial",10)).place(x=525,y=130)
    data3 = Label(projectstat, text=HP, font=("arial",10)).place(x=525,y=160)
    data4 = Label(projectstat, text=AvWorkers, font=("arial",10)).place(x=525,y=190)
    
    label8 = Label(projectstat, text="Do you want to add a project", font=("arial",10)).place(x=50,y=250)

    def yeS():
        projectstat.destroy()
        addProject()
    def des():
        projectstat.destroy()

    yEs = Button(projectstat, text="Yes", font=("arial",8), width=5, command=yeS).place(x=535,y=250)
    nO = Button(projectstat, text="No", font=("arial",8), width=5, command=des).place(x=585,y=250)

#main menu
mainmenu = Tk()
mainmenu.geometry("700x370")
mainmenu.title("Main Menu")

yc = IntVar()

label1 = Label(mainmenu, text="XYZ Company", font=("arial",20,"bold", "italic")).pack()
label2 = Label(mainmenu, text="Main Menu", font=("arial",16)).pack()
label3 = Label(mainmenu, text="1. Add a new project to existing projects.", font=("arial",10)).place(x=50,y=100)
label4 = Label(mainmenu, text="2. Remove a completed project from existing projects.", font=("arial",10)).place(x=50,y=130)
label5 = Label(mainmenu, text="3. Add new workers to available workers group.", font=("arial",10)).place(x=50,y=160)
label6 = Label(mainmenu, text="4. Update details on ongoing projects.", font=("arial",10)).place(x=50,y=190)
label7 = Label(mainmenu, text="5. Project Statistics", font=("arial",10)).place(x=50,y=220)
label8 = Label(mainmenu, text="6. Exit", font=("arial",10)).place(x=50,y=250)
label9 = Label(mainmenu, text="Your Choice:", font=("arial",10)).place(x=440,y=280)

def submitb():
    global YourChoice
    try:
        YourChoice = yc.get()
    except:
        messagebox.showerror("error", "Please enter a valid number selected from main menu")
    else:
        if YourChoice in range (1,7):
            WinSelect()
        else:
            messagebox.showerror("error", "Please enter a valid number selected from main menu")

entry1 = Entry(mainmenu, textvariable = yc).place(x=525,y=280)

submit = Button(mainmenu, text="submit", font=("arial",8) , width=7, command=submitb).place(x=600,y=320)

mainloop()