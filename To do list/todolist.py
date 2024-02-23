###Program Name: todolist.py
###Programmer: Aaliyah Raderberg
###Project: Python To-do List

##This script provides a menu-driven interface where users can add, edit, delete, search, sort,
##and display tasks. Each task has a name, category, deadline, and reminder.
##The tasks are stored in a list within the TaskManager class, and the script utilizes datetime
##module to handle dates and times.


import datetime

class Task:
    def __init__(self, name, category, deadline=None, reminder=None):
        self.name = name
        self.category = category
        self.deadline = deadline
        self.reminder = reminder

    def __str__(self):
        task_info = f"Name: {self.name}\nCategory: {self.category}\n"
        if self.deadline:
            task_info += f"Deadline: {self.deadline.strftime('%Y-%m-%d')}\n"
        if self.reminder:
            task_info += f"Reminder: {self.reminder.strftime('%Y-%m-%d')}\n"
        return task_info

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def edit_task(self, index, task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = task
            print("Task edited successfully.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

    def search_task(self, keyword):
        found_tasks = []
        for task in self.tasks:
            if keyword.lower() in task.name.lower() or keyword.lower() in task.category.lower():
                found_tasks.append(task)
        return found_tasks

    def sort_tasks_by_deadline(self):
        self.tasks.sort(key=lambda x: x.deadline if x.deadline else datetime.datetime.max)
        print("Tasks sorted by deadline.")

    def display_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"\nTask {i}:\n{task}")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Search Task")
        print("5. Sort Tasks by Deadline")
        print("6. Display Tasks")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter task name: ")
            category = input("Enter task category: ")
            deadline_str = input("Enter deadline (YYYY-MM-DD ) or leave blank: ")
            deadline = datetime.datetime.strptime(deadline_str, "%Y-%m-%d") if deadline_str else None
            reminder_str = input("Enter reminder (YYYY-MM-DD ) or leave blank: ")
            reminder = datetime.datetime.strptime(reminder_str, "%Y-%m-%d") if reminder_str else None
            task = Task(name, category, deadline, reminder)
            task_manager.add_task(task)
        elif choice == '2':
            index = int(input("Enter the index of the task to edit: ")) - 1
            task = task_manager.tasks[index] if 0 <= index < len(task_manager.tasks) else None
            if task:
                name = input("Enter new task name: ")
                category = input("Enter new task category: ")
                deadline_str = input("Enter new deadline (YYYY-MM-DD ) or leave blank: ")
                deadline = datetime.datetime.strptime(deadline_str, "%Y-%m-%d") if deadline_str else None
                reminder_str = input("Enter new reminder (YYYY-MM-DD ) or leave blank: ")
                reminder = datetime.datetime.strptime(reminder_str, "%Y-%m-%d")  if reminder_str else None
                edited_task = Task(name, category, deadline, reminder)
                task_manager.edit_task(index, edited_task)
            else:
                print("Invalid task index.")
        elif choice == '3':
            index = int(input("Enter the index of the task to delete: ")) - 1
            task_manager.delete_task(index)
        elif choice == '4':
            keyword = input("Enter keyword to search for: ")
            found_tasks = task_manager.search_task(keyword)
            print("\nFound Tasks:")
            for i, task in enumerate(found_tasks, 1):
                print(f"\nTask {i}:\n{task}")
        elif choice == '5':
            task_manager.sort_tasks_by_deadline()
        elif choice == '6':
            task_manager.display_tasks()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
