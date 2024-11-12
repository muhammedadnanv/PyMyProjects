import os

class TodoApp:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from a file."""
        if os.path.exists('tasks.txt'):
            with open('tasks.txt', 'r') as file:
                self.tasks = [line.strip() for line in file.readlines()]

    def save_tasks(self):
        """Save tasks to a file."""
        with open('tasks.txt', 'w') as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def display_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks to show.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def add_task(self, task):
        """Add a new task."""
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_num):
        """Remove a task by its number."""
        if 1 <= task_num <= len(self.tasks):
            removed_task = self.tasks.pop(task_num - 1)
            self.save_tasks()
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")

    def run(self):
        """Run the app."""
        print("Welcome to the Todo App!")
        while True:
            print("\nChoose an option:")
            print("1. View tasks")
            print("2. Add a task")
            print("3. Remove a task")
            print("4. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                self.display_tasks()
            elif choice == '2':
                task = input("Enter the task: ")
                self.add_task(task)
                print(f"Task added: {task}")
            elif choice == '3':
                self.display_tasks()
                task_num = int(input("Enter task number to remove: "))
                self.remove_task(task_num)
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = TodoApp()
    app.run()
