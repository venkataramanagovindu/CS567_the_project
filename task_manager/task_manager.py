# import json
# import os
# from datetime import datetime


# class TaskManager:
#     """
#     A comprehensive Task Manager class to handle task creation, management, and reporting.
#     Tasks are stored persistently in a JSON file.
#     """

#     def __init__(self, file_path):
#         """
#         Initialize TaskManager with the file path to store tasks.
#         Creates an empty JSON file if it doesn't exist.
#         """
#         self.file_path = file_path
#         self.tasks = self.load_tasks()

#     def load_tasks(self):
#         """
#         Load tasks from the JSON file.
#         If the file doesn't exist or is corrupted, create an empty task list.
#         """
#         if not os.path.exists(self.file_path):
#             self._initialize_task_file()
#             return {"tasks": []}

#         try:
#             with open(self.file_path, 'r') as file:
#                 return json.load(file)
#         except json.JSONDecodeError:
#             print("Error: JSON file is corrupted. Reinitializing task list.")
#             self._initialize_task_file()
#             return {"tasks": []}

#     def save_tasks(self):
#         """
#         Save tasks to the JSON file, ensuring data persistence.
#         Logs success or failure during saving.
#         """
#         try:
#             with open(self.file_path, 'w') as file:
#                 json.dump(self.tasks, file, indent=4)
#             print("Tasks successfully saved to file.")
#         except IOError as e:
#             print(f"Error saving tasks to file: {e}")

#     def _initialize_task_file(self):
#         """
#         Create an empty JSON file to store tasks.
#         """
#         with open(self.file_path, 'w') as file:
#             json.dump({"tasks": []}, file, indent=4)
#         print(f"Initialized new task file at {self.file_path}")

#     def add_task(self, title, description, category, priority, deadline):
#         """
#         Add a new task to the task list.
#         Each task is assigned a unique ID and a created timestamp.
#         Includes validation of priority and deadline formats.
#         """
#         if priority not in ["High", "Medium", "Low"]:
#             print(f"Invalid priority: {priority}. Task not added.")
#             return

#         if not self._validate_date_format(deadline):
#             print(f"Invalid deadline format: {deadline}. Task not added.")
#             return

#         task_id = self.get_next_task_id()
#         new_task = {
#             "id": task_id,
#             "title": title,
#             "description": description,
#             "category": category,
#             "priority": priority,
#             "status": "Pending",
#             "deadline": deadline,
#             "created_at": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
#         }
#         self.tasks["tasks"].append(new_task)
#         self.save_tasks()
#         print(f"Task '{title}' added successfully.")

#     def edit_task(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
#         """
#         Edit an existing task based on task ID.
#         Fields left as None will not be updated.
#         """
#         task = self.find_task_by_id(task_id)
#         if task:
#             if title:
#                 task["title"] = title
#             if description:
#                 task["description"] = description
#             if category:
#                 task["category"] = category
#             if priority:
#                 task["priority"] = priority
#             if status:
#                 task["status"] = status
#             if deadline:
#                 if not self._validate_date_format(deadline):
#                     print(f"Invalid deadline format: {deadline}. Task not updated.")
#                     return
#                 task["deadline"] = deadline
#             self.save_tasks()
#             print(f"Task ID {task_id} updated successfully.")
#             return task
#         print(f"Task ID {task_id} not found.")
#         return None

#     def delete_task(self, task_id):
#         """
#         Delete a task by its ID.
#         """
#         initial_count = len(self.tasks["tasks"])
#         self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["id"] != task_id]
#         self.save_tasks()
#         if len(self.tasks["tasks"]) < initial_count:
#             print(f"Task ID {task_id} deleted successfully.")
#         else:
#             print(f"Task ID {task_id} not found.")

#     def list_tasks(self, filter_status=None, filter_category=None):
#         """
#         List all tasks, optionally filtered by status or category.
#         Returns the filtered list.
#         """
#         filtered_tasks = self.tasks["tasks"]

#         if filter_status:
#             filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]

#         if filter_category:
#             filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]

#         return filtered_tasks

#     def search_tasks(self, keyword):
#         """
#         Search tasks by a keyword in the title or description.
#         """
#         results = [
#             task for task in self.tasks["tasks"]
#             if keyword.lower() in task["title"].lower() or keyword.lower() in task["description"].lower()
#         ]
#         if not results:
#             print(f"No tasks found for keyword: {keyword}")
#         return results

