import json
import os

class JSONProcessor:
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found.")
        self.file_path = file_path

    def load_json(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def validate_json(self, schema):
        data = self.load_json()
        return all(key in data for key in schema)

    def modify_json(self, key, value):
        data = self.load_json()
        data[key] = value
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)
        return data
