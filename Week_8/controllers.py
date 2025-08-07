from datetime import datetime
from task import Task, RecurringTask, PriorityTask
from task_list import TaskList
from dao import TaskTestDAO, TaskCSVDAO

class TaskFactory:
    @staticmethod
    def create_task(title: str, date_due: datetime = None, interval: int = None, priority: int = None):
        if interval is not None:
            return RecurringTask(title, date_due, False, interval)
        elif priority is not None:
            return PriorityTask(title, date_due, False, priority)
        return Task(title, date_due)

class TaskManagerController:
    def __init__(self):
        self.task_list = TaskList()
        self.dao = None

    def add_task(self, title: str, date_due: datetime = None, interval: int = None, priority: int = None):
        task = TaskFactory.create_task(title, date_due, interval, priority)
        self.task_list.add_task(task)

    def view_uncompleted_tasks(self) -> str:
        return self.task_list.view_tasks()

    def complete_task(self, index: int):
        task = self.task_list.get_task(index)
        task.mark_completed()

    def load_tasks(self, file_path: str):
        self.dao = TaskCSVDAO(file_path)
        tasks = self.dao.get_all_tasks()
        self.task_list.tasks = []  # Clear existing tasks
        for task in tasks:
            self.task_list.add_task(task)

    def save_tasks(self, file_path: str):
        self.dao = TaskCSVDAO(file_path)
        self.dao.save_all_tasks(self.task_list.tasks)