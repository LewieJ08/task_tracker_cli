import json 
import datetime
import os

JSONFILE = "tasks.json"
COMMANDS = ["exit","add","update","delete","mark-in-progress","mark-done","list","clear"]
STATUS = ["todo","in-progress","done"]

def currentTime():
    return str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))

# Core functions
def add(taskName):
    with open(JSONFILE) as file:
        data = json.load(file)

    iD = 1
    current_ids = []

    for item in data:
        current_ids.append(item["id"])

    while iD in current_ids:
        iD += 1

    data.append({
            "id": iD,
            "description": taskName,
            "status": "todo",
            "createdAt": currentTime(),
            "updatedAt": None,
    })

    with open(JSONFILE,"w") as file:
        json.dump(data,file,indent = 4)

    print(f"Task saved successfully. (ID: {iD})")

def update(taskId):
    with open(JSONFILE) as file:
        data = json.load(file)
    
    for item in data:
        if item["id"] == taskId:
            updatedTask = input("> ").lower().strip()
            item["description"] = updatedTask
            item["updatedAt"] = currentTime()
            
            with open(JSONFILE,"w") as file:
                json.dump(data,file,indent = 4)

            print(f"Task updated successfully to '{updatedTask}'.")
            return
               
    print("Task not found.")
    
    
def delete(taskId):
    updatedData = []

    with open(JSONFILE) as file:
        data = json.load(file)

    for item in data:
        if item["id"] != taskId:
            updatedData.append(item)
            
    if len(updatedData) == len(data):
        print("Task not found.")
        return 
    
    with open(JSONFILE,"w") as file:
        json.dump(updatedData,file,indent = 4)

    print("Task deleted successfully.")
           
# Marking task/updating task status
def mark_task(command,taskId):
    with open(JSONFILE) as file:
        data = json.load(file)

    for item in data:
        if item["id"] == taskId:
            if command == "mark-in-progress":
                item["status"] = "in-progress"

                with open(JSONFILE,"w") as file:
                    json.dump(data,file,indent = 4)
                print("Task status updated successfully.")
                return
            
            elif command == "mark-done":
                item["status"] = "done"

                with open(JSONFILE,"w") as file:
                    json.dump(data,file,indent = 4)
                print("Task status updated successfully.")
                return
    print("Task not found.")

# Listing tasks
def list_tasks():
    with open(JSONFILE) as file:
        data = json.load(file)

    for item in data:
        for i in item:
            if i != "id":
                if list(item.keys())[-1] == i:
                    print(i+":",(item[i]), end="")
                else:
                    print(i+":",(item[i]), end=", ")
        print()

def list_by_status(status):
    task_list = []

    with open(JSONFILE) as file:
        data = json.load(file)

    for item in data:
        if item["status"] == status:
            task_list.append(item)
    
    if status not in STATUS:
        print("Invalid Status.")
        return

    elif len(task_list) == 0:
        print(f"No tasks with the '{status}' Status could be found")    
        return    

    print(task_list)

#Deleting all tasks/clearing json file
def clear():
    while True:
        inp = input("Are you sure you want to delete all tasks? (y/n)> ").lower().strip()
        if inp == "y":
            with open(JSONFILE,"w") as file:
                json.dump([], file) 
            break
        elif inp == "n":
            break
        else:
            print("Invalid Input.")
            

# Main function
def main():
    os.system("cls")

    if not os.path.exists(JSONFILE):
        with open(JSONFILE, "w") as file:
            json.dump([], file) 

    # Main loop
    while True:
        uinput = input("Task-Tracker> ").lower().strip()
        splitInput = uinput.split(" ", 1)
        if splitInput[0] == COMMANDS[0]:
            break

        elif len(splitInput) == 1 and splitInput[0] == COMMANDS[6]:
            list_tasks()
            continue

        elif splitInput[0] == COMMANDS[7]:
            clear()
            continue
            
        elif len(splitInput) != 2:
            print("Invalid input.")
            continue

        command, argument = splitInput

        if command == COMMANDS[1]:
            add(argument)

        elif command == COMMANDS[2]:
            try:
                argument = int(argument)
                update(argument)
            except ValueError:
                print("Task ID must be an integer")

        elif command == COMMANDS[3]:
            try:
                argument = int(argument)
                delete(argument)
            except ValueError:
                print("Task ID must be an integer")

        elif command == COMMANDS[4]:
            try:
                argument = int(argument)
                mark_task(command,argument)
            except ValueError:
                print("Task ID must be an integer")

        elif command == COMMANDS[5]:
            try:
                argument = int(argument)
                mark_task(command,argument)
            except ValueError:
                print("Task ID must be an integer")

        elif command == COMMANDS[6]:
            list_by_status(argument)

        else:
            print(f"The term '{command}' is not recognized as a TaskTracker command.")
            continue

# Program entry point
if __name__ == "__main__":
    main()