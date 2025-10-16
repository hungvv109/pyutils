import pytest
from pyutils.todo_tool import handle_todo, load_todos

def test_add_todo(tmp_path, monkeypatch):
    monkeypatch.setattr('pyutils.todo_tool.TODO_FILE', tmp_path / 'test.json')
    handle_todo('add', 'Học Python')
    todos = load_todos()
    assert 'Học Python' in todos
