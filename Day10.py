#Write a Python program that allows the user to create multiple to-do lists (e.g., work tasks, 
#personal tasks) and manage tasks for each list. 

# Multi-List To-Do Application

todo_lists = {}

while True:
    print("\nOptions:")
    print("1. Create a new to-do list")
    print("2. Add task to a list")
    print("3. View tasks in a list")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        list_name = input("Enter the name of the new to-do list: ")
        todo_lists[list_name] = []
        print(f"List '{list_name}' created.")

    elif choice == "2":
        list_name = input("Enter the list name: ")
        if list_name in todo_lists:
            task = input("Enter a new task: ")
            todo_lists[list_name].append(task)
            print("Task added.")
        else:
            print(f"No list named '{list_name}'")

    elif choice == "3":
        list_name = input("Enter the list name: ")
        if list_name in todo_lists:
            print(f"Tasks in '{list_name}':")
            for i, task in enumerate(todo_lists[list_name], 1):
                print(f"{i}. {task}")
        else:
            print(f"No list named '{list_name}'")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid option. Try again.")


        