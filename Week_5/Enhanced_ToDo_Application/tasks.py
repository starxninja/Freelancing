import datetime
from typing import List

class Task:
    """Represents a single task in a to-do list."""
    
    def __init__(self, title: str, date_due: datetime.datetime, description: str = ""):
        self.title = title
        self.completed = False
        self.date_created = datetime.datetime.now()
        self.date_due = date_due
        self.description = description
    
    def mark_completed(self) -> None:
        """Marks the task as completed."""
        self.completed = True
    
    def change_title(self, new_title: str) -> None:
        """Changes the title of the task."""
        self.title = new_title
    
    def change_date_due(self, date_due: datetime.datetime) -> None:
        """Changes the due date of the task."""
        self.date_due = date_due
    
    def change_description(self, description: str) -> None:
        """Changes the description of the task."""
        self.description = description
    
    def __str__(self) -> str:
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} - {status} (created: {self.date_created}, due: {self.date_due})"


class RecurringTask(Task):
    """Represents a recurring task that repeats at a given interval."""
    
    def __init__(self, title: str, date_due: datetime.datetime, interval: datetime.timedelta):
        super().__init__(title, date_due)
        self.interval = interval
        self.completed_dates: List[datetime.datetime] = []
    
    def _compute_next_due_date(self) -> datetime.datetime:
        """Computes the next due date based on the interval."""
        return self.date_due + self.interval
    
    def mark_completed(self) -> None:
        """Marks the task as completed and updates the next due date."""
        self.completed_dates.append(datetime.datetime.now())
        self.date_due = self._compute_next_due_date()
        self.completed = False  # Reset for next occurrence
    
    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str} - Recurring (interval: {self.interval}, completed dates: {len(self.completed_dates)})"


class TaskList:
    """Manages a list of tasks."""
    
    def __init__(self, owner: str):
        self.owner = owner
        self.tasks: List[Task] = []
    
    def add_task(self, task: Task) -> None:
        """Adds a task to the list."""
        self.tasks.append(task)
    
    def remove_task(self, index: int) -> None:
        """Removes a task at the given index."""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
    
    def get_task(self, index: int) -> Task:
        """Returns the task at the given index."""
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        raise IndexError("Task index out of range")
    
    def view_tasks(self) -> None:
        """Displays all tasks."""
        if not self.tasks:
            print("No tasks in the list.")
            return
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")
    
    def view_overdue_tasks(self) -> None:
        """Displays all overdue tasks."""
        now = datetime.datetime.now()
        overdue = [task for task in self.tasks if not task.completed and task.date_due < now]
        if not overdue:
            print("No overdue tasks.")
            return
        for i, task in enumerate(overdue):
            print(f"{i + 1}. {task}")