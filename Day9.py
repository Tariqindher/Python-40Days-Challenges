#Data Structures
#List with Loops

numbers = [1,2,3,4,5,6,8]
print(numbers)
for i in numbers:
      print(i, end=" ")


for i in range(6,10):
    numbers.append(i)

print(numbers)
print()
numbers.remove(1)
print(numbers)
print(f'first item of List: {numbers[0]}')
print(f'Last item of List: {numbers[-1]}')
print("First 5 Number print")
print(numbers[:5])


if 5 in numbers:
       print("5 is in the list")
else: 
       print("5 is not in the list")

print("Reverse the List")

numbers.reverse()
print(f'Reversed the List: {numbers}')
print(f'The length of the list is:   {len(numbers)}')

print(f'The Total count Number 2 appear times :{numbers.count(2) }')

nested_list = [[1,2], [2,3],[4,5]]
for sublist in nested_list:
     print(sublist , end = " ")


#*To-Do List Program with Multiple Tasks*

print()


# To-Do List Program

todo_list = []

while True:
    print('\nOptions:')
    print('1. Add task')
    print('2. View tasks')
    print('3. Mark task as completed')
    print('4. Remove completed tasks')
    print('5. Exit')

    choice = input('Choose an option: ')

    if choice == '1':
        task = input('Enter a new task: ')
        todo_list.append({'task': task, 'completed': False})

    elif choice == '2':
        if not todo_list:
            print("No tasks available.")
        else:
            for i, task in enumerate(todo_list):
                status = 'Done' if task['completed'] else 'Not Done'
                print(f'{i + 1}. {task["task"]} - {status}')

    elif choice == '3':
        task_number = int(input('Enter task number to mark as completed: ')) - 1
        if 0 <= task_number < len(todo_list):
            todo_list[task_number]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    elif choice == '4':
        todo_list = [task for task in todo_list if not task['completed']]
        print("Completed tasks removed.")

    elif choice == '5':
        print("Exiting program...")
        break

    else:
        print("Invalid option. Try again.")






     