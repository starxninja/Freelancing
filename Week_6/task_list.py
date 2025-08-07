class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    @property
    def uncompleted_tasks(self) -> list:
        return [task for task in self.tasks if not task.completed]

    def view_tasks(self):
        if not self.uncompleted_tasks:
            print("No uncompleted tasks.")
        else:
            print("The following tasks are still to be done:")
            for task in self.uncompleted_tasks:
                print(f"Task: {task}")