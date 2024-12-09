# from json_processor.processor import JSONProcessor
# import json

# def main():
#     # Step 1: Create a sample JSON file
#     file_name = "sample.json"
#     with open(file_name, 'w') as file:
#         json.dump({"name": "Example", "version": 1}, file, indent=4)

#     print(f"Sample JSON file '{file_name}' created.")

#     # Step 2: Initialize the processor
#     processor = JSONProcessor(file_name)

#     # Step 3: Load JSON
#     print("Loaded JSON data:")
#     print(processor.load_json())

#     # Step 4: Validate JSON
#     schema = ["name", "version"]
#     is_valid = processor.validate_json(schema)
#     print(f"Validation result (schema: {schema}): {is_valid}")

#     # Step 5: Modify JSON
#     updated_data = processor.modify_json("author", "John Doe")
#     print("Updated JSON data:")
#     print(updated_data)

# if __name__ == "__main__":
#     main()


# from task_manager.task_manager import TaskManager
# import os

# def display_menu():
#     print("\nTask Management App")
#     print("1. Add Task")
#     print("2. Edit Task")
#     print("3. Delete Task")
#     print("4. List Tasks")
#     print("5. Search Tasks")
#     print("6. Export Tasks")
#     print("7. Generate Report")
#     print("8. Exit")

# def main():
#     file_path = "tasks.json"
#     task_manager = TaskManager(file_path)

#     while True:
#         display_menu()
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             title = input("Enter task title: ")
#             description = input("Enter task description: ")
#             category = input("Enter task category: ")
#             priority = input("Enter task priority (Low, Medium, High): ")
#             deadline = input("Enter task deadline (YYYY-MM-DD HH:MM): ")

#             task_manager.add_task(title, description, category, priority, deadline)

#         elif choice == "2":
#             task_id = int(input("Enter task ID to edit: "))
#             print("Leave blank if you do not want to update a field.")
#             title = input("Enter new title: ")
#             description = input("Enter new description: ")
#             category = input("Enter new category: ")
#             priority = input("Enter new priority: ")
#             status = input("Enter new status: ")
#             deadline = input("Enter new deadline: ")

#             task_manager.edit_task(task_id, title or None, description or None, category or None, 
#                                    priority or None, status or None, deadline or None)

#         elif choice == "3":
#             task_id = int(input("Enter task ID to delete: "))
#             task_manager.delete_task(task_id)

#         elif choice == "4":
#             filter_status = input("Enter status to filter by (Pending, In Progress, Completed): ")
#             filter_category = input("Enter category to filter by: ")
#             tasks = task_manager.list_tasks(filter_status, filter_category)
#             for task in tasks:
#                 print(task)

#         elif choice == "5":
#             keyword = input("Enter keyword to search: ")
#             search_results = task_manager.search_tasks(keyword)
#             for task in search_results:
#                 print(task)

#         elif choice == "6":
#             export_file = input("Enter export file name: ")
#             task_manager.export_to_json(export_file)
#             print(f"Tasks exported to {export_file}")

#         elif choice == "7":
#             report = task_manager.generate_report()
#             print(f"Total Tasks: {report['total_tasks']}")
#             print(f"Completed Tasks: {report['completed_tasks']}")
#             print(f"Pending Tasks: {report['pending_tasks']}")
#             print(f"In Progress Tasks: {report['in_progress_tasks']}")

#         elif choice == "8":
#             print("Exiting Task Management App...")
#             break

#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

# from task_manager import TaskManager
from task_manager.task_manager import TaskManager



def display_menu():
    """
    Display the main menu options for the task management application.
    """
    print("\n=== Task Management Menu ===")
    print("1. Add a Task")
    print("2. Edit a Task")
    print("3. Delete a Task")
    print("4. List All Tasks")
    print("5. List Tasks by Status or Category")
    print("6. Search Tasks by Keyword")
    print("7. Sort Tasks by Deadline")
    print("8. Sort Tasks by Priority")
    print("9. Generate Task Report")
    print("10. Export Tasks to JSON")
    print("11. Exit")


def get_task_details():
    """
    Prompt the user for task details and return them as a dictionary.
    """
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    category = input("Enter the task category (e.g., Work, Personal): ")
    priority = input("Enter the task priority (High, Medium, Low): ")
    deadline = input("Enter the task deadline (YYYY-MM-DD): ")
    return {
        "title": title,
        "description": description,
        "category": category,
        "priority": priority,
        "deadline": deadline
    }


def main():
    """
    Main function to drive the task management application.
    """
    task_file = "tasks.json"
    task_manager = TaskManager(task_file)

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-11): ")

        if choice == "1":
            # Add a Task
            details = get_task_details()
            task_manager.add_task(
                details["title"],
                details["description"],
                details["category"],
                details["priority"],
                details["deadline"]
            )

        elif choice == "2":
            # Edit a Task
            task_id = int(input("Enter the task ID to edit: "))
            print("Leave fields blank to keep them unchanged.")
            title = input("New Title: ")
            description = input("New Description: ")
            category = input("New Category: ")
            priority = input("New Priority (High, Medium, Low): ")
            status = input("New Status (Pending, In Progress, Completed): ")
            deadline = input("New Deadline (YYYY-MM-DD): ")
            task_manager.edit_task(task_id, title, description, category, priority, status, deadline)

        elif choice == "3":
            # Delete a Task
            task_id = int(input("Enter the task ID to delete: "))
            task_manager.delete_task(task_id)

        elif choice == "4":
            # List All Tasks
            print("\n=== All Tasks ===")
            task_manager.print_all_tasks()

        elif choice == "5":
            # List Tasks by Status or Category
            filter_status = input("Enter the task status to filter by (Pending, In Progress, Completed) or press Enter to skip: ")
            filter_category = input("Enter the task category to filter by or press Enter to skip: ")
            filtered_tasks = task_manager.list_tasks(filter_status, filter_category)
            if filtered_tasks:
                print("\nFiltered Tasks:")
                for task in filtered_tasks:
                    task_manager.print_task(task)
            else:
                print("No tasks match the given criteria.")

        elif choice == "6":
            # Search Tasks by Keyword
            keyword = input("Enter a keyword to search tasks: ")
            search_results = task_manager.search_tasks(keyword)
            if search_results:
                print("\nSearch Results:")
                for task in search_results:
                    task_manager.print_task(task)
            else:
                print("No tasks match the given keyword.")

        elif choice == "7":
            # Sort Tasks by Deadline
            task_manager.sort_tasks_by_deadline()
            print("Tasks sorted by deadline successfully.")

        elif choice == "8":
            # Sort Tasks by Priority
            task_manager.sort_tasks_by_priority()
            print("Tasks sorted by priority successfully.")

        elif choice == "9":
            # Generate Task Report
            report = task_manager.generate_report()
            print(f"\n=== Task Report ===\n{report}")

        elif choice == "10":
            # Export Tasks to JSON
            export_file = input("Enter the file name to export tasks (e.g., export_tasks.json): ")
            task_manager.export_to_json(export_file)

        elif choice == "11":
            # Exit the Application
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please select an option from the menu.")

        input("\nPress Enter to continue...")  # Pause before showing the menu again


if __name__ == "__main__":
    main()
