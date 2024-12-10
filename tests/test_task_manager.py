# import unittest
# import os
# import json
# from datetime import datetime, timedelta
# from task_manager.task_manager import TaskManager  # Replace with the filename where TaskManager class resides
# from unittest.mock import patch


# class TestTaskManager(unittest.TestCase):

#     def setUp(self):
#         """
#         Setup a temporary JSON file and initialize the TaskManager for testing.
#         """
#         self.test_file = "test_tasks.json"
#         self.task_manager = TaskManager(self.test_file)

#     def tearDown(self):
#         """
#         Clean up by removing the test JSON file after each test.
#         """
#         if os.path.exists(self.test_file):
#             os.remove(self.test_file)

#     def test_add_task(self):
#         """
#         Test adding a task to the task list.
#         """
#         self.task_manager.add_task(
#             title="Test Task",
#             description="A task for testing",
#             category="Testing",
#             priority="High",
#             deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
#         )
#         self.assertEqual(len(self.task_manager.tasks["tasks"]), 1)
#         self.assertEqual(self.task_manager.tasks["tasks"][0]["title"], "Test Task")

#     def test_edit_task(self):
#         """
#         Test editing an existing task.
#         """
#         self.task_manager.add_task(
#             title="Test Task",
#             description="A task for testing",
#             category="Testing",
#             priority="High",
#             deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
#         )
#         task_id = self.task_manager.tasks["tasks"][0]["id"]
#         self.task_manager.edit_task(task_id, title="Updated Task", status="Completed")
#         task = self.task_manager.find_task_by_id(task_id)
#         self.assertEqual(task["title"], "Updated Task")
#         self.assertEqual(task["status"], "Completed")

#     def test_delete_task(self):
#         """
#         Test deleting a task by ID.
#         """
#         self.task_manager.add_task(
#             title="Test Task",
#             description="A task for testing",
#             category="Testing",
#             priority="High",
#             deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
#         )
#         task_id = self.task_manager.tasks["tasks"][0]["id"]
#         self.task_manager.delete_task(task_id)
#         self.assertIsNone(self.task_manager.find_task_by_id(task_id))

#     def test_list_tasks(self):
#         """
#         Test listing tasks with optional filters.
#         """
#         self.task_manager.add_task(
#             title="High Priority Task",
#             description="High priority",
#             category="Work",
#             priority="High",
#             deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
#         )
#         self.task_manager.add_task(
#             title="Low Priority Task",
#             description="Low priority",
#             category="Personal",
#             priority="Low",
#             deadline=(datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d')
#         )
#         high_priority_tasks = self.task_manager.list_tasks(filter_status=None, filter_category="Work")
#         self.assertEqual(len(high_priority_tasks), 1)
#         self.assertEqual(high_priority_tasks[0]["priority"], "High")

#     def test_sort_tasks_by_deadline(self):
#         """
#         Test sorting tasks by deadline.
#         """
#         self.task_manager.add_task(
#             title="Task 1",
#             description="Earliest deadline",
#             category="Work",
#             priority="Medium",
#             deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
#         )
#         self.task_manager.add_task(
#             title="Task 2",
#             description="Later deadline",
#             category="Personal",
#             priority="High",
#             deadline=(datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
#         )
#         self.task_manager.sort_tasks_by_deadline()
#         self.assertEqual(self.task_manager.tasks["tasks"][0]["title"], "Task 1")

#     def test_sort_tasks_by_priority(self):
#         """
#         Test sorting tasks by priority.
#         """
#         self.task_manager.add_task(
#             title="Task 1",
#             description="High priority",
#             category="Work",
#             priority="High",
#             deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
#         )
#         self.task_manager.add_task(
#             title="Task 2",
#             description="Low priority",
#             category="Personal",
#             priority="Low",
#             deadline=(datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
#         )
#         self.task_manager.sort_tasks_by_priority()
#         self.assertEqual(self.task_manager.tasks["tasks"][0]["priority"], "High")

