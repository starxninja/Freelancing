import datetime
from typing import List
from users import Owner

class Task:
    """Represents a single task in a to-do list."""
    
    def __init__(self, title: str, date_due: datetime.datetime, description: str = ""):
        """
        Initializes a Task.
        
        Args:
            title (str): Title of the task
            date_due (datetime.datetime): Due date
            description (str, optional): Task description. Defaults to "".
        """
        self.title = title
        self.completed = False
        self.date_created = datetime.datetime.now()
        self.date_due = date_due
        self.description = description
    
    def mark_completed(self) -> None:
        """Marks the task as completed."""
        self.completed = True
    
    def change_title(self, new_title: str) -> None:
        """Changes the task title."""
        self.title = new_title
    
    def change_date_due(self, date_due: datetime.datetime) -> None:
        """Changes the due date."""
        self.date_due = date_due
    
    def change_description(self, description: str) -> None:
        """Changes the description."""
        self.description = description
    
    def __str__(self) -> str:
        """String representation of the Task."""
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} - {status} (created: {self.date_created}, due: {self.date_due})"


class RecurringTask(Task):
    """Represents a recurring task that repeats at intervals."""
    
    def __init__(self, title: str, date_due: datetime.datetime, interval: datetime.timedelta):
        """
        Initializes a RecurringTask.
        
        Args:
            title (str): Title of the task
            date_due (datetime.datetime): Initial due date
            interval (datetime.timedelta): Time between recurrences
        """
        super().__init__(title, date_due)
        self.interval = interval
        self.completed_dates: List[datetime.datetime] = []
    
    def _compute_next_due_date(self) -> datetime.datetime:
        """Calculates the next due date based on the interval."""
        return self.date_due + self.interval
    
    def mark_completed(self) -> None:
        """
        Marks the task as completed and schedules the next occurrence.
        Overrides Task.mark_completed().
        """
        self.completed_dates.append(datetime.datetime.now())
        self.date_due = self._compute_next_due_date()
        self.completed = False  # Reset for next occurrence
    
    def __str__(self) -> str:
        """String representation including recurrence info."""
        base_str = super().__str__()
        return f"{base_str} - Recurring (interval: {self.interval}, completed dates: {len(self.completed_dates)})"


class TaskList:
    """Manages a collection of tasks owned by an Owner."""
    
    def __init__(self, owner: Owner):
        """
        Initializes a TaskList with an Owner.
        
        Args:
            owner (Owner): The owner of this task list
        """
        self.owner = owner
        self.tasks: List[Task] = []
    
    def add_task(self, task: Task) -> None:
        """Adds a task to the list."""
        self.tasks.append(task)
    
    def remove_task(self, index: int) -> None:
        """Removes a task at the specified index."""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
    
    def get_task(self, index: int) -> Task:
        """
        Retrieves a task by index.
        
        Args:
            index (int): The task index
            
        Returns:
            Task: The task at the specified index
            
        Raises:
            IndexError: If index is out of range
        """
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        raise IndexError("Task index out of range")
    
    def view_tasks(self) -> None:
        """Displays all tasks in the list."""
        if not self.tasks:
            print("No tasks in the list.")
            return
        print(f"\n{self.owner}'s Tasks:")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")
    
    def view_overdue_tasks(self) -> None:
        """Displays all overdue tasks."""
        now = datetime.datetime.now()
        overdue = [task for task in self.tasks 
                  if not task.completed and task.date_due < now]
        if not overdue:
            print("No overdue tasks.")
            return
        print(f"\n{self.owner}'s Overdue Tasks:")
        for i, task in enumerate(overdue):
            print(f"{i + 1}. {task}")