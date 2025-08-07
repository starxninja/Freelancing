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
            return "No uncompleted tasks."
        result = ["The following tasks are still to be done:"]
        for task in self.uncompleted_tasks:
            result.append(f"Task: {task}")
        return "\n".join(result)

    def check_task_index(self, ix: int) -> bool:
        return 0 <= ix < len(self.tasks)

    def get_task(self, ix: int):
        if not self.check_task_index(ix):
            raise IndexError("Task index does not exist.")
        return self.tasks[ix]