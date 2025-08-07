from abc import ABC, abstractmethod
from datetime import datetime

class AbstractTask(ABC):
    def __init__(self, title: str, date_due: datetime = None, completed: bool = False, date_created: datetime = None):
        self.title = title
        self.date_due = date_due
        self.completed = completed
        self.date_created = date_created or datetime.now()

    @abstractmethod
    def mark_completed(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Task(AbstractTask):
    def mark_completed(self):
        self.completed = True

    def change_date_due(self, new_date: datetime):
        self.date_due = new_date

    def __str__(self):
        return f"{self.title} (Due: {self.date_due.strftime('%Y-%m-%d') if self.date_due else 'No due date'}, Completed: {self.completed})"

class RecurringTask(AbstractTask):
    def __init__(self, title: str, date_due: datetime = None, completed: bool = False, interval: int = None, completed_dates: list = None, date_created: datetime = None):
        super().__init__(title, date_due, completed, date_created)
        self.interval = interval
        self.completed_dates = completed_dates or []

    def mark_completed(self):
        super().mark_completed()
        if self.interval:
            self.completed_dates.append(datetime.now())
            self.date_due = self.date_due + datetime.timedelta(days=self.interval) if self.date_due else datetime.now() + datetime.timedelta(days=self.interval)
            self.completed = False

    def __str__(self):
        return f"{self.title} (Due: {self.date_due.strftime('%Y-%m-%d') if self.date_due else 'No due date'}, Completed: {self.completed}, Interval: {self.interval}, Completed Dates: {self.completed_dates})"

class PriorityTask(AbstractTask):
    PRIORITY_MAP = {1: "low", 2: "medium", 3: "high"}

    def __init__(self, title: str, date_due: datetime = None, completed: bool = False, priority: int = 1, date_created: datetime = None):
        super().__init__(title, date_due, completed, date_created)
        if not isinstance(priority, int) or priority not in self.PRIORITY_MAP:
            raise ValueError("Priority must be an integer between 1 and 3")
        self.priority = priority

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"{self.title} (Due: {self.date_due.strftime('%Y-%m-%d') if self.date_due else 'No due date'}, Completed: {self.completed}, Priority: {self.PRIORITY_MAP[self.priority]})"