from datetime import datetime

class Task:
    def __init__(self, title: str, date_due: datetime = None, completed: bool = False, date_created: datetime = None):
        self.title = title
        self.date_due = date_due
        self.completed = completed
        self.date_created = date_created or datetime.now()

    def __str__(self):
        return f"{self.title} (Due: {self.date_due.strftime('%Y-%m-%d') if self.date_due else 'No due date'}, Completed: {self.completed})"

class RecurringTask(Task):
    def __init__(self, title: str, date_due: datetime = None, completed: bool = False, interval: int = None, completed_dates: list = None, date_created: datetime = None):
        super().__init__(title, date_due, completed, date_created)
        self.interval = interval
        self.completed_dates = completed_dates or []

    def __str__(self):
        return f"{self.title} (Due: {self.date_due.strftime('%Y-%m-%d') if self.date_due else 'No due date'}, Completed: {self.completed}, Interval: {self.interval}, Completed Dates: {self.completed_dates})"