#     def test_generate_report(self):
#         """
#         Test generating a report of task statistics.
#         """
#         self.task_manager.add_task(
#             title="Task 1",
#             description="Pending task",
#             category="Work",
#             priority="Medium",
#             deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
#         )
#         self.task_manager.add_task(
#             title="Task 2",
#             description="Completed task",
#             category="Personal",
#             priority="Low",
#             deadline=(datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
#         )
#         task_id = self.task_manager.tasks["tasks"][1]["id"]
#         self.task_manager.edit_task(task_id, status="Completed")
#         report = self.task_manager.generate_report()
#         self.assertEqual(report["total_tasks"], 2)
#         self.assertEqual(report["completed_tasks"], 1)
    
#     def test_search_tasks(self):
#         """
#         Test searching for tasks by keyword.
#         """
#         self.task_manager.add_task(
#             title="Searchable Task",
#             description="This task should be found",
#             category="Testing",
#             priority="Medium",
#             deadline=(datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
#         )
#         results = self.task_manager.search_tasks("Searchable")
#         self.assertEqual(len(results), 1)
#         self.assertEqual(results[0]["title"], "Searchable Task")
#     def test_export_to_json(self):
#         """
#         Test exporting tasks to a JSON file.
#         """
#         export_file = "exported_tasks.json"
#         try:
#             self.task_manager.add_task(
#                 title="Task to Export",
#                 description="Export test",
#                 category="Export",
#                 priority="High",
#                 deadline=(datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
#             )
#             self.task_manager.export_to_json(export_file)
#             with open(export_file, 'r') as file:
#                 exported_data = json.load(file)
#             self.assertIn("tasks", exported_data)
#             self.assertEqual(len(exported_data["tasks"]), 1)
#             self.assertEqual(exported_data["tasks"][0]["title"], "Task to Export")
#         finally:
#             if os.path.exists(export_file):
#                 os.remove(export_file)
            

#     def test_print_task(self):
#         """
#         Test printing a single task.
#         """
#         self.task_manager.add_task(
#             title="Printable Task",
#             description="This task will be printed",
#             category="Print",
#             priority="Low",
#             deadline=(datetime.now() + timedelta(days=4)).strftime('%Y-%m-%d')
#         )
#         task = self.task_manager.tasks["tasks"][0]
#         with patch('builtins.print') as mock_print:
#             self.task_manager.print_task(task)
#             mock_print.assert_called_with(
#                 f"ID: {task['id']}, Title: {task['title']}, Priority: {task['priority']}, "
#                 f"Status: {task['status']}, Deadline: {task['deadline']}"
#             )

#     def test_print_all_tasks(self):
#         """
#         Test printing all tasks.
#         """
#         self.task_manager.add_task(
#             title="Task 1",
#             description="First printable task",
#             category="Print",
#             priority="Medium",
#             deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
#         )
#         self.task_manager.add_task(
#             title="Task 2",
#             description="Second printable task",
#             category="Print",
#             priority="High",
#             deadline=(datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
#         )
#         with patch('builtins.print') as mock_print:
#             self.task_manager.print_all_tasks()
#             self.assertEqual(mock_print.call_count, 2)





# if __name__ == "__main__":
#     unittest.main()



# V2

