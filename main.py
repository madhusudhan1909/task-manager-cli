import json
import os

TASK_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task():
    task = input("Enter a new task: ")
    tasks = load_tasks()
    tasks.append({"title": task, "done": False})
    save_tasks(tasks)
    print(f"Task added: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"

        print(f"{idx}. {task['title']} - {status}")

def mark_task_done():
    tasks = load_tasks()
    list_tasks()
    try:
        task_no = int(input("Enter task number to mark as done: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]['done'] = True
            save_tasks(tasks)
            print(f"Marked as done: {tasks[task_no - 1]['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

