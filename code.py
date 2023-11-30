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
    global YourChoice
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
    label3 = Label(addproject, text="Project Code          -     **Enter '0' to Project Code to exit.", font=("arial",10)).place(x=50,y=100)
    label4 = Label(addproject, text="Clients Name         -", font=("arial",10)).place(x=50,y=130)
    label5 = Label(addproject, text="Start date              -", font=("arial",10)).place(x=50,y=160)
    label6 = Label(addproject, text="Expected end date -", font=("arial",10)).place(x=50,y=190)
    label7 = Label(addproject, text="Number of workers -", font=("arial",10)).place(x=50,y=220)
    label8 = Label(addproject, text="Project status        -", font=("arial",10)).place(x=50,y=250)

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
        ProjectCode = pc.get()
        ClientsName = cn.get()
        StartDate = sd.get()
        ExEndDate = ed.get()
        NumberOfWorkers = nw.get()
        ProjectStat = listbox1.get(stat[0])
        if (ProjectCode == 0):
            addproject.destroy()
        else:
            result = messagebox.askyesno('Save details', 'Do you want to save the project')
            if result:
                if(len(ProjectsDetails) == 0):
                    if(ProjectStat == "completed"):
                        actualenddate = askstring("Actual end date", "Actual end date of the project")
                        cProjectDetails = [[ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat, actualenddate]]
                        cProjectsDetails.extend(cProjectDetails)
                        messagebox.showinfo("show info", "Project saved")
                        print(cProjectsDetails)
                        addproject.destroy()
                    elif(NumberOfWorkers <= AvWorkers):
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
                                actualenddate = askstring("Actual end date", "Actual end date")
                            elif(NumberOfWorkers <= AvWorkers):
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

    submit = Button(addproject, text="Submit Data", font=("arial",8), command=submitb).place(x=585,y=320)

def rProject():
    rproject = Toplevel(mainmenu)
    rproject.geometry("700x200")
    rproject.title("Add a new project")

    sb = IntVar()

    label1 = Label(rproject, text="XYZ Company", font=("arial",20,"bold", "italic")).pack()
    label2 = Label(rproject, text="Remove Completed Project", font=("arial",16)).pack()
    label3 = Label(rproject, text="Project Code          -", font=("arial",10)).place(x=50,y=100)
    entry1 = Entry(rproject, textvariable = sb).place(x=525,y=100)

    def submitb():
        
        ProjectCode = 0

        ProjectCode = sb.get()
        if (ProjectCode > 0):
            result = messagebox.askyesno('Confirm', 'Do you want to remove the project')
            if result:
                for index in range(len(ProjectsDetails)):
                    if ProjectCode in ProjectsDetails[index]:
                        if(ProjectsDetails[index][5] == "completed"):
                            del ProjectsDetails[index]
                            messagebox.showinfo("show info", "Project Removed")
                            rproject.destroy()
                        else:
                            messagebox.showwarning("warning", "error, project is not completed")
                        break
                    else:
                        messagebox.showwarning("warning", "error, project code not found")
                        rproject.destroy()
                        rProject()
            else:
                rproject.destroy()
                rProject()
        else:
            messagebox.showwarning("warning", "Please enter a valid project code")
            rproject.destroy()
            rProject()
    
    def des():
        rproject.destroy()


    submit = Button(rproject, text="Submit Data", font=("arial",8), command=submitb).place(x=585,y=150)
    Exit = Button(rproject, text="Exit", font=("arial",8), command=des).place(x=25,y=150)

