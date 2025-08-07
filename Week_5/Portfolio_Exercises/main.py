import datetime
from users import Owner
from tasks import Task, RecurringTask, TaskList

def main():
    """Main entry point for the ToDo application with Owner support."""
    print("=== ToDo App Initialization ===")
    name = input("Enter owner name: ")
    email = input("Enter owner email: ")
    owner = Owner(name, email)
    task_list = TaskList(owner)
    
    print(f"\nWelcome, {owner}!")
    
    while True:
        print("\n===== ToDo App Menu =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. View Overdue Tasks")
        print("5. Mark Task as Completed")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            title = input("Enter task title: ")
            due_date_str = input("Enter due date (YYYY-MM-DD): ")
            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d")
            
            task_type = input("Is this a recurring task? (y/n): ").lower()
            if task_type == "y":
                interval_days = int(input("Enter recurrence interval in days: "))
                interval = datetime.timedelta(days=interval_days)
                task = RecurringTask(title, due_date, interval)
            else:
                description = input("Enter task description (optional): ")
                task = Task(title, due_date, description)
            
            task_list.add_task(task)
            print("Task added successfully!")
        
        elif choice == "2":
            task_list.view_tasks()
            if task_list.tasks:
                try:
                    task_num = int(input("Enter task number to remove: ")) - 1
                    task_list.remove_task(task_num)
                    print("Task removed successfully!")
                except (ValueError, IndexError):
                    print("Invalid task number!")
        
        elif choice == "3":
            task_list.view_tasks()
        
        elif choice == "4":
            task_list.view_overdue_tasks()
        
        elif choice == "5":
            task_list.view_tasks()
            if task_list.tasks:
                try:
                    task_num = int(input("Enter task number to mark as completed: ")) - 1
                    task = task_list.get_task(task_num)
                    task.mark_completed()
                    print("Task marked as completed!")
                except (ValueError, IndexError):
                    print("Invalid task number!")
        
        elif choice == "6":
            print(f"Goodbye, {owner.name}!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()