import unittest
import os
import json
from json_processor.processor import JSONProcessor
from hypothesis import given, strategies as st

class TestJSONProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temporary JSON file
        self.test_file = "test.json"
        with open(self.test_file, 'w') as file:
            json.dump({"name": "Test"}, file)

    def tearDown(self):
        # Remove the temporary file
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_json(self):
        processor = JSONProcessor(self.test_file)
        data = processor.load_json()
        self.assertEqual(data, {"name": "Test"})

    def test_validate_json(self):
        processor = JSONProcessor(self.test_file)
        schema = ["name"]
        self.assertTrue(processor.validate_json(schema))

    def test_modify_json(self):
        processor = JSONProcessor(self.test_file)
        modified_data = processor.modify_json("age", 25)
        self.assertEqual(modified_data, {"name": "Test", "age": 25})

    @given(st.dictionaries(keys=st.text(), values=st.integers()))
    def test_modify_json_with_random_input(self, random_data):
        processor = JSONProcessor(self.test_file)
        for key, value in random_data.items():
            modified_data = processor.modify_json(key, value)
            self.assertIn(key, modified_data)

if __name__ == '__main__':
    unittest.main()
