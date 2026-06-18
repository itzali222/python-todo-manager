#              Your Project is Todo app/list

tasks = []   # empty list

def menu_system():
    while True:
        print("\n1. add task")
        print("2.show task")
        print("3.deleted task")
        print("4.repeat task")
        print("5.schedule")
        print("6.complete task")
        print("7.edit task")
        print("8.search task")
        print("9.read task")
        print("10.write task")
        print("11.task by date")
        print("12.colorama")
        print("13.save task")
        print("14.load task")
        print("15.exit")

        try:
            choice = int(input("Select your option:"))
        except:
            print("Invalid input")
            continue

        if choice == 1:
            add_task()

        elif choice == 2:
            show_task()

        elif choice == 3:
            deleted_task()

        elif choice == 4:
            repeat_task()

        elif choice == 5:
            day = input("Enter your day: ")
            schedule_task(day)

        elif choice == 6:
            complete_task()

        elif choice == 7:
            edit_task()

        elif choice == 8:
            search_task()

        elif choice == 9:
            read_task()

        elif choice == 10:
            write_task()

        elif choice == 11:
            task_by_date()

        elif choice == 12:
            colorama()

        elif choice == 13:
            save_tasks()

        elif choice == 14:
            load_tasks()

        elif choice == 15:
            print("Good Bye")
            break

        else:
            print("Invalid choice")


def add_task():
    task = input("Enter your task: ")
    priority = input("Enter your priority (high/low): ")

    tasks.append({
        "task": task,
        "done": False,
        "priority": priority,
        "day": "Monday"
    })

    print("Task added successfully")


def show_task():
    if not tasks:
        print("No data Available")

    else:
        for i, t in enumerate(tasks, 1):

            status = "Done" if t["done"] else "Pending"

            print(
                f"{i}. {t['task']} | "
                f"Status: {status} | "
                f"Priority: {t['priority']} | "
                f"Day: {t['day']}"
            )


def deleted_task():
    show_task()

    try:
        num = int(input("Enter a number of deleted task: "))

        if 0 < num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted")

        else:
            print("Invalid task number")

    except:
        print("Invalid input")


def repeat_task():
    task = input("Enter task to repeat: ")

    try:
        times = int(input("How many times: "))

        for i in range(times):
            print(task)

    except:
        print("Invalid input")


def schedule_task(day):

    schedule = {
        "Monday": ["Python", "Gym"],
        "Tuesday": ["ML", "Project"],
        "Wednesday": ["Deep Learning"],
        "Thursday": ["Maths"],
        "Friday": ["LLM"],
        "Saturday": ["Revision"],
        "Sunday": ["Games"]
    }

    if day in schedule:
        print(f"Your tasks for {day} are:")
        print(schedule[day])

    else:
        print("No Schedule")


def complete_task():
    show_task()

    try:
        num = int(input("Enter task number: "))

        if 0 < num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("Task completed")

        else:
            print("Invalid task number")

    except:
        print("Invalid input")


def edit_task():
    show_task()

    try:
        num = int(input("Enter task number: "))

        if 0 < num <= len(tasks):

            new_text = input("Enter new task: ")
            tasks[num - 1]["task"] = new_text

            print("Task updated")

        else:
            print("Invalid task number")

    except:
        print("Invalid input")


def search_task():

    keyword = input("Search task: ")

    found = False

    for t in tasks:

        if keyword.lower() in t["task"].lower():
            print(t)
            found = True

    if not found:
        print("Task not found")


def write_task():

    text = input("Enter text: ")

    with open("myfile.txt", "a") as f:
        f.write(text + "\n")


def read_task():

    with open("myfile.txt", "r") as f:
        text = f.read()

    print(text)


def task_by_date():
    date = input("Enter the date (dd-mm-yyyy):")
    if date == "23-4-26":
        print("Your date is correct")
    else:
        print("Your date is wrong")


from colorama import Fore, init

init()


def colorama():

    status = input("Enter status (done/pending): ")

    if status.lower() == "done":
        print(Fore.GREEN + "Task Completed")

    else:
        print(Fore.RED + "Task Pending")

import json

def save_tasks():

    with open("tasks.json", "w") as f:
        json.dump(tasks, f)


def load_tasks():

    global tasks

    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)

    except:
        tasks = []



# Calling Function

# menu_system()
# deleted_task()
# show_task()
# completed_task()
# edit_task()
# search_task()
# schedule_task()
# add_task()
# repeat_task()
# read_task()
# write_task()
# colorama()
# save_tasks()
# load_tasks()
# task_by_date()