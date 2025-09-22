import json
import os


def print_tasks(path="Task-Manager.json"):
    print("\n* My Tasks *")
    with open(path, "r") as file:
        json_data = json.load(file)
    for index, task in enumerate(json_data, start=1):
        completed = "Still in progress" if task["completed"] == False else "Completed"
        print(f"{index}: {task["task"]} | {completed}")
    print()


def save_list(path="Task-Manager.json"):
    with open(path, "w") as file:
        json.dump(tasks, file, indent=4)


if os.path.exists("Task-Manager.json") and os.path.getsize("Task-Manager.json") > 0:
    with open("Task-Manager.json", "r") as file:
        tasks = json.load(file)
else:
    tasks = []

while True:
    print("=== Task Manager ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter the task description: ")
        task_data = {"task": task, "completed": False}
        tasks.append(task_data)
        save_list()
        print("Task added.\n")

    elif choice == "2":
        print_tasks()

    elif choice == "3":
        print_tasks()
        legal = False
        while legal == False:
            task_number = int(input("Choose task: "))
            if task_number < 1 or task_number > len(tasks):
                print("Illegal number.")
            else:
                legal = True
        tasks[task_number - 1]["completed"] = True
        save_list()
        print("Task Completed.\n")

    elif choice == "4":
        print_tasks()
        legal = False
        while legal == False:
            task_number = int(input("Choose task to delete: "))
            if task_number < 1 or task_number > len(tasks):
                print("Illegal number.")
            else:
                legal = True
        sure = input("Are you sure? (y/n) ")
        if sure == "y":
            del tasks[task_number - 1]
            save_list()
        print("Task Deleted.\n")

    elif choice == "5":
        break
