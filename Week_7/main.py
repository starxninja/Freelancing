from ui import CommandLineUI
from controllers import TaskManagerController

def main():
    controller = TaskManagerController()
    ui = CommandLineUI(controller)
    ui.run()

if __name__ == "__main__":
    main()