from controllers import TaskManagerController
from datetime import datetime

class CommandLineUI:
    def __init__(self, controller: TaskManagerController):
        self.controller = controller

    def _print_menu(self):
        print("\nToDo App Menu:")
        print("[A]dd task, [V]iew uncompleted tasks, [C]omplete task, [L]oad tasks, [S]ave tasks, [Q]uit")

    def run(self):
        while True:
            self._print_menu()
            action = input("What should I do? ").lower()
            try:
                if action == 'a':
                    title = input("Enter task title: ")
                    date_due = input("Enter due date (YYYY-MM-DD) or leave blank: ")
                    date_due = datetime.strptime(date_due, "%Y-%m-%d") if date_due else None
                    task_type = input("Task type ([S]tandard, [R]ecurring, [P]riority): ").lower()
                    interval = None
                    priority = None
                    if task_type == 'r':
                        interval = int(input("Enter interval (days): "))
                    elif task_type == 'p':
                        priority = int(input("Enter priority (1=low, 2=medium, 3=high): "))
                    self.controller.add_task(title, date_due, interval, priority)
                    print("Task added.")
                elif action == 'v':
                    print(self.controller.view_uncompleted_tasks())
                elif action == 'c':
                    index = int(input("Enter task index to complete: "))
                    self.controller.complete_task(index)
                    print("Task completed.")
                elif action == 'l':
                    file_path = input("Enter file path to load tasks (e.g., tasks.csv): ")
                    self.controller.load_tasks(file_path)
                    print("Tasks loaded.")
                elif action == 's':
                    file_path = input("Enter file path to save tasks (e.g., tasks.csv): ")
                    self.controller.save_tasks(file_path)
                    print("Tasks saved.")
                elif action == 'q':
                    print("Exiting...")
                    break
                else:
                    print("Invalid option, try again.")
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
            except IndexError as e:
                print(f"Error: {e}. Please try again.")
            except FileNotFoundError as e:
                print(f"Error: {e}. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")