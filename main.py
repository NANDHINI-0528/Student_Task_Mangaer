# Student Task Manager
# This program helps students manage their assignments.

# Store all student tasks
tasks = []

# Display the menu repeatedly
while True:

    print("\n===== STUDENT TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    # Get user's choice
    choice = input("Enter your choice: ")

    # Add a new task
    if choice == "1":
        task = input("Enter task name: ")

        if task.strip():
            tasks.append({"name": task, "completed": False})
            print("Task added successfully!")
        else:
            print("Task name cannot be empty!")

    # Display all tasks
    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available!")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks):
                status = "Completed" if task["completed"] else "Pending"
                print(i + 1, task["name"], "-", status)

    # Mark a task as completed
    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks available!")

        else:
            for i, task in enumerate(tasks):
                print(i + 1, task["name"])

            number = input("Enter task number: ")

            # Validate user input
            if number.isdigit():
                number = int(number)

                if 1 <= number <= len(tasks):
                    tasks[number - 1]["completed"] = True
                    print("Task completed successfully!")
                else:
                    print("Invalid task number!")

            else:
                print("Please enter a number!")

    # Delete a task
    elif choice == "4":

        if len(tasks) == 0:
            print("No tasks available!")

        else:
            for i, task in enumerate(tasks):
                print(i + 1, task["name"])

            number = input("Enter task number to delete: ")

            # Validate task number
            if number.isdigit():
                number = int(number)

                if 1 <= number <= len(tasks):
                    deleted = tasks.pop(number - 1)
                    print("Task deleted:", deleted["name"])
                else:
                    print("Invalid task number!")

            else:
                print("Please enter a number!")

    # Exit the application
    elif choice == "5":
        print("Thank you for using Student Task Manager!")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice! Try again.")

