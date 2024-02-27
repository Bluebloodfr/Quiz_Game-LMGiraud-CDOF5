def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip().split(';', 1) for line in file]
    except FileNotFoundError:
        return []

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for completed, task in tasks:
            file.write(f"{completed};{task}\n")

def add_task(tasks, task):
    tasks.append((False, task))

def remove_task(tasks, task_index):
    del tasks[task_index]

def mark_task_completed(tasks, task_index):
    tasks[task_index] = (True, tasks[task_index][1])

def print_tasks(tasks):
    if not tasks:
        print("No tasks")
    else:
        for index, (completed, task) in enumerate(tasks):
            status = 'X' if completed else ' '
            print(f"{index + 1}. [{status}] {task}")

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("\nTODO LIST")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == "2":
            print_tasks(tasks)
            task_index = int(input("Enter the task number to remove: ")) - 1
            remove_task(tasks, task_index)
        elif choice == "3":
            print_tasks(tasks)
        elif choice == "4":
            print_tasks(tasks)
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            mark_task_completed(tasks, task_index)
        elif choice == "5":
            save_tasks(filename, tasks)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
