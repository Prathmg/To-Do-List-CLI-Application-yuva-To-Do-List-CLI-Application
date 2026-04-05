import json
import os

class TaskManager:
    def __init__(self):
        self.file = "data.json"
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                return json.load(f)
        return []

    def save_tasks(self):
        with open(self.file, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task):
        if task.strip() == "":
            print("Task cannot be empty!")
            return
        self.tasks.append({"task": task, "done": False})
        print("Task added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for i, t in enumerate(self.tasks, start=1):
            status = "✔" if t["done"] else "✘"
            print(f"{i}. [{status}] {t['task']}")

    def delete_task(self, index):
        try:
            index = int(index) - 1
            removed = self.tasks.pop(index)
            print(f"Deleted: {removed['task']}")
        except:
            print("Invalid task number!")

    def mark_complete(self, index):
        try:
            index = int(index) - 1
            self.tasks[index]["done"] = True
            print("Task marked as completed!")
        except:
            print("Invalid task number!")