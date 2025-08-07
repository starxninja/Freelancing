from task import Task, RecurringTask
from task_list import TaskList
from dao import TaskTestDAO, TaskCSVDAO
from datetime import datetime

def main():
    task_list = TaskList()
    while True:
        print("\nToDo App Menu:")
        print("[A]dd task, [V]iew uncompleted tasks, [L]oad tasks, [S]ave tasks, [Q]uit")
        action = input("What should I do? ").lower()
        if action == 'a':
            title = input("Enter task title: ")
            date_due = input("Enter due date (YYYY-MM-DD) or leave blank: ")
            date_due = datetime.strptime(date_due, "%Y-%m-%d") if date_due else None
            is_recurring = input("Is this a recurring task? (y/n): ").lower() == 'y'
            if is_recurring:
                interval = int(input("Enter interval (days): "))
                task = RecurringTask(title, date_due, False, interval)
            else:
                task = Task(title, date_due)
            task_list.add_task(task)
            print("Task added.")
        elif action == 'v':
            task_list.view_tasks()
        elif action == 'l':
            file_path = input("Enter file path to load tasks (e.g., tasks.csv): ")
            dao = TaskCSVDAO(file_path)  # Use TaskCSVDAO for CSV persistence
            tasks = dao.get_all_tasks()
            task_list.tasks = []  # Clear existing tasks
            for task in tasks:
                task_list.add_task(task)
            print("Tasks loaded.")
        elif action == 's':
            file_path = input("Enter file path to save tasks (e.g., tasks.csv): ")
            dao = TaskCSVDAO(file_path)
            dao.save_all_tasks(task_list.tasks)
            print("Tasks saved.")
        elif action == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()