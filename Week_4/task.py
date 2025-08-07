# COMP11124 Object Oriented Programming - Week 4 Task Class
# Exercise 1 Start
# Introduction: This class models a single to-do item, including its title, completion status, creation time, and due date.
import datetime
from datetime import datetime as dt

class Task:
    def __init__(self, unique_title: str, deadline: dt) -> None:
        self.unique_title: str = unique_title
        self.is_done: bool = False
        self.created_time: dt = datetime.datetime.now()
        self.deadline: dt = deadline

    def __str__(self) -> str:
        status = "Completed" if self.is_done else "Not Completed"
        return f"Task: {self.unique_title}, Status: {status}, Created: {self.created_time.strftime('%Y-%m-%d %H:%M')}, Due: {self.deadline.strftime('%Y-%m-%d %H:%M')}"

    def mark_completed(self) -> None:
        self.is_done = True
        print(f"Exercise 4: Task '{self.unique_title}' marked as completed!")

    def change_title(self, updated_title: str) -> None:
        self.unique_title = updated_title
        print(f"Exercise 4: Task title changed to '{updated_title}'!")

    def change_due_date(self, updated_deadline: dt) -> None:
        self.deadline = updated_deadline
        print(f"Exercise 1 (Libraries): Due date for '{self.unique_title}' changed!")
# Exercise 1 End