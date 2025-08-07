# COMP11124 Object Oriented Programming - Week 4 Main Program
from task_list import TaskList
from task import Task
from datetime import datetime as dt

# Exercise 2 Start
# Introduction: This function demonstrates how to populate a TaskList with several sample tasks, each with a unique title and due date.
def propagate_task_list(task_collection: TaskList) -> TaskList:
    initial_tasks = [
        Task("Submit Report", dt(2025, 7, 25, 12, 0)),
        Task("Clean Garage", dt(2025, 7, 26, 15, 0)),
        Task("Order Supplies", dt(2025, 7, 27, 10, 0))
    ]
    for single_task in initial_tasks:
        task_collection.add_task(single_task)
    print("Exercise 3: Sample tasks added to the list.")
    return task_collection
# Exercise 2 End

# Exercise 3 Start
# Introduction: This is the main program loop for the To-Do List Manager. It allows the user to add, view, remove, complete, and edit tasks interactively.
def main() -> None:
    print("Exercise 1 Start: Creating TaskList")
    user_task_collection = TaskList("ALEX")
    user_task_collection = propagate_task_list(user_task_collection)
    while True:
        print("\nExercise 1: To-Do List Manager")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Change task title")
        print("6. Change task due date")
        print("7. Quit")
        menu_selection = input("Enter your choice: ")
        if menu_selection == "1":
            input_title = input("Enter the task title: ")
            input_due = input("Enter due date (YYYY-MM-DD HH:MM): ")
            try:
                parsed_due = dt.strptime(input_due, "%Y-%m-%d %H:%M")
                user_task_collection.add_task(Task(input_title, parsed_due))
            except ValueError:
                print("Exercise 1: Invalid date format. Use YYYY-MM-DD HH:MM.")
        elif menu_selection == "2":
            user_task_collection.view_tasks()
        elif menu_selection == "3":
            user_task_collection.view_tasks()
            try:
                idx_remove = int(input("Enter the task number to remove: ")) - 1
                user_task_collection.remove_task(idx_remove)
            except ValueError:
                print("Exercise 2: Please enter a valid number.")
        elif menu_selection == "4":
            user_task_collection.view_tasks()
            try:
                idx_complete = int(input("Enter the task number to mark as completed: ")) - 1
                if 0 <= idx_complete < len(user_task_collection.task_items):
                    user_task_collection.task_items[idx_complete].mark_completed()
                else:
                    print("Exercise 4: Invalid task number. Please try again.")
            except ValueError:
                print("Exercise 4: Please enter a valid number.")
        elif menu_selection == "5":
            user_task_collection.view_tasks()
            try:
                idx_title = int(input("Enter the task number to change title: ")) - 1
                if 0 <= idx_title < len(user_task_collection.task_items):
                    new_title_input = input("Enter the new task title: ")
                    user_task_collection.task_items[idx_title].change_title(new_title_input)
                else:
                    print("Exercise 4: Invalid task number. Please try again.")
            except ValueError:
                print("Exercise 4: Please enter a valid number.")
        elif menu_selection == "6":
            user_task_collection.view_tasks()
            try:
                idx_due = int(input("Enter the task number to change due date: ")) - 1
                if 0 <= idx_due < len(user_task_collection.task_items):
                    new_due_input = input("Enter new due date (YYYY-MM-DD HH:MM): ")
                    try:
                        parsed_new_due = dt.strptime(new_due_input, "%Y-%m-%d %H:%M")
                        user_task_collection.task_items[idx_due].change_due_date(parsed_new_due)
                    except ValueError:
                        print("Exercise 1 (Libraries): Invalid date format. Use YYYY-MM-DD HH:MM.")
                else:
                    print("Exercise 1 (Libraries): Invalid task number. Please try again.")
            except ValueError:
                print("Exercise 1 (Libraries): Please enter a valid number.")
        elif menu_selection == "7":
            print("Exercise 1 End: Goodbye!")
            break
        else:
            print("Exercise 1: Invalid choice. Please try again.")
# Exercise 3 End

if __name__ == "__main__":
    main()