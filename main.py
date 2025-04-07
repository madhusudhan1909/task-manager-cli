import json

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Task added: {title}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{idx}. {task['title']} - {status}")

if __name__ == "__main__":
    print("1. Add Task")
    print("2. List Tasks")
    choice = input("Choose an option: ")
    if choice == "1":
        title = input("Enter a new task: ")
        add_task(title)
    elif choice == "2":
        list_tasks()

