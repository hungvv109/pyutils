import json
from pathlib import Path

TODO_FILE = Path.home() / '.pyutils_todo.json'

def load_todos():
    if TODO_FILE.exists():
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=2)

def handle_todo(action, item=None):
    todos = load_todos()

    if action == 'add' and item:
        todos.append(item)
        save_todos(todos)
        print(f"✅ Added: {item}")
    elif action == 'list':
        print("📋 To-do list:")
        for i, todo in enumerate(todos, 1):
            print(f"{i}. {todo}")
    elif action == 'remove' and item:
        if item in todos:
            todos.remove(item)
            save_todos(todos)
            print(f"🗑️ Removed: {item}")
        else:
            print(f"❌ '{item}' not found.")