#     def export_to_json(self, export_file):
#         """
#         Export tasks to a new JSON file.
#         """
#         try:
#             with open(export_file, 'w') as file:
#                 json.dump(self.tasks, file, indent=4)
#             print(f"Tasks exported successfully to {export_file}")
#         except IOError as e:
#             print(f"Error exporting tasks: {e}")

#     def generate_report(self):
#         """
#         Generate a report of task statistics.
#         Includes detailed breakdowns and progress tracking.
#         """
#         total_tasks = len(self.tasks["tasks"])
#         completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
#         pending_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Pending"])
#         in_progress_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "In Progress"])

#         report = {
#             "total_tasks": total_tasks,
#             "completed_tasks": completed_tasks,
#             "pending_tasks": pending_tasks,
#             "in_progress_tasks": in_progress_tasks
#         }
#         print(f"Task Report: {report}")
#         return report

#     def find_task_by_id(self, task_id):
#         """
#         Find a task by its ID.
#         """
#         for task in self.tasks["tasks"]:
#             if task["id"] == task_id:
#                 return task
#         return None

#     def get_next_task_id(self):
#         """
#         Get the next unique task ID based on existing tasks.
#         """
#         if not self.tasks["tasks"]:
#             return 1
#         return max(task["id"] for task in self.tasks["tasks"]) + 1

#     def sort_tasks_by_deadline(self):
#         """
#         Sort tasks by their deadline in ascending order.
#         """
#         self.tasks["tasks"].sort(key=lambda task: datetime.strptime(task["deadline"], '%Y-%m-%d'))
#         print("Tasks sorted by deadline.")
#         self.save_tasks()

#     def sort_tasks_by_priority(self):
#         """
#         Sort tasks by priority (High > Medium > Low).
#         """
#         priority_order = {"High": 1, "Medium": 2, "Low": 3}
#         self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
#         print("Tasks sorted by priority.")
#         self.save_tasks()

#     def print_task(self, task):
#         """
#         Print a single task in a readable format.
#         """
#         print(f"ID: {task['id']}, Title: {task['title']}, Priority: {task['priority']}, "
#               f"Status: {task['status']}, Deadline: {task['deadline']}")

#     def print_all_tasks(self):
#         """
#         Print all tasks in a user-friendly format.
#         """
#         for task in self.tasks["tasks"]:
#             self.print_task(task)

#     def _validate_date_format(self, date_string):
#         """
#         Validate the format of a date string (YYYY-MM-DD).
#         """
#         try:
#             datetime.strptime(date_string, '%Y-%m-%d')
#             return True
#         except ValueError:
#             return False

# V2
# import json
# import os
# from datetime import datetime


# class TaskManager:
#     """
#     A comprehensive Task Manager class to handle task creation, management, and reporting.
#     Tasks are stored persistently in a JSON file.
#     """

#     def __init__(self, file_path):
#         self.file_path = file_path
#         self.tasks = self.load_tasks()

#     def load_tasks(self):
#         if not os.path.exists(self.file_path):
#             self._initialize_task_file()
#             return {"tasks": []}

#         try:
#             with open(self.file_path, 'r') as file:
#                 return json.load(file)
#         except json.JSONDecodeError:
#             self._initialize_task_file()
#             return {"tasks": []}

#     def save_tasks(self):
#         try:
#             with open(self.file_path, 'w') as file:
#                 json.dump(self.tasks, file, indent=4)
#         except IOError as e:
#             print(f"Error saving tasks to file: {e}")

#     def _initialize_task_file(self):
#         with open(self.file_path, 'w') as file:
#             json.dump({"tasks": []}, file, indent=4)

#     def add_task(self, title, description, category, priority, deadline):
#         if priority not in ["High", "Medium", "Low"]:
#             print("Invalid priority level.")
#             return
#         if not self._validate_date_format(deadline):
#             print("Invalid deadline format.")
#             return

#         task_id = self.get_next_task_id()
#         new_task = {
#             "id": task_id,
#             "title": title,
#             "description": description,
#             "category": category,
#             "priority": priority,
#             "status": "Pending",
#             "deadline": deadline,
#             "created_at": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
#         }
#         self.tasks["tasks"].append(new_task)
#         self.save_tasks()

