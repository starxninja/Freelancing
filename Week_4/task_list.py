# COMP11124 Object Oriented Programming - Week 4 TaskList Class
# Exercise 1 Start
# Introduction: This class manages a collection of Task objects for a specific user, providing methods to add, remove, and display tasks.
from task import Task

class TaskList:
    def __init__(self, owner_identifier: str) -> None:
        self.owner_identifier: str = owner_identifier.upper()
        self.task_collection: list[Task] = []

    def add_task(self, task_to_add: Task) -> None:
        self.task_collection.append(task_to_add)
        print(f"Exercise 2: Task '{task_to_add.unique_title}' added successfully!")

    def remove_task(self, index_to_remove: int) -> None:
        if 0 <= index_to_remove < len(self.task_collection):
            removed_task = self.task_collection.pop(index_to_remove)
            print(f"Exercise 2: Task '{removed_task.unique_title}' removed successfully!")
        else:
            print("Exercise 2: Invalid task index. Please try again.")

    def view_tasks(self) -> None:
        if not self.task_collection:
            print("Exercise 2: No tasks in the list.")
        else:
            print(f"\nExercise 2: {self.owner_identifier}'s Task List:")
            for idx, task in enumerate(self.task_collection, 1):
                print(f"{idx}. {task}")
# Exercise 1 End