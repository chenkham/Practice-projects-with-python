task_list = []

def Add_task():
    enter_task = input("Enter task: ").strip()
    if enter_task != "":
        task_list.append(enter_task)
    else:
        print("Task cannot be empty.")


def Remove_Task():
    if task_list:
        try:
            task_rem = int(input("Enter task index to remove: "))
            remove_task = task_list.pop(task_rem-1)
            print(f"Task '{remove_task}' removed successfully.")
        except IndexError:
            print("Invalid index!.")
        except ValueError:
            print("Please enter a valid index.")
    else:
        print("Task list is empty.")
def Show_Task():
    if task_list:
        print("\nTask list:")
        for number, task in enumerate(task_list, 1):
            print(f"{number}. {task}")
    else:
        print("No tasks available to show.")

while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Show Task")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        Add_task()
    elif choice == 2:
        Remove_Task()
    elif choice == 3:
        Show_Task()
    elif choice == 4:
        print("Exiting To-Do list.")
        break
    else:
        print("Invalid choice! Please select an option from 1 to 4.")