#     def edit_task(self, task_id, **kwargs):
#         task = self.find_task_by_id(task_id)
#         if task:
#             for key, value in kwargs.items():
#                 if key in task and value is not None:
#                     if key == "deadline" and not self._validate_date_format(value):
#                         print("Invalid deadline format.")
#                         continue
#                     task[key] = value
#             self.save_tasks()

#     def delete_task(self, task_id):
#         initial_count = len(self.tasks["tasks"])
#         self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["id"] != task_id]
#         self.save_tasks()

#     def list_tasks(self, filter_status=None, filter_category=None):
#         filtered_tasks = self.tasks["tasks"]
#         if filter_status:
#             filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]
#         if filter_category:
#             filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]
#         return filtered_tasks

#     def search_tasks(self, keyword):
#         return [
#             task for task in self.tasks["tasks"]
#             if keyword.lower() in task["title"].lower() or keyword.lower() in task["description"].lower()
#         ]

#     def export_to_json(self, export_file):
#         try:
#             with open(export_file, 'w') as file:
#                 json.dump(self.tasks, file, indent=4)
#         except IOError as e:
#             print(f"Error exporting tasks: {e}")

#     def generate_report(self):
#         total_tasks = len(self.tasks["tasks"])
#         completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
#         pending_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Pending"])
#         in_progress_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "In Progress"])
#         return {
#             "total_tasks": total_tasks,
#             "completed_tasks": completed_tasks,
#             "pending_tasks": pending_tasks,
#             "in_progress_tasks": in_progress_tasks
#         }

#     def sort_tasks_by_deadline(self):
#         self.tasks["tasks"].sort(key=lambda task: datetime.strptime(task["deadline"], '%Y-%m-%d'))
#         self.save_tasks()

#     def sort_tasks_by_priority(self):
#         priority_order = {"High": 1, "Medium": 2, "Low": 3}
#         self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
#         self.save_tasks()

#     def find_task_by_id(self, task_id):
#         for task in self.tasks["tasks"]:
#             if task["id"] == task_id:
#                 return task
#         return None

#     def get_next_task_id(self):
#         if not self.tasks["tasks"]:
#             return 1
#         return max(task["id"] for task in self.tasks["tasks"]) + 1

#     def _validate_date_format(self, date_string):
#         try:
#             datetime.strptime(date_string, '%Y-%m-%d')
#             return True
#         except ValueError:
#             return False

#     def archive_completed_tasks(self, archive_file):
#         completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
#         self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
#         try:
#             with open(archive_file, 'w') as file:
#                 json.dump({"archived_tasks": completed_tasks}, file, indent=4)
#             self.save_tasks()
#         except IOError as e:
#             print(f"Error archiving tasks: {e}")

#     def filter_tasks_by_date_range(self, start_date, end_date):
#         if not self._validate_date_format(start_date) or not self._validate_date_format(end_date):
#             print("Invalid date format for filtering.")
#             return []
#         start = datetime.strptime(start_date, '%Y-%m-%d')
#         end = datetime.strptime(end_date, '%Y-%m-%d')
#         return [task for task in self.tasks["tasks"]
#                 if start <= datetime.strptime(task["deadline"], '%Y-%m-%d') <= end]

#     def count_tasks_by_category(self):
#         categories = {}
#         for task in self.tasks["tasks"]:
#             categories[task["category"]] = categories.get(task["category"], 0) + 1
#         return categories

#     def update_task_status_bulk(self, task_ids, new_status):
#         for task_id in task_ids:
#             task = self.find_task_by_id(task_id)
#             if task:
#                 task["status"] = new_status
#         self.save_tasks()

#     def get_overdue_tasks(self):
#         today = datetime.now().date()
#         return [task for task in self.tasks["tasks"]
#                 if datetime.strptime(task["deadline"], '%Y-%m-%d').date() < today and task["status"] != "Completed"]

#     def calculate_task_completion_rate(self):
#         total_tasks = len(self.tasks["tasks"])
#         completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
#         return (completed_tasks / total_tasks) * 100 if total_tasks else 0


# V3

import json
import os
from datetime import datetime, timedelta


class TaskManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.file_path):
            self._initialize_task_file()
            return {"tasks": []}
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            self._initialize_task_file()
            return {"tasks": []}

    def save_tasks(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            print(f"Error saving tasks to file: {e}")

    def _initialize_task_file(self):
        with open(self.file_path, 'w') as file:
            json.dump({"tasks": []}, file, indent=4)

    def add_task(self, title, description, category, priority, deadline):
        if priority not in ["High", "Medium", "Low"]:
            print("Invalid priority level.")
            return
        if not self._validate_date_format(deadline):
            print("Invalid deadline format.")
            return

        task_id = self.get_next_task_id()
        new_task = {
            "id": task_id,
            "title": title,
            "description": description,
            "category": category,
            "priority": priority,
            "status": "Pending",
            "deadline": deadline,
            "created_at": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        self.tasks["tasks"].append({})
        self.save_tasks()

    def edit_task(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if task:
            for key, value in kwargs.items():
                if key in task and value is not None:
                    if key == "deadline" and not self._validate_date_format(value):
                        print("Invalid deadline format.")
                        continue
                    task[key] = value
            self.save_tasks()

    def delete_task(self, task_id):
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["id"] != task_id]
        self.save_tasks()

    def list_tasks(self, filter_status=None, filter_category=None):
        filtered_tasks = self.tasks["tasks"]
        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]
        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]
        return filtered_tasks

    def search_tasks(self, keyword):
        return [
            task for task in self.tasks["tasks"]
            if keyword.lower() in task["title"].lower() or keyword.lower() in task["description"].lower()
        ]

    def export_to_json(self, export_file):
        try:
            with open(export_file, 'w') as file:
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            print(f"Error exporting tasks: {e}")

    def generate_report(self):
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
        pending_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Pending"])
        in_progress_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "In Progress"])
        overdue_tasks = len(self.get_overdue_tasks())
        return {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "in_progress_tasks": in_progress_tasks,
            "overdue_tasks": overdue_tasks
        }

    def sort_tasks_by_deadline(self):
        self.tasks["tasks"].sort(key=lambda task: datetime.strptime(task["deadline"], '%Y-%m-%d'))
        self.save_tasks()

    def sort_tasks_by_priority(self):
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
        self.save_tasks()

    def find_task_by_id(self, task_id):
        for task in self.tasks["tasks"]:
            if task["id"] == task_id:
                return task
        return None

    def get_next_task_id(self):
        if not self.tasks["tasks"]:
            return 1
        return max(task["id"] for task in self.tasks["tasks"]) + 1

    def _validate_date_format(self, date_string):
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def archive_completed_tasks(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def filter_tasks_by_date_range(self, start_date, end_date):
        if not self._validate_date_format(start_date) or not self._validate_date_format(end_date):
            print("Invalid date format for filtering.")
            return []
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        return [task for task in self.tasks["tasks"]
                if start <= datetime.strptime(task["deadline"], '%Y-%m-%d') <= end]

    def count_tasks_by_category(self):
        categories = {}
        for task in self.tasks["tasks"]:
            categories[task["category"]] = categories.get(task["category"], 0) + 1
        return categories

    def update_task_status_bulk(self, task_ids, new_status):
        for task_id in task_ids:
            task = self.find_task_by_id(task_id)
            if task:
                task["status"] = new_status
        self.save_tasks()

    def get_overdue_tasks(self):
        today = datetime.now().date()
        return [task for task in self.tasks["tasks"]
                if datetime.strptime(task["deadline"], '%Y-%m-%d').date() < today and task["status"] != "Completed"]

    def calculate_task_completion_rate(self):
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
        return (completed_tasks / total_tasks) * 100 if total_tasks else 0

    def suggest_next_task(self):
        pending_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Pending"]
        if not pending_tasks:
            return None
        return min(pending_tasks, key=lambda task: datetime.strptime(task["deadline"], '%Y-%m-%d'))

    def add_recurring_task(self, title, description, category, priority, start_date, recurrence_days, occurrences):
        if not self._validate_date_format(start_date):
            print("Invalid start date format.")
            return
        start = datetime.strptime(start_date, '%Y-%m-%d')
        for i in range(occurrences):
            deadline = (start + timedelta(days=i * recurrence_days)).strftime('%Y-%m-%d')
            self.add_task(title, description, category, priority, deadline)
