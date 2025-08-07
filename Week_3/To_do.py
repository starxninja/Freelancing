# COMP11124 Object Oriented Programming - Week 3 To-Do List Manager

# Initialize an empty list to store tasks
user_tasks = []

# Function to add a task to the list
def add_new_task(task_description):
    user_tasks.append(task_description)
    print(f"Added new task: '{task_description}' to your to-do list!")

# Function to view current tasks in the list
def display_all_tasks():
    if not user_tasks:
        print("Your to-do list is currently empty.")
    else:
        print("Here are your current tasks:")
        for idx, task_item in enumerate(user_tasks, 1):
            print(f"Task {idx}: {task_item}")

# Function to remove a task from the list
def delete_task_by_index(task_number):
    if 1 <= task_number <= len(user_tasks):
        removed = user_tasks.pop(task_number - 1)
        print(f"Successfully removed: '{removed}' from your to-do list.")
    else:
        print("That task number is not valid. Please try again.")

# Main program loop
while True:
    print("\nPersonal To-Do List Manager")
    print("1. Add a new task")
    print("2. Show all tasks")
    print("3. Delete a task")
    print("4. Exit")
    
    user_choice = input("Select an option (1-4): ")
    
    if user_choice == "1":
        new_task = input("Describe the new task: ")
        add_new_task(new_task)
    elif user_choice == "2":
        display_all_tasks()
    elif user_choice == "3":
        display_all_tasks()
        try:
            task_to_remove = int(input("Enter the number of the task to delete: "))
            delete_task_by_index(task_to_remove)
        except ValueError:
            print("Please enter a valid task number.")
    elif user_choice == "4":
        print("Thank you for using your personal to-do list. Goodbye!")
        break
    else:
        print("Invalid selection. Please choose a valid option.")