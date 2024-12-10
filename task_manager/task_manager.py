# V4
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
                task_data = json.load(file)
                return task_data
        except json.JSONDecodeError:
            self._initialize_task_file()
            return {"tasks": []}

    def save_tasks(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            self.log_error(f"Error saving tasks to file: {e}")

    def _initialize_task_file(self):
        with open(self.file_path, 'w') as file:
            default_content = {"tasks": []}
            json.dump(default_content, file, indent=4)

    def add_task(self, title, description, category, priority, deadline):
        if not self._validate_title(title):
            return

        if not self._validate_description(description):
            return

        if not self._is_priority_valid(priority):
            return
        if not self._validate_category(category):
            return

        if not self._validate_date_format(deadline):
            return

        task_id = self.get_next_task_id()
        new_task = self._build_task(task_id, title, description, category, priority, deadline)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def _validate_title(self, title):
        if not title or len(title.strip()) < 3:
            print("Invalid title: Title must be at least 3 characters long.")
            return False
        return True

    def _validate_description(self, description):
        if not description or len(description.strip()) < 5:
            print("Invalid description: Description must be at least 5 characters long.")
            return False
        return True

    def _is_priority_valid(self, priority):
        valid_priorities = ["High", "Medium", "Low"]
        if priority not in valid_priorities:
            print("Invalid priority level.")
            return False
        return True

    def _build_task(self, task_id, title, description, category, priority, deadline):
        creation_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "category": category,
            "priority": priority,
            "status": "Pending",
            "deadline": deadline,
            "created_at": creation_time
        }
        return task

    def edit_task(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        for key, value in kwargs.items():
            if key in task and value is not None:
                if key == "deadline" and not self._validate_date_format(value):
                    continue
                task[key] = value
        self.log_task_history(task_id, "Edited", kwargs)
        self.save_tasks()

    def log_task_history(self, task_id, action, details):
        log_entry = {
            "task_id": task_id,
            "action": action,
            "details": details,
            "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        try:
            with open("task_history.log", 'a') as log_file:
                log_file.write(json.dumps(log_entry) + "\n")
        except IOError as e:
            print(f"Error logging task history: {e}")

    def delete_task(self, task_id):
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["id"] != task_id]
        self.log_task_history(task_id, "Deleted", {})
        self.save_tasks()

    def reset_task_file(self):
        self.tasks = {"tasks": []}
        self.save_tasks()

    def clone_task(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        new_task = task.copy()
        new_task["id"] = self.get_next_task_id()
        new_task["created_at"] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def list_tasks(self, filter_status=None, filter_category=None):
        filtered_tasks = self.tasks["tasks"]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]

        return filtered_tasks

    def search_tasks(self, keyword):
        keyword = keyword.lower()
        return [
            task for task in self.tasks["tasks"]
            if keyword in task["title"].lower() or keyword in task["description"].lower()
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
        self.tasks["tasks"].sort(key=lambda task: self._parse_date(task["deadline"]))
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
        task_ids = [task["id"] for task in self.tasks["tasks"]]
        return max(task_ids) + 1

    def _validate_date_format(self, date_string):
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            print(f"Invalid date format: {date_string}")
            return False

    def _parse_date(self, date_string):
        return datetime.strptime(date_string, '%Y-%m-%d')

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
            return []
        start = self._parse_date(start_date)
        end = self._parse_date(end_date)
        return [
            task for task in self.tasks["tasks"]
            if start <= self._parse_date(task["deadline"]) <= end
        ]

    def count_tasks_by_category(self):
        category_count = {}
        for task in self.tasks["tasks"]:
            category = task["category"]
            category_count[category] = category_count.get(category, 0) + 1
        return category_count

    def update_task_status_bulk(self, task_ids, new_status):
        if not self._validate_status(new_status):
            print(f"Bulk update failed: Invalid status '{new_status}'.")
            return
        for task_id in task_ids:
            task = self.find_task_by_id(task_id)
            if task:
                task["status"] = new_status
        self.save_tasks()

    def _validate_category(self, category):
        allowed_categories = ["Work", "Personal", "Health", "Education", "Misc"]
        if category not in allowed_categories:
            print(f"Invalid category: {category}. Allowed categories are: {', '.join(allowed_categories)}")
            return False
        return True
    
    def _validate_status(self, status):
        allowed_statuses = ["Pending", "In Progress", "Completed", "Archived"]
        if status not in allowed_statuses:
            print(f"Invalid status: {status}. Allowed statuses are: {', '.join(allowed_statuses)}")
            return False
        return True

    def get_tasks_by_priority(self, priority):
        if not self._is_priority_valid(priority):
            return []
        return [task for task in self.tasks["tasks"] if task["priority"] == priority]
    
    def count_tasks_by_status(self):
        status_count = {}
        for task in self.tasks["tasks"]:
            status = task["status"]
            status_count[status] = status_count.get(status, 0) + 1
        return status_count

    def mark_task_as_completed(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
        task["status"] = "Completed"
        self.save_tasks()
        print(f"Task with ID {task_id} marked as Completed.")


    def get_overdue_tasks(self):
        now = datetime.now()
        return [
            task for task in self.tasks["tasks"]
            if task["status"] != "Completed" and self._parse_date(task["deadline"]) < now
        ]

    def extend_task_deadline(self, task_id, days=0, hours=0):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task["deadline"])
        new_deadline = current_deadline + timedelta(days=days, hours=hours)
        task["deadline"] = new_deadline.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def generate_priority_report(self):
        priority_count = {"High": 0, "Medium": 0, "Low": 0}
        for task in self.tasks["tasks"]:
            if task["priority"] in priority_count:
                priority_count[task["priority"]] += 1
        return priority_count