import csv
from datetime import datetime
from task import Task, RecurringTask

class TaskTestDAO:
    def __init__(self, storage_path: str):
        self.storage_path = storage_path

    def get_all_tasks(self) -> list:
        task_list = [
            Task("Buy groceries", datetime.strptime("2023-10-20", "%Y-%m-%d"), False),
            RecurringTask("Water plants", datetime.strptime("2023-10-21", "%Y-%m-%d"), False, 7, []),
            Task("Finish homework", datetime.strptime("2023-10-22", "%Y-%m-%d"), True)
        ]
        return task_list

    def save_all_tasks(self, tasks: list) -> None:
        pass  # Simulate saving, no actual file operations

class TaskCSVDAO:
    def __init__(self, storage_path: str):
        self.storage_path = storage_path
        self.fieldnames = ["title", "type", "date_due", "completed", "interval", "completed_dates", "date_created"]

    def get_all_tasks(self) -> list:
        tasks = []
        with open(self.storage_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                task_type = row["type"]
                task_title = row["title"]
                task_date_due = datetime.strptime(row["date_due"], "%Y-%m-%d") if row["date_due"] else None
                task_completed = row["completed"] == "True"
                task_interval = int(row["interval"].split()[0]) if row["interval"] else None
                task_date_created = datetime.strptime(row["date_created"], "%Y-%m-%d") if row["date_created"] else None
                task_completed_dates = [datetime.strptime(date, "%Y-%m-%d") for date in row["completed_dates"].split(";")] if row["completed_dates"] else []
                if task_type == "RecurringTask":
                    task = RecurringTask(task_title, task_date_due, task_completed, task_interval, task_completed_dates, task_date_created)
                else:
                    task = Task(task_title, task_date_due, task_completed, task_date_created)
                tasks.append(task)
        return tasks

    def save_all_tasks(self, tasks: list) -> None:
        with open(self.storage_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for task in tasks:
                row = {
                    "title": task.title,
                    "type": "RecurringTask" if isinstance(task, RecurringTask) else "Task",
                    "date_due": task.date_due.strftime("%Y-%m-%d") if task.date_due else "",
                    "completed": str(task.completed),
                    "interval": str(task.interval) if hasattr(task, "interval") else "",
                    "completed_dates": ";".join([date.strftime("%Y-%m-%d") for date in task.completed_dates]) if hasattr(task, "completed_dates") else "",
                    "date_created": task.date_created.strftime("%Y-%m-%d") if task.date_created else ""
                }
                writer.writerow(row)