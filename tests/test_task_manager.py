import unittest
import os
import json
from datetime import datetime, timedelta
from task_manager.task_manager import TaskManager  # Replace with the filename where TaskManager class resides
from unittest.mock import patch


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        """
        Setup a temporary JSON file and initialize the TaskManager for testing.
        """
        self.test_file = "test_tasks.json"
        self.task_manager = TaskManager(self.test_file)

    def tearDown(self):
        """
        Clean up by removing the test JSON file after each test.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task(self):
        """
        Test adding a task to the task list.
        """
        self.task_manager.add_task(
            title="Test Task",
            description="A task for testing",
            category="Testing",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.assertEqual(len(self.task_manager.tasks["tasks"]), 1)
        self.assertEqual(self.task_manager.tasks["tasks"][0]["title"], "Test Task")

    def test_edit_task(self):
        """
        Test editing an existing task.
        """
        self.task_manager.add_task(
            title="Test Task",
            description="A task for testing",
            category="Testing",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        task_id = self.task_manager.tasks["tasks"][0]["id"]
        self.task_manager.edit_task(task_id, title="Updated Task", status="Completed")
        task = self.task_manager.find_task_by_id(task_id)
        self.assertEqual(task["title"], "Updated Task")
        self.assertEqual(task["status"], "Completed")

    def test_delete_task(self):
        """
        Test deleting a task by ID.
        """
        self.task_manager.add_task(
            title="Test Task",
            description="A task for testing",
            category="Testing",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        task_id = self.task_manager.tasks["tasks"][0]["id"]
        self.task_manager.delete_task(task_id)
        self.assertIsNone(self.task_manager.find_task_by_id(task_id))

    def test_list_tasks(self):
        """
        Test listing tasks with optional filters.
        """
        self.task_manager.add_task(
            title="High Priority Task",
            description="High priority",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="Low Priority Task",
            description="Low priority",
            category="Personal",
            priority="Low",
            deadline=(datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d')
        )
        high_priority_tasks = self.task_manager.list_tasks(filter_status=None, filter_category="Work")
        self.assertEqual(len(high_priority_tasks), 1)
        self.assertEqual(high_priority_tasks[0]["priority"], "High")

    def test_sort_tasks_by_deadline(self):
        """
        Test sorting tasks by deadline.
        """
        self.task_manager.add_task(
            title="Task 1",
            description="Earliest deadline",
            category="Work",
            priority="Medium",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="Task 2",
            description="Later deadline",
            category="Personal",
            priority="High",
            deadline=(datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
        )
        self.task_manager.sort_tasks_by_deadline()
        self.assertEqual(self.task_manager.tasks["tasks"][0]["title"], "Task 1")

    def test_sort_tasks_by_priority(self):
        """
        Test sorting tasks by priority.
        """
        self.task_manager.add_task(
            title="Task 1",
            description="High priority",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="Task 2",
            description="Low priority",
            category="Personal",
            priority="Low",
            deadline=(datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
        )
        self.task_manager.sort_tasks_by_priority()
        self.assertEqual(self.task_manager.tasks["tasks"][0]["priority"], "High")

    def test_generate_report(self):
        """
        Test generating a report of task statistics.
        """
        self.task_manager.add_task(
            title="Task 1",
            description="Pending task",
            category="Work",
            priority="Medium",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="Task 2",
            description="Completed task",
            category="Personal",
            priority="Low",
            deadline=(datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
        )
        task_id = self.task_manager.tasks["tasks"][1]["id"]
        self.task_manager.edit_task(task_id, status="Completed")
        report = self.task_manager.generate_report()
        self.assertEqual(report["total_tasks"], 2)
        self.assertEqual(report["completed_tasks"], 1)
    
    def test_search_tasks(self):
        """
        Test searching for tasks by keyword.
        """
        self.task_manager.add_task(
            title="Searchable Task",
            description="This task should be found",
            category="Testing",
            priority="Medium",
            deadline=(datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
        )
        results = self.task_manager.search_tasks("Searchable")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Searchable Task")
    def test_export_to_json(self):
        """
        Test exporting tasks to a JSON file.
        """
        export_file = "exported_tasks.json"
        try:
            self.task_manager.add_task(
                title="Task to Export",
                description="Export test",
                category="Export",
                priority="High",
                deadline=(datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
            )
            self.task_manager.export_to_json(export_file)
            with open(export_file, 'r') as file:
                exported_data = json.load(file)
            self.assertIn("tasks", exported_data)
            self.assertEqual(len(exported_data["tasks"]), 1)
            self.assertEqual(exported_data["tasks"][0]["title"], "Task to Export")
        finally:
            if os.path.exists(export_file):
                os.remove(export_file)
            

    def test_print_task(self):
        """
        Test printing a single task.
        """
        self.task_manager.add_task(
            title="Printable Task",
            description="This task will be printed",
            category="Print",
            priority="Low",
            deadline=(datetime.now() + timedelta(days=4)).strftime('%Y-%m-%d')
        )
        task = self.task_manager.tasks["tasks"][0]
        with patch('builtins.print') as mock_print:
            self.task_manager.print_task(task)
            mock_print.assert_called_with(
                f"ID: {task['id']}, Title: {task['title']}, Priority: {task['priority']}, "
                f"Status: {task['status']}, Deadline: {task['deadline']}"
            )

    def test_print_all_tasks(self):
        """
        Test printing all tasks.
        """
        self.task_manager.add_task(
            title="Task 1",
            description="First printable task",
            category="Print",
            priority="Medium",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="Task 2",
            description="Second printable task",
            category="Print",
            priority="High",
            deadline=(datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
        )
        with patch('builtins.print') as mock_print:
            self.task_manager.print_all_tasks()
            self.assertEqual(mock_print.call_count, 2)





if __name__ == "__main__":
    unittest.main()
