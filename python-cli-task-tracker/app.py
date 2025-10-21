import json
import sys
from pathlib import Path

DATA = Path("tasks.json")

def load():
    if DATA.exists():
        return json.loads(DATA.read_text())
    return []

def save(tasks):
    DATA.write_text(json.dumps(tasks, indent=2))

def add_task(title):
    tasks = load()
    tasks.append({"title": title, "done": False})
    save(tasks)
    print(f"Added: {title}")

def list_tasks():
    tasks = load()
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✓" if t["done"] else " "
        print(f"{i}. [{status}] {t['title']}")

def mark_done(index):
    tasks = load()
    if 1 <= index <= len(tasks):
        tasks[index-1]["done"] = True
        save(tasks)
        print(f"Completed: {tasks[index-1]['title']}")
    else:
        print("Invalid task number.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py [add|list|done] ...")
        return
    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) >= 3:
        add_task(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_tasks()
    elif cmd == "done" and len(sys.argv) == 3:
        try:
            idx = int(sys.argv[2])
            mark_done(idx)
        except ValueError:
            print("Provide a number for 'done'.")
    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()