def UpProject():
    upproject = Toplevel(mainmenu)
    upproject.geometry("700x400")
    upproject.title("Add a new project")

    pc = IntVar()
    cn = StringVar()
    sd = StringVar()
    ed = StringVar()
    nw = IntVar()

    label1 = Label(upproject, text="XYZ Company", font=("arial",20,"bold", "italic")).pack()
    label2 = Label(upproject, text="Add a new project", font=("arial",16)).pack()
    label3 = Label(upproject, text="Project Code          -     **Enter '0' to Project Code to exit.", font=("arial",10)).place(x=50,y=100)
    entry1 = Entry(upproject, textvariable = pc).place(x=525,y=100)
    label4 = Label(upproject, text="Clients Name         -", font=("arial",10)).place(x=50,y=130)
    entry2 = Entry(upproject, textvariable = cn).place(x=525,y=130)
    label5 = Label(upproject, text="Start date              -", font=("arial",10)).place(x=50,y=160)
    entry3 = Entry(upproject, textvariable = sd).place(x=525,y=160)
    label6 = Label(upproject, text="Expected end date -", font=("arial",10)).place(x=50,y=190)
    entry4 = Entry(upproject, textvariable = ed).place(x=525,y=190)
    label7 = Label(upproject, text="Number of workers -", font=("arial",10)).place(x=50,y=220)
    entry5 = Entry(upproject, textvariable = nw).place(x=525,y=220)
    label8 = Label(upproject, text="Project status        -", font=("arial",10)).place(x=50,y=250)
    listbox1 = Listbox(upproject,width=10,height=3, selectmode=SINGLE)

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
        ProjectCode = pc.get()
        ClientsName = cn.get()
        StartDate = sd.get()
        ExEndDate = ed.get()
        NumberOfWorkers = nw.get()
        ProjectStat = listbox1.get(stat[0])
        if (ProjectCode == 0):
            addproject.destroy()
        else:
            result = messagebox.askyesno('Update details', 'Do you want to update the project')
            if result:
                for index in range(len(ProjectsDetails)):
                    if ProjectCode in ProjectsDetails[index]:
                        AvWorkers += ProjectsDetails[index][4]
                        if(NumberOfWorkers <= AvWorkers):
                            AvWorkers -= NumberOfWorkers
                            del ProjectsDetails[index]
                            ProjectDetails = [ProjectCode, ClientsName, StartDate, ExEndDate, NumberOfWorkers, ProjectStat]
                            ProjectsDetails.insert(index, ProjectDetails)
                            messagebox.showinfo("show info", "Project saved")
                            print(ProjectsDetails)
                        else:
                            messagebox.showwarning("warning", "There is no enough workers")
                            addproject.destroy()
                            addProject()
                        break
                    else:
                        messagebox.showwarning("warning", "Project Code does not exits")
                        addproject.destroy()
                        addProject()
                        break
            else:
                addproject.destroy()
                addProject()
    
    submit = Button(upproject, text="Submit Data", font=("arial",8), command=submitb).place(x=585,y=320)

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

def pStats():
    projectstat = Toplevel(mainmenu)
    projectstat.geometry("700x300")
    projectstat.title("Project Statistics")

    global AvWorkers
    global ProjectsDetails
    OP = 0
    HP = 0
    CP = 0

    for index in range(len(ProjectsDetails)):
        if ("ongoing" in ProjectsDetails[index]):
            OP += 1
        elif ("on hold" in ProjectsDetails[index]):
            HP += 1
        elif ("completed" in ProjectsDetails[index]):
            CP += 1 
    
    label1 = Label(projectstat, text="XYZ Company", font=("arial",20,"bold", "italic")).pack()
    label2 = Label(projectstat, text="Project Statistics", font=("arial",16)).pack()
    label3 = Label(projectstat, text="Number of ongoing projects", font=("arial",10)).place(x=50,y=100)
    dash1 = Label(projectstat, text="-", font=("arial",10)).place(x=300,y=100)
    label4 = Label(projectstat, text="Number of completed projects", font=("arial",10)).place(x=50,y=130)
    dash2 = Label(projectstat, text="-", font=("arial",10)).place(x=300,y=130)
    label5 = Label(projectstat, text="Number of on hold projects", font=("arial",10)).place(x=50,y=160)
    dash3 = Label(projectstat, text="-", font=("arial",10)).place(x=300,y=160)
    label6 = Label(projectstat, text="Number of available workers to assign", font=("arial",10)).place(x=50,y=190)
    dash4 = Label(projectstat, text="-", font=("arial",10)).place(x=300,y=190)
    data1 = Label(projectstat, text=OP, font=("arial",10)).place(x=525,y=100)
    data2 = Label(projectstat, text=CP, font=("arial",10)).place(x=525,y=130)
    data3 = Label(projectstat, text=HP, font=("arial",10)).place(x=525,y=160)
    data4 = Label(projectstat, text=AvWorkers, font=("arial",10)).place(x=525,y=190)
    
    label8 = Label(projectstat, text="Do you want to add a project", font=("arial",10)).place(x=50,y=250)

    def yeS():
        projectstat()
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

def submitb():
    global YourChoice
    YourChoice = yc.get()
    WinSelect()

entry1 = Entry(mainmenu, textvariable = yc).place(x=525,y=280)

submit = Button(mainmenu, text="Submit Data", font=("arial",8), command=submitb).place(x=585,y=320)

mainloop()