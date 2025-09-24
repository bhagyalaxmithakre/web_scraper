todo_list = []

def show_menu():
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            status = "✔" if task['done'] else "✘"
            print(f"{i}. {task['title']} [{status}]")

def add_task():
    task_name = input("\nEnter the task: ")
    todo_list.append({"title": task_name, "done": False})
    print(f"Task '{task_name}' added successfully!")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number to remove: "))
        removed = todo_list.pop(task_num - 1)
        print(f"Task '{removed['title']}' removed successfully!")
    except (ValueError, IndexError):
        print("Invalid input. Please try again.")

def mark_completed():
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number to mark as completed: "))
        todo_list[task_num - 1]['done'] = True
        print(f"Task '{todo_list[task_num - 1]['title']}' marked as completed!")
    except (ValueError, IndexError):
        print("Invalid input. Please try again.")

while True:
    show_menu()
    choice = input("\nEnter your choice (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        mark_completed()
    elif choice == '5':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1-5.")
