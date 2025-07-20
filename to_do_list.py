import json
import os

FILE_NAME = "todo_list.json"

def load_tasks():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks, category=None, completed=None):
    filtered = [
        task for task in tasks
        if (category is None or task["category"].lower() == category.lower()) and
           (completed is None or task["completed"] == completed)
    ]

    if not filtered:
        print("No tasks to display.")
        return

    for idx, task in enumerate(filtered, start=1):
        status = "✔ Done" if task["completed"] else "❌ Not Done"
        print(f"{idx}. {task['title']} [{task['category']}] - {status}")

def add_task(tasks):
    title = input("Enter task title: ").strip()
    category = input("Enter category (e.g., Work, Personal): ").strip()
    tasks.append({"title": title, "category": category, "completed": False})
    print("Task added!")

def mark_completed(tasks):
    display_tasks(tasks, completed=False)
    try:
        index = int(input("Enter the number of the task to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def filter_by_category(tasks):
    category = input("Enter category to filter by: ").strip()
    display_tasks(tasks, category=category)

def main():
    tasks = load_tasks()

    while True:
        print("\n------ To-Do List Menu ------")
        print("1. View All Tasks")
        print("2. View Completed Tasks")
        print("3. View Incomplete Tasks")
        print("4. Add Task")
        print("5. Mark Task as Completed")
        print("6. Remove Task")
        print("7. Filter Tasks by Category")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            display_tasks(tasks, completed=True)
        elif choice == "3":
            display_tasks(tasks, completed=False)
        elif choice == "4":
            add_task(tasks)
        elif choice == "5":
            mark_completed(tasks)
        elif choice == "6":
            remove_task(tasks)
        elif choice == "7":
            filter_by_category(tasks)
        elif choice == "8":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