import unittest
import os
import json
from datetime import datetime, timedelta
from task_manager.task_manager import TaskManager
from unittest.mock import patch
from hypothesis import given, strategies as st
from hypothesis import settings, HealthCheck

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        """Setup a temporary JSON file and initialize TaskManager for testing."""
        self.test_file = "test_tasks.json"
        self.task_manager = TaskManager(self.test_file)

    def setup_test_environment(self):
        test_file = "test_hypothesis_tasks.json"
        return TaskManager(test_file), test_file
    
    def teardown_test_environment(self, test_file):
        if os.path.exists(test_file):
            os.remove(test_file)

    def tearDown(self):
        """Remove the test JSON file after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    @given(
    title=st.text(min_size=3, max_size=50).filter(lambda x: len(x.strip()) >= 3),
    description=st.text(min_size=5, max_size=200).filter(lambda x: len(x.strip()) >= 5),
    category=st.sampled_from(["Work", "Personal", "Health", "Education", "Misc"]),
    priority=st.sampled_from(["High", "Medium", "Low"]),
    days=st.integers(min_value=1, max_value=30)
    )
    def test_add_task_with_hypothesis(self, title, description, category, priority, days):
        task_manager, test_file = self.setup_test_environment()
        try:
            deadline = (datetime.now() + timedelta(days=days)).strftime('%Y-%m-%d')
            task_manager.add_task(title, description, category, priority, deadline)
            assert len(task_manager.tasks["tasks"]) == 1
        finally:
            self.teardown_test_environment(test_file)


    @given(
        title=st.text(min_size=3, max_size=50).filter(lambda x: len(x.strip()) >= 3),
        description=st.text(min_size=5, max_size=200).filter(lambda x: len(x.strip()) >= 5),
        category=st.sampled_from(["Work", "Personal", "Health", "Education", "Misc"]),
        priority=st.sampled_from(["High", "Medium", "Low"]),
        days=st.integers(min_value=1, max_value=30)
    )
    @settings(suppress_health_check=[HealthCheck.differing_executors])
    def test_add_task_with_hypothesis(self, title, description, category, priority, days):
        task_manager, test_file = self.setup_test_environment()
        try:
            deadline = (datetime.now() + timedelta(days=days)).strftime('%Y-%m-%d')
            task_manager.add_task(title, description, category, priority, deadline)
            assert len(task_manager.tasks["tasks"]) == 1
        finally:
            self.teardown_test_environment(test_file)

    def test_add_task(self):
        """Test adding a task."""
        self.task_manager.add_task(
            title="Task 1",
            description="Task description",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.assertEqual(len(self.task_manager.tasks["tasks"]), 1)
        self.assertEqual(self.task_manager.tasks["tasks"][0]["title"], "Task 1")


    @given(priority=st.sampled_from(["High", "Medium", "Low"]))
    def test_get_tasks_by_priority_with_hypothesis(self, priority):
        task_manager, test_file = self.setup_test_environment()
        try:
            task_manager.add_task(
                title="Task 1",
                description="Description 1",
                category="Work",
                priority=priority,
                deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
            )
            tasks = task_manager.get_tasks_by_priority(priority)
            assert len(tasks) == 1
            assert tasks[0]["priority"] == priority
        finally:
            self.teardown_test_environment(test_file)

    def test_add_task_invalid_title(self):
        """
        Test adding a task with an invalid title.
        """
        self.task_manager.add_task(
            title="",
            description="Valid description",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.assertEqual(len(self.task_manager.tasks["tasks"]), 0)

    def test_add_task_invalid_description(self):
        """
        Test adding a task with an invalid description.
        """
        self.task_manager.add_task(
            title="Valid Title",
            description="",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.assertEqual(len(self.task_manager.tasks["tasks"]), 0)

    def test_add_task_invalid_priority(self):
        """
        Test adding a task with an invalid priority.
        """
        self.task_manager.add_task(
            title="Valid Title",
            description="Valid description",
            category="Work",
            priority="InvalidPriority",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.assertEqual(len(self.task_manager.tasks["tasks"]), 0)

    def test_add_task_invalid_category(self):
        """
        Test adding a task with an invalid category.
        """
        self.task_manager.add_task(
            title="Valid Title",
            description="Valid description",
            category="InvalidCategory",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.assertEqual(len(self.task_manager.tasks["tasks"]), 0)

    def test_add_task_invalid_deadline(self):
        """
        Test adding a task with an invalid deadline.
        """
        self.task_manager.add_task(
            title="Valid Title",
            description="Valid description",
            category="Work",
            priority="High",
            deadline="InvalidDate"
        )
        self.assertEqual(len(self.task_manager.tasks["tasks"]), 0)


    def test_edit_task(self):
        """Test editing an existing task."""
        self.task_manager.add_task(
            title="Task 1",
            description="Task description",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        task_id = self.task_manager.tasks["tasks"][0]["id"]
        self.task_manager.edit_task(task_id, title="Updated Title", status="Completed")
        task = self.task_manager.find_task_by_id(task_id)
        self.assertEqual(task["title"], "Updated Title")
        self.assertEqual(task["status"], "Completed")

    def test_delete_task(self):
        """Test deleting a task."""
        self.task_manager.add_task(
            title="Task 1",
            description="Task description",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        task_id = self.task_manager.tasks["tasks"][0]["id"]
        self.task_manager.delete_task(task_id)
        self.assertIsNone(self.task_manager.find_task_by_id(task_id))

    def test_list_tasks(self):
        """Test listing tasks with filters."""
        self.task_manager.add_task(
            title="High Priority Task",
            description="Important task",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="Low Priority Task",
            description="Unimportant task",
            category="Personal",
            priority="Low",
            deadline=(datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d')
        )
        filtered_tasks = self.task_manager.list_tasks(filter_category="Work")
        self.assertEqual(len(filtered_tasks), 1)
        self.assertEqual(filtered_tasks[0]["priority"], "High")

    def test_sort_tasks_by_deadline(self):
        """Test sorting tasks by deadline."""
        self.task_manager.add_task(
            title="Task 1",
            description="Earlier deadline",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="Task 2",
            description="Later deadline",
            category="Personal",
            priority="Low",
            deadline=(datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
        )
        self.task_manager.sort_tasks_by_deadline()
        self.assertEqual(self.task_manager.tasks["tasks"][0]["title"], "Task 1")

    def test_sort_tasks_by_priority(self):
        """Test sorting tasks by priority."""
        self.task_manager.add_task(
            title="Task 1",
            description="High priority task",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="Task 2",
            description="Low priority task",
            category="Personal",
            priority="Low",
            deadline=(datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
        )
        self.task_manager.sort_tasks_by_priority()
        self.assertEqual(self.task_manager.tasks["tasks"][0]["priority"], "High")

    def test_generate_report(self):
        """Test generating task statistics."""
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

    def test_archive_completed_tasks(self):
        """Test archiving completed tasks."""
        archive_file = "archive_tasks.json"
        try:
            self.task_manager.add_task(
                title="Task 1",
                description="Pending task",
                category="Work",
                priority="Medium",
                deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
            )
            task_id = self.task_manager.tasks["tasks"][0]["id"]
            self.task_manager.edit_task(task_id, status="Completed")
            self.task_manager.archive_completed_tasks(archive_file)
            with open(archive_file, 'r') as file:
                archived_tasks = json.load(file)
            self.assertEqual(len(archived_tasks["archived_tasks"]), 1)
            self.assertEqual(archived_tasks["archived_tasks"][0]["status"], "Completed")
        finally:
            if os.path.exists(archive_file):
                os.remove(archive_file)

    def test_filter_tasks_by_date_range(self):
        """Test filtering tasks within a date range."""
        self.task_manager.add_task(
            title="Task 1",
            description="First task",
            category="Work",
            priority="Medium",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="Task 2",
            description="Second task",
            category="Personal",
            priority="Low",
            deadline=(datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
        )
        filtered_tasks = self.task_manager.filter_tasks_by_date_range(
            (datetime.now()).strftime('%Y-%m-%d'),
            (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
        )
        self.assertEqual(len(filtered_tasks), 1)
        self.assertEqual(filtered_tasks[0]["title"], "Task 1")

    def test_extend_task_deadline(self):
        """Test extending a task's deadline."""
        self.task_manager.add_task(
            title="Task 1",
            description="Original deadline",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        task_id = self.task_manager.tasks["tasks"][0]["id"]
        self.task_manager.extend_task_deadline(task_id, days=2, hours=5)
        updated_task = self.task_manager.find_task_by_id(task_id)
        extended_deadline = datetime.strptime(updated_task["deadline"], '%Y-%m-%d %H:%M:%S')
        self.assertTrue(extended_deadline > datetime.now())

    def test_get_overdue_tasks(self):
        """Test retrieving overdue tasks."""
        self.task_manager.add_task(
            title="Overdue Task",
            description="This task is overdue",
            category="Work",
            priority="Low",
            deadline=(datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        )
        overdue_tasks = self.task_manager.get_overdue_tasks()
        self.assertEqual(len(overdue_tasks), 1)
        self.assertEqual(overdue_tasks[0]["title"], "Overdue Task")

    def test_generate_priority_report(self):
        """Test generating a report based on task priorities."""
        self.task_manager.add_task(
            title="Task 1",
            description="High priority task",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="Task 2",
            description="Low priority task",
            category="Personal",
            priority="Low",
            deadline=(datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
        )
        priority_report = self.task_manager.generate_priority_report()
        self.assertEqual(priority_report["High"], 1)
        self.assertEqual(priority_report["Low"], 1)

    # def test_clone_task(self):
    #     """
    #     Test cloning an existing task.
    #     """
    #     # Add a task to clone
    #     self.task_manager.add_task(
    #         title="Task to Clone",
    #         description="This task will be cloned",
    #         category="Work",
    #         priority="Medium",
    #         deadline=(datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
    #     )
    def test_clone_task(self):
        self.task_manager.add_task(
            title="Original Task",
            description="Task to clone",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        original_task_id = self.task_manager.tasks["tasks"][0]["id"]
        self.task_manager.clone_task(original_task_id)
        self.assertEqual(len(self.task_manager.tasks["tasks"]), 2)
        cloned_task = self.task_manager.tasks["tasks"][1]
        self.assertNotEqual(original_task_id, cloned_task["id"])
        self.assertEqual(cloned_task["title"], "Original Task")

        
        # Get the original task ID
        original_task_id = self.task_manager.tasks["tasks"][0]["id"]

        # Clone the task
        self.task_manager.clone_task(original_task_id)

        # Verify that a new task was added
        self.assertEqual(len(self.task_manager.tasks["tasks"]), 3)

        # Get the cloned task
        cloned_task = self.task_manager.tasks["tasks"][1]

        # Check if the cloned task matches the original task except for the ID and created_at
        self.assertNotEqual(cloned_task["id"], original_task_id)
        self.assertEqual(cloned_task["title"], "Original Task")
        self.assertEqual(cloned_task["description"], "Task to clone")
        self.assertEqual(cloned_task["category"], "Work")
        self.assertEqual(cloned_task["priority"], "High")
        self.assertEqual(cloned_task["created_at"], self.task_manager.tasks["tasks"][0]["created_at"])


    def test_reset_task_file(self):
        self.task_manager.add_task(
            title="Task to Delete",
            description="This will be removed",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.assertEqual(len(self.task_manager.tasks["tasks"]), 1)
        self.task_manager.reset_task_file()
        self.assertEqual(len(self.task_manager.tasks["tasks"]), 0)



    def test_count_tasks_by_category(self):
        """
        Test counting tasks by category.
        """
        # Add multiple tasks with different categories
        self.task_manager.add_task(
            title="Work Task 1",
            description="Task in Work category",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="Work Task 2",
            description="Another task in Work category",
            category="Work",
            priority="Medium",
            deadline=(datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="Personal Task",
            description="Task in Personal category",
            category="Personal",
            priority="Low",
            deadline=(datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="Health Task",
            description="Task in Health category",
            category="Health",
            priority="Medium",
            deadline=(datetime.now() + timedelta(days=4)).strftime('%Y-%m-%d')
        )

        # Call the method to count tasks by category
        category_counts = self.task_manager.count_tasks_by_category()

        # Verify the counts for each category
        self.assertEqual(category_counts["Work"], 2)
        self.assertEqual(category_counts["Personal"], 1)
        self.assertEqual(category_counts["Health"], 1)

        # Verify that no unexpected categories exist
        self.assertEqual(len(category_counts), 3)

    def test_update_task_status_bulk(self):
        """
        Test updating the status of multiple tasks in bulk.
        """
        # Add multiple tasks
        self.task_manager.add_task(
            title="Task 1",
            description="First task",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="Task 2",
            description="Second task",
            category="Personal",
            priority="Medium",
            deadline=(datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="Task 3",
            description="Third task",
            category="Health",
            priority="Low",
            deadline=(datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
        )

        # Get task IDs
        task_ids = [task["id"] for task in self.task_manager.tasks["tasks"]]

        # Bulk update the status of all tasks
        self.task_manager.update_task_status_bulk(task_ids, new_status="Completed")

        # Verify that the status of all tasks was updated
        for task_id in task_ids:
            task = self.task_manager.find_task_by_id(task_id)
            self.assertEqual(task["status"], "Completed")

        # Test with an invalid status
        with patch('builtins.print') as mock_print:
            self.task_manager.update_task_status_bulk(task_ids, new_status="InvalidStatus")
            mock_print.assert_called_with("Bulk update failed: Invalid status 'InvalidStatus'.")

    def test_get_tasks_by_priority(self):
        """
        Test retrieving tasks filtered by a specific priority.
        """
        # Add tasks with different priorities
        self.task_manager.add_task(
            title="High Priority Task",
            description="This is a high priority task",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="Medium Priority Task",
            description="This is a medium priority task",
            category="Personal",
            priority="Medium",
            deadline=(datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="Low Priority Task",
            description="This is a low priority task",
            category="Health",
            priority="Low",
            deadline=(datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
        )

        # Test filtering by "High" priority
        high_priority_tasks = self.task_manager.get_tasks_by_priority("High")
        self.assertEqual(len(high_priority_tasks), 1)
        self.assertEqual(high_priority_tasks[0]["title"], "High Priority Task")

        # Test filtering by "Medium" priority
        medium_priority_tasks = self.task_manager.get_tasks_by_priority("Medium")
        self.assertEqual(len(medium_priority_tasks), 1)
        self.assertEqual(medium_priority_tasks[0]["title"], "Medium Priority Task")

        # Test filtering by "Low" priority
        low_priority_tasks = self.task_manager.get_tasks_by_priority("Low")
        self.assertEqual(len(low_priority_tasks), 1)
        self.assertEqual(low_priority_tasks[0]["title"], "Low Priority Task")

        # Test filtering by an invalid priority
        invalid_priority_tasks = self.task_manager.get_tasks_by_priority("InvalidPriority")
        self.assertEqual(len(invalid_priority_tasks), 0)


    def test_count_tasks_by_status(self):
        """
        Test counting tasks by their status.
        """
        # Add tasks with different statuses
        self.task_manager.add_task(
            title="Pending Task",
            description="Task in Pending status",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="In Progress Task",
            description="Task in In Progress status",
            category="Personal",
            priority="Medium",
            deadline=(datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
        )
        self.task_manager.add_task(
            title="Completed Task",
            description="Task in Completed status",
            category="Health",
            priority="Low",
            deadline=(datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
        )
        
        # Mark one task as completed
        task_id = self.task_manager.tasks["tasks"][0]["id"]
        self.task_manager.edit_task(task_id, status="In Progress")
        
        # Count tasks by status
        status_counts = self.task_manager.count_tasks_by_status()

        # Assert counts for each status
        # TODO
        self.assertEqual(status_counts["Pending"], 2)
        self.assertEqual(status_counts["In Progress"], 1)

    def test_mark_task_as_completed(self):
        """
        Test marking a task as completed.
        """
        # Add a task
        self.task_manager.add_task(
            title="Task to Complete",
            description="This task will be marked as completed",
            category="Work",
            priority="High",
            deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        )

        # Get the task ID
        task_id = self.task_manager.tasks["tasks"][0]["id"]

        # Mark the task as completed
        self.task_manager.mark_task_as_completed(task_id)

        # Verify the task's status is updated
        task = self.task_manager.find_task_by_id(task_id)
        self.assertEqual(task["status"], "Completed")

        # Test with an invalid task ID
        with patch('builtins.print') as mock_print:
            self.task_manager.mark_task_as_completed(9999)  # Invalid ID
            mock_print.assert_called_with("Task with ID 9999 not found.")

    def test_export_to_json(self):
        """
        Test exporting tasks to a JSON file.
        """
        export_file = "test_export_tasks.json"
        try:
            # Add tasks to export
            self.task_manager.add_task(
                title="Exported Task 1",
                description="First task for export",
                category="Work",
                priority="High",
                deadline=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
            )
            self.task_manager.add_task(
                title="Exported Task 2",
                description="Second task for export",
                category="Personal",
                priority="Low",
                deadline=(datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
            )

            # Export tasks to JSON
            self.task_manager.export_to_json(export_file)

            # Verify the exported file exists and contains the correct data
            with open(export_file, 'r') as file:
                exported_data = json.load(file)
            self.assertIn("tasks", exported_data)
            self.assertEqual(len(exported_data["tasks"]), 2)
            self.assertEqual(exported_data["tasks"][0]["title"], "Exported Task 1")
            self.assertEqual(exported_data["tasks"][1]["title"], "Exported Task 2")
        finally:
            if os.path.exists(export_file):
                os.remove(export_file)

    def test_load_tasks_with_invalid_json(self):
        """
        Test loading tasks from a corrupted JSON file.
        """
        # Create a corrupted JSON file
        with open(self.test_file, 'w') as file:
            file.write("INVALID_JSON")
        
        # Initialize TaskManager to load the corrupted file
        self.task_manager = TaskManager(self.test_file)

        # Verify that tasks are re-initialized to an empty list
        self.assertEqual(self.task_manager.tasks, {"tasks": []})


if __name__ == "__main__":
    unittest.main()
