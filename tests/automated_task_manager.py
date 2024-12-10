import unittest
import os
import json
from datetime import datetime, timedelta
from task_manager.task_manager import TaskManager
from unittest.mock import patch
from hypothesis import given, strategies as st


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

    @given(
        title=st.text(min_size=4, max_size=50),
        description=st.text(min_size=5, max_size=200),
        category=st.sampled_from(["Work", "Personal", "Health", "Education", "Misc"]),
        priority=st.sampled_from(["High", "Medium", "Low"]),
        days=st.integers(min_value=1, max_value=30)
    )
    def test_add_task_with_hypothesis(self, title, description, category, priority, days):
        """
        Test add_task with dynamically generated inputs using Hypothesis.
        """
        task_manager, test_file = self.setup_test_environment()
        try:
            deadline = (datetime.now() + timedelta(days=days)).strftime('%Y-%m-%d')
            task_manager.add_task(title, description, category, priority, deadline)
            assert len(task_manager.tasks["tasks"]) == 1
            assert task_manager.tasks["tasks"][0]["title"] == title
        finally:
            self.teardown_test_environment(test_file)


if __name__ == "__main__":
    unittest.main()
