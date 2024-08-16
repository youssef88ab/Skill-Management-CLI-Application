import termcolor
import json
import datetime

Task_id    = 1 
Tasks = []

def Task_Add(Task_Name):
    
    global Task_id
    
    Task  = {
        "Id" : Task_id , 
        "Description" : Task_Name , 
        "Status"      : "todo" , 
        "CreatedAt"   : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") , 
        "UpdatedAt"   : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    
    Tasks.append(Task)
    
    # Output
    
    print(f"Task added successfully (ID: {Task_id})")
    Task_id += 1

def Task_Update(Task_Id , NewTask):

    # Search For Existing Task By Id In The File And Update It By New One

    # Output : 

    print(f"Task Updated Succesfully")

    pass

def Task_Delete(Task_Id):

    # Find Task By Id And Delete It 

    # Output : 

    pass

def Task_List(Status):

    if (Status == "NULL"): 
        for Task in Tasks : 
            print(Task)


def Main():

    cli = input(termcolor.colored(("task-cli "),color="yellow"))

    if (cli.startswith("add")) :

        Task_Add(cli[4::])
        Main()

    elif(cli.startswith("Update")) : 

        Task_Update(cli[7],cli[9::])

    elif(cli == "list") : Task_List("NULL")

    



Main()