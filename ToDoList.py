class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully!\n")

    def view_tasks(self):
        print("\nTo-Do List:")
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def update_task(self, index, new_task):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] = new_task
            print(f"Task updated successfully!\n")
        else:
            print("Invalid task index. Please enter a valid index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            deleted_task = self.tasks.pop(index - 1)
            print(f"Task '{deleted_task}' deleted successfully!\n")
        else:
            print("Invalid task index. Please enter a valid index.")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter task: ")
            to_do_list.add_task(task)

        elif choice == '2':
            to_do_list.view_tasks()

        elif choice == '3':
            index = int(input("Enter the index of the task to update: "))
            new_task = input("Enter the new task: ")
            to_do_list.update_task(index, new_task)

        elif choice == '4':
            index = int(input("Enter the index of the task to delete: "))
            to_do_list.delete_task(index)

        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "_main_":
    main()