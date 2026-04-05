from task_manager import TaskManager
from utils import get_valid_input

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def main():
    manager = TaskManager()

    while True:
        show_menu()
        choice = get_valid_input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            manager.add_task(task)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            index = input("Enter task number to delete: ")
            manager.delete_task(index)

        elif choice == "4":
            index = input("Enter task number to mark complete: ")
            manager.mark_complete(index)

        elif choice == "5":
            manager.save_tasks()
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()