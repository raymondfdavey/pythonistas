"""A simple To-Do list application."""

import os
from datetime import date


class ToDoList:
    """A simple To-Do list application."""

    def __init__(self, directory="todo", filename=None):
        """Initialize the ToDoList instance."""
        assert isinstance(directory, str)
        # Make the directory. You need to use exist_ok=True to avoid an error
        os.makedirs(directory, exist_ok=True)
        # If no filename is given, use today's date with the .txt extension
        # Hint: use the os.path.join function to join the directory and filename
        if filename:
            self.filename = os.path.join(directory, filename)
        else:
            self.filename = os.path.join(directory, f"{date.today()}.txt")
        # Create the file and warn the user if it already exists
        if os.path.exists(self.filename):
            print(f"Warning: Overwriting {self.filename}!")
        self.create_file()

    def create_file(self):
        """Create the file if it doesn't exist."""
        with open(self.filename, mode="w", encoding="utf-8") as f:
            pass

    def get_tasks(self):
        """Read the file and return the list of tasks."""
        with open(self.filename, mode="r", encoding="utf-8") as f:
            tasks = f.readlines()
        return tasks

    def strip_tasks(self, tasks):
        """Strip the tasks of numbers and whitespace."""
        # Hint: use a list comprehension to strip each task
        # Hint: split and strip are useful string methods here...
        # Hint: you can chain methods together, e.g. "hello".upper().strip()
        tasks = [task.split(': ')[1].strip() for task in tasks]
        return tasks

    def add_task(self, task):
        """Add a task to the list. 
        Each task is numbered sequentially, starting from 1 with a colon and 
        a space following it before the task description."""
        # Hint: you can use the len function to get the number of tasks
        n_tasks = len(self.get_tasks())
        with open(self.filename, 'a', encoding="utf-8") as f:
            f.write(f"{n_tasks + 1}: {str(task)}\n")

    def remove_task(self, task):
        """Remove a task from the list."""
        # Hint: you can use the strip_tasks method to get a list of tasks
        # without numbers and whitespace
        tasks = self.get_tasks()
        tasks = self.strip_tasks(tasks)
        # Remove the task from the list
        tasks.remove(task)
        # Add the numbers back to the tasks
        tasks = [f"{i + 1}: {task}\n" for i, task in enumerate(tasks)]
        # Write the tasks back to the file
        with open(self.filename, 'w', encoding="utf-8") as f:
            f.writelines(tasks)

    def print_tasks(self):
        """Print the tasks in the list."""
        # Hint: remember to add some formatting to make it look nice!
        tasks = self.get_tasks()
        print(f"\nTo-Do list: {self.filename} ({len(self.get_tasks())} tasks)")
        print("=" * 20)
        print(''.join(tasks))
        print("-" * 20)

    
def main():
    """Create a ToDoList and run the program."""
    todo = ToDoList()
    todo.add_task("Feed the dog")
    todo.add_task("Buy milk")
    todo.add_task("Water the plants")
    todo.print_tasks()
    todo.remove_task("Buy milk")
    todo.add_task("Call mum")
    todo.add_task("Finish Python assignment")
    todo.print_tasks()

if __name__ == "__main__":
    main()
