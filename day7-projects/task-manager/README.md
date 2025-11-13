# Project 1: CLI Task Manager

Build a command-line task management application with file persistence.

## Features
- Add, list, complete, delete tasks
- Priority levels (high, medium, low)
- Due dates
- JSON file storage
- Search and filter tasks

## Commands
```bash
python task_manager.py add "Buy groceries" --priority high --due 2025-11-20
python task_manager.py list
python task_manager.py complete 1
python task_manager.py delete 2
python task_manager.py search "groceries"
```

## Implementation
- Use argparse for CLI
- Task class with OOP
- JSON for persistence
- datetime for dates
- Filter/sort functionality

## Run
```bash
python src/task_manager.py --help
pytest tests/ -v
```
