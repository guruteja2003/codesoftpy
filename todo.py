import argparse

tasks = []

def add_task(task):
  tasks.append(task)
  print(f"Task added: {task}")

def view_tasks():
  if tasks:
    print("Your tasks:")
    for i, task in enumerate(tasks):
      print(f"{i+1}. {task}")
  else:
    print("No tasks yet.")

def complete_task(task_index):
  try:
    task_index = int(task_index) - 1
    completed_task = tasks.pop(task_index)
    print(f"Task completed: {completed_task}")
  except IndexError:
    print("Invalid task index.")

def remove_task(task_index):
  try:
    task_index = int(task_index) - 1
    removed_task = tasks.pop(task_index)
    print(f"Task removed: {removed_task}")
  except IndexError:
    print("Invalid task index.")

# Parse command-line arguments
parser = argparse.ArgumentParser(description="To-Do List Application")
parser.add_argument("command", choices=["add", "view", "complete", "remove"])
parser.add_argument("task", nargs="?")
parser.add_argument("task_index", nargs="?", type=int)
args = parser.parse_args()

if args.command == "add":
  add_task(args.task)
elif args.command == "view":
  view_tasks()
elif args.command == "complete":
  complete_task(args.task_index)
elif args.command == "remove":
  remove_task(args.task_index)
else:
  print("Invalid command.")
