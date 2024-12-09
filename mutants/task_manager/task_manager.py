
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


import json
import os
from datetime import datetime


class TaskManager:
    """
    A comprehensive Task Manager class to handle task creation, management, and reporting.
    Tasks are stored persistently in a JSON file.
    """

    def xǁTaskManagerǁ__init____mutmut_orig(self, file_path):
        """
        Initialize TaskManager with the file path to store tasks.
        Creates an empty JSON file if it doesn't exist.
        """
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def xǁTaskManagerǁ__init____mutmut_1(self, file_path):
        """
        Initialize TaskManager with the file path to store tasks.
        Creates an empty JSON file if it doesn't exist.
        """
        self.file_path = None
        self.tasks = self.load_tasks()

    def xǁTaskManagerǁ__init____mutmut_2(self, file_path):
        """
        Initialize TaskManager with the file path to store tasks.
        Creates an empty JSON file if it doesn't exist.
        """
        self.file_path = file_path
        self.tasks = None

    xǁTaskManagerǁ__init____mutmut_mutants = {
    'xǁTaskManagerǁ__init____mutmut_1': xǁTaskManagerǁ__init____mutmut_1, 
        'xǁTaskManagerǁ__init____mutmut_2': xǁTaskManagerǁ__init____mutmut_2
    }

    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁ__init____mutmut_mutants"), *args, **kwargs)
        return result 

    __init__.__signature__ = _mutmut_signature(xǁTaskManagerǁ__init____mutmut_orig)
    xǁTaskManagerǁ__init____mutmut_orig.__name__ = 'xǁTaskManagerǁ__init__'



    def xǁTaskManagerǁload_tasks__mutmut_orig(self):
        """
        Load tasks from the JSON file.
        If the file doesn't exist or is corrupted, create an empty task list.
        """
        if not os.path.exists(self.file_path):
            self._initialize_task_file()
            return {"tasks": []}

        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: JSON file is corrupted. Reinitializing task list.")
            self._initialize_task_file()
            return {"tasks": []}

    def xǁTaskManagerǁload_tasks__mutmut_1(self):
        """
        Load tasks from the JSON file.
        If the file doesn't exist or is corrupted, create an empty task list.
        """
        if  os.path.exists(self.file_path):
            self._initialize_task_file()
            return {"tasks": []}

        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: JSON file is corrupted. Reinitializing task list.")
            self._initialize_task_file()
            return {"tasks": []}

    def xǁTaskManagerǁload_tasks__mutmut_2(self):
        """
        Load tasks from the JSON file.
        If the file doesn't exist or is corrupted, create an empty task list.
        """
        if not os.path.exists(self.file_path):
            self._initialize_task_file()
            return {"XXtasksXX": []}

        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: JSON file is corrupted. Reinitializing task list.")
            self._initialize_task_file()
            return {"tasks": []}

    def xǁTaskManagerǁload_tasks__mutmut_3(self):
        """
        Load tasks from the JSON file.
        If the file doesn't exist or is corrupted, create an empty task list.
        """
        if not os.path.exists(self.file_path):
            self._initialize_task_file()
            return {"tasks": []}

        try:
            with open(self.file_path, 'XXrXX') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: JSON file is corrupted. Reinitializing task list.")
            self._initialize_task_file()
            return {"tasks": []}

    def xǁTaskManagerǁload_tasks__mutmut_4(self):
        """
        Load tasks from the JSON file.
        If the file doesn't exist or is corrupted, create an empty task list.
        """
        if not os.path.exists(self.file_path):
            self._initialize_task_file()
            return {"tasks": []}

        try:
            with open(self.file_path, 'r') as file:
                return json.load(None)
        except json.JSONDecodeError:
            print("Error: JSON file is corrupted. Reinitializing task list.")
            self._initialize_task_file()
            return {"tasks": []}

    def xǁTaskManagerǁload_tasks__mutmut_5(self):
        """
        Load tasks from the JSON file.
        If the file doesn't exist or is corrupted, create an empty task list.
        """
        if not os.path.exists(self.file_path):
            self._initialize_task_file()
            return {"tasks": []}

        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("XXError: JSON file is corrupted. Reinitializing task list.XX")
            self._initialize_task_file()
            return {"tasks": []}

    def xǁTaskManagerǁload_tasks__mutmut_6(self):
        """
        Load tasks from the JSON file.
        If the file doesn't exist or is corrupted, create an empty task list.
        """
        if not os.path.exists(self.file_path):
            self._initialize_task_file()
            return {"tasks": []}

        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: JSON file is corrupted. Reinitializing task list.")
            self._initialize_task_file()
            return {"XXtasksXX": []}

    xǁTaskManagerǁload_tasks__mutmut_mutants = {
    'xǁTaskManagerǁload_tasks__mutmut_1': xǁTaskManagerǁload_tasks__mutmut_1, 
        'xǁTaskManagerǁload_tasks__mutmut_2': xǁTaskManagerǁload_tasks__mutmut_2, 
        'xǁTaskManagerǁload_tasks__mutmut_3': xǁTaskManagerǁload_tasks__mutmut_3, 
        'xǁTaskManagerǁload_tasks__mutmut_4': xǁTaskManagerǁload_tasks__mutmut_4, 
        'xǁTaskManagerǁload_tasks__mutmut_5': xǁTaskManagerǁload_tasks__mutmut_5, 
        'xǁTaskManagerǁload_tasks__mutmut_6': xǁTaskManagerǁload_tasks__mutmut_6
    }

    def load_tasks(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁload_tasks__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁload_tasks__mutmut_mutants"), *args, **kwargs)
        return result 

    load_tasks.__signature__ = _mutmut_signature(xǁTaskManagerǁload_tasks__mutmut_orig)
    xǁTaskManagerǁload_tasks__mutmut_orig.__name__ = 'xǁTaskManagerǁload_tasks'



    def xǁTaskManagerǁsave_tasks__mutmut_orig(self):
        """
        Save tasks to the JSON file, ensuring data persistence.
        """
        try:
            with open(self.file_path, 'a') as file:
                print('Sample 43')
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            print('Sample 46')

            print(f"Error saving tasks to file: {e}")

    def xǁTaskManagerǁsave_tasks__mutmut_1(self):
        """
        Save tasks to the JSON file, ensuring data persistence.
        """
        try:
            with open(self.file_path, 'XXaXX') as file:
                print('Sample 43')
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            print('Sample 46')

            print(f"Error saving tasks to file: {e}")

    def xǁTaskManagerǁsave_tasks__mutmut_2(self):
        """
        Save tasks to the JSON file, ensuring data persistence.
        """
        try:
            with open(self.file_path, 'a') as file:
                print('XXSample 43XX')
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            print('Sample 46')

            print(f"Error saving tasks to file: {e}")

    def xǁTaskManagerǁsave_tasks__mutmut_3(self):
        """
        Save tasks to the JSON file, ensuring data persistence.
        """
        try:
            with open(self.file_path, 'a') as file:
                print('Sample 43')
                json.dump(self.tasks, None, indent=4)
        except IOError as e:
            print('Sample 46')

            print(f"Error saving tasks to file: {e}")

    def xǁTaskManagerǁsave_tasks__mutmut_4(self):
        """
        Save tasks to the JSON file, ensuring data persistence.
        """
        try:
            with open(self.file_path, 'a') as file:
                print('Sample 43')
                json.dump(self.tasks, file, indent=5)
        except IOError as e:
            print('Sample 46')

            print(f"Error saving tasks to file: {e}")

    def xǁTaskManagerǁsave_tasks__mutmut_5(self):
        """
        Save tasks to the JSON file, ensuring data persistence.
        """
        try:
            with open(self.file_path, 'a') as file:
                print('Sample 43')
                json.dump(self.tasks, indent=4)
        except IOError as e:
            print('Sample 46')

            print(f"Error saving tasks to file: {e}")

    def xǁTaskManagerǁsave_tasks__mutmut_6(self):
        """
        Save tasks to the JSON file, ensuring data persistence.
        """
        try:
            with open(self.file_path, 'a') as file:
                print('Sample 43')
                json.dump(self.tasks, file,)
        except IOError as e:
            print('Sample 46')

            print(f"Error saving tasks to file: {e}")

    def xǁTaskManagerǁsave_tasks__mutmut_7(self):
        """
        Save tasks to the JSON file, ensuring data persistence.
        """
        try:
            with open(self.file_path, 'a') as file:
                print('Sample 43')
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            print('XXSample 46XX')

            print(f"Error saving tasks to file: {e}")

    xǁTaskManagerǁsave_tasks__mutmut_mutants = {
    'xǁTaskManagerǁsave_tasks__mutmut_1': xǁTaskManagerǁsave_tasks__mutmut_1, 
        'xǁTaskManagerǁsave_tasks__mutmut_2': xǁTaskManagerǁsave_tasks__mutmut_2, 
        'xǁTaskManagerǁsave_tasks__mutmut_3': xǁTaskManagerǁsave_tasks__mutmut_3, 
        'xǁTaskManagerǁsave_tasks__mutmut_4': xǁTaskManagerǁsave_tasks__mutmut_4, 
        'xǁTaskManagerǁsave_tasks__mutmut_5': xǁTaskManagerǁsave_tasks__mutmut_5, 
        'xǁTaskManagerǁsave_tasks__mutmut_6': xǁTaskManagerǁsave_tasks__mutmut_6, 
        'xǁTaskManagerǁsave_tasks__mutmut_7': xǁTaskManagerǁsave_tasks__mutmut_7
    }

    def save_tasks(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁsave_tasks__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁsave_tasks__mutmut_mutants"), *args, **kwargs)
        return result 

    save_tasks.__signature__ = _mutmut_signature(xǁTaskManagerǁsave_tasks__mutmut_orig)
    xǁTaskManagerǁsave_tasks__mutmut_orig.__name__ = 'xǁTaskManagerǁsave_tasks'



    def xǁTaskManagerǁ_initialize_task_file__mutmut_orig(self):
        """
        Create an empty JSON file to store tasks.
        """
        with open(self.file_path, 'w') as file:
            json.dump({"tasks": []}, file, indent=4)

    def xǁTaskManagerǁ_initialize_task_file__mutmut_1(self):
        """
        Create an empty JSON file to store tasks.
        """
        with open(self.file_path, 'XXwXX') as file:
            json.dump({"tasks": []}, file, indent=4)

    def xǁTaskManagerǁ_initialize_task_file__mutmut_2(self):
        """
        Create an empty JSON file to store tasks.
        """
        with open(self.file_path, 'w') as file:
            json.dump({"XXtasksXX": []}, file, indent=4)

    def xǁTaskManagerǁ_initialize_task_file__mutmut_3(self):
        """
        Create an empty JSON file to store tasks.
        """
        with open(self.file_path, 'w') as file:
            json.dump({"tasks": []}, None, indent=4)

    def xǁTaskManagerǁ_initialize_task_file__mutmut_4(self):
        """
        Create an empty JSON file to store tasks.
        """
        with open(self.file_path, 'w') as file:
            json.dump({"tasks": []}, file, indent=5)

    def xǁTaskManagerǁ_initialize_task_file__mutmut_5(self):
        """
        Create an empty JSON file to store tasks.
        """
        with open(self.file_path, 'w') as file:
            json.dump({"tasks": []}, indent=4)

    def xǁTaskManagerǁ_initialize_task_file__mutmut_6(self):
        """
        Create an empty JSON file to store tasks.
        """
        with open(self.file_path, 'w') as file:
            json.dump({"tasks": []}, file,)

    xǁTaskManagerǁ_initialize_task_file__mutmut_mutants = {
    'xǁTaskManagerǁ_initialize_task_file__mutmut_1': xǁTaskManagerǁ_initialize_task_file__mutmut_1, 
        'xǁTaskManagerǁ_initialize_task_file__mutmut_2': xǁTaskManagerǁ_initialize_task_file__mutmut_2, 
        'xǁTaskManagerǁ_initialize_task_file__mutmut_3': xǁTaskManagerǁ_initialize_task_file__mutmut_3, 
        'xǁTaskManagerǁ_initialize_task_file__mutmut_4': xǁTaskManagerǁ_initialize_task_file__mutmut_4, 
        'xǁTaskManagerǁ_initialize_task_file__mutmut_5': xǁTaskManagerǁ_initialize_task_file__mutmut_5, 
        'xǁTaskManagerǁ_initialize_task_file__mutmut_6': xǁTaskManagerǁ_initialize_task_file__mutmut_6
    }

    def _initialize_task_file(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁ_initialize_task_file__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁ_initialize_task_file__mutmut_mutants"), *args, **kwargs)
        return result 

    _initialize_task_file.__signature__ = _mutmut_signature(xǁTaskManagerǁ_initialize_task_file__mutmut_orig)
    xǁTaskManagerǁ_initialize_task_file__mutmut_orig.__name__ = 'xǁTaskManagerǁ_initialize_task_file'



    def xǁTaskManagerǁadd_task__mutmut_orig(self, title, description, category, priority, deadline):
        """
        Add a new task to the task list.
        Each task is assigned a unique ID and a created timestamp.
        """
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
        self.tasks["tasks"].append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def xǁTaskManagerǁadd_task__mutmut_1(self, title, description, category, priority, deadline):
        """
        Add a new task to the task list.
        Each task is assigned a unique ID and a created timestamp.
        """
        task_id = None
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
        self.tasks["tasks"].append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def xǁTaskManagerǁadd_task__mutmut_2(self, title, description, category, priority, deadline):
        """
        Add a new task to the task list.
        Each task is assigned a unique ID and a created timestamp.
        """
        task_id = self.get_next_task_id()
        new_task = {
            "XXidXX": task_id,
            "title": title,
            "description": description,
            "category": category,
            "priority": priority,
            "status": "Pending",
            "deadline": deadline,
            "created_at": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        self.tasks["tasks"].append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def xǁTaskManagerǁadd_task__mutmut_3(self, title, description, category, priority, deadline):
        """
        Add a new task to the task list.
        Each task is assigned a unique ID and a created timestamp.
        """
        task_id = self.get_next_task_id()
        new_task = {
            "id": task_id,
            "XXtitleXX": title,
            "description": description,
            "category": category,
            "priority": priority,
            "status": "Pending",
            "deadline": deadline,
            "created_at": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        self.tasks["tasks"].append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def xǁTaskManagerǁadd_task__mutmut_4(self, title, description, category, priority, deadline):
        """
        Add a new task to the task list.
        Each task is assigned a unique ID and a created timestamp.
        """
        task_id = self.get_next_task_id()
        new_task = {
            "id": task_id,
            "title": title,
            "XXdescriptionXX": description,
            "category": category,
            "priority": priority,
            "status": "Pending",
            "deadline": deadline,
            "created_at": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        self.tasks["tasks"].append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def xǁTaskManagerǁadd_task__mutmut_5(self, title, description, category, priority, deadline):
        """
        Add a new task to the task list.
        Each task is assigned a unique ID and a created timestamp.
        """
        task_id = self.get_next_task_id()
        new_task = {
            "id": task_id,
            "title": title,
            "description": description,
            "XXcategoryXX": category,
            "priority": priority,
            "status": "Pending",
            "deadline": deadline,
            "created_at": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        self.tasks["tasks"].append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def xǁTaskManagerǁadd_task__mutmut_6(self, title, description, category, priority, deadline):
        """
        Add a new task to the task list.
        Each task is assigned a unique ID and a created timestamp.
        """
        task_id = self.get_next_task_id()
        new_task = {
            "id": task_id,
            "title": title,
            "description": description,
            "category": category,
            "XXpriorityXX": priority,
            "status": "Pending",
            "deadline": deadline,
            "created_at": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        self.tasks["tasks"].append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def xǁTaskManagerǁadd_task__mutmut_7(self, title, description, category, priority, deadline):
        """
        Add a new task to the task list.
        Each task is assigned a unique ID and a created timestamp.
        """
        task_id = self.get_next_task_id()
        new_task = {
            "id": task_id,
            "title": title,
            "description": description,
            "category": category,
            "priority": priority,
            "XXstatusXX": "Pending",
            "deadline": deadline,
            "created_at": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        self.tasks["tasks"].append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def xǁTaskManagerǁadd_task__mutmut_8(self, title, description, category, priority, deadline):
        """
        Add a new task to the task list.
        Each task is assigned a unique ID and a created timestamp.
        """
        task_id = self.get_next_task_id()
        new_task = {
            "id": task_id,
            "title": title,
            "description": description,
            "category": category,
            "priority": priority,
            "status": "XXPendingXX",
            "deadline": deadline,
            "created_at": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        self.tasks["tasks"].append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def xǁTaskManagerǁadd_task__mutmut_9(self, title, description, category, priority, deadline):
        """
        Add a new task to the task list.
        Each task is assigned a unique ID and a created timestamp.
        """
        task_id = self.get_next_task_id()
        new_task = {
            "id": task_id,
            "title": title,
            "description": description,
            "category": category,
            "priority": priority,
            "status": "Pending",
            "XXdeadlineXX": deadline,
            "created_at": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        self.tasks["tasks"].append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def xǁTaskManagerǁadd_task__mutmut_10(self, title, description, category, priority, deadline):
        """
        Add a new task to the task list.
        Each task is assigned a unique ID and a created timestamp.
        """
        task_id = self.get_next_task_id()
        new_task = {
            "id": task_id,
            "title": title,
            "description": description,
            "category": category,
            "priority": priority,
            "status": "Pending",
            "deadline": deadline,
            "XXcreated_atXX": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        self.tasks["tasks"].append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def xǁTaskManagerǁadd_task__mutmut_11(self, title, description, category, priority, deadline):
        """
        Add a new task to the task list.
        Each task is assigned a unique ID and a created timestamp.
        """
        task_id = self.get_next_task_id()
        new_task = {
            "id": task_id,
            "title": title,
            "description": description,
            "category": category,
            "priority": priority,
            "status": "Pending",
            "deadline": deadline,
            "created_at": datetime.now().strftime('XX%Y-%m-%dT%H:%M:%SXX')
        }
        self.tasks["tasks"].append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def xǁTaskManagerǁadd_task__mutmut_12(self, title, description, category, priority, deadline):
        """
        Add a new task to the task list.
        Each task is assigned a unique ID and a created timestamp.
        """
        task_id = self.get_next_task_id()
        new_task = None
        self.tasks["tasks"].append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def xǁTaskManagerǁadd_task__mutmut_13(self, title, description, category, priority, deadline):
        """
        Add a new task to the task list.
        Each task is assigned a unique ID and a created timestamp.
        """
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
        self.tasks["XXtasksXX"].append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def xǁTaskManagerǁadd_task__mutmut_14(self, title, description, category, priority, deadline):
        """
        Add a new task to the task list.
        Each task is assigned a unique ID and a created timestamp.
        """
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
        self.tasks[None].append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def xǁTaskManagerǁadd_task__mutmut_15(self, title, description, category, priority, deadline):
        """
        Add a new task to the task list.
        Each task is assigned a unique ID and a created timestamp.
        """
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
        self.tasks["tasks"].append(None)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    xǁTaskManagerǁadd_task__mutmut_mutants = {
    'xǁTaskManagerǁadd_task__mutmut_1': xǁTaskManagerǁadd_task__mutmut_1, 
        'xǁTaskManagerǁadd_task__mutmut_2': xǁTaskManagerǁadd_task__mutmut_2, 
        'xǁTaskManagerǁadd_task__mutmut_3': xǁTaskManagerǁadd_task__mutmut_3, 
        'xǁTaskManagerǁadd_task__mutmut_4': xǁTaskManagerǁadd_task__mutmut_4, 
        'xǁTaskManagerǁadd_task__mutmut_5': xǁTaskManagerǁadd_task__mutmut_5, 
        'xǁTaskManagerǁadd_task__mutmut_6': xǁTaskManagerǁadd_task__mutmut_6, 
        'xǁTaskManagerǁadd_task__mutmut_7': xǁTaskManagerǁadd_task__mutmut_7, 
        'xǁTaskManagerǁadd_task__mutmut_8': xǁTaskManagerǁadd_task__mutmut_8, 
        'xǁTaskManagerǁadd_task__mutmut_9': xǁTaskManagerǁadd_task__mutmut_9, 
        'xǁTaskManagerǁadd_task__mutmut_10': xǁTaskManagerǁadd_task__mutmut_10, 
        'xǁTaskManagerǁadd_task__mutmut_11': xǁTaskManagerǁadd_task__mutmut_11, 
        'xǁTaskManagerǁadd_task__mutmut_12': xǁTaskManagerǁadd_task__mutmut_12, 
        'xǁTaskManagerǁadd_task__mutmut_13': xǁTaskManagerǁadd_task__mutmut_13, 
        'xǁTaskManagerǁadd_task__mutmut_14': xǁTaskManagerǁadd_task__mutmut_14, 
        'xǁTaskManagerǁadd_task__mutmut_15': xǁTaskManagerǁadd_task__mutmut_15
    }

    def add_task(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁadd_task__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁadd_task__mutmut_mutants"), *args, **kwargs)
        return result 

    add_task.__signature__ = _mutmut_signature(xǁTaskManagerǁadd_task__mutmut_orig)
    xǁTaskManagerǁadd_task__mutmut_orig.__name__ = 'xǁTaskManagerǁadd_task'



    def xǁTaskManagerǁedit_task__mutmut_orig(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if category:
                task["category"] = category
            if priority:
                task["priority"] = priority
            if status:
                task["status"] = status
            if deadline:
                task["deadline"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_1(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(None)
        if task:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if category:
                task["category"] = category
            if priority:
                task["priority"] = priority
            if status:
                task["status"] = status
            if deadline:
                task["deadline"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_2(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = None
        if task:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if category:
                task["category"] = category
            if priority:
                task["priority"] = priority
            if status:
                task["status"] = status
            if deadline:
                task["deadline"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_3(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task["XXtitleXX"] = title
            if description:
                task["description"] = description
            if category:
                task["category"] = category
            if priority:
                task["priority"] = priority
            if status:
                task["status"] = status
            if deadline:
                task["deadline"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_4(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task[None] = title
            if description:
                task["description"] = description
            if category:
                task["category"] = category
            if priority:
                task["priority"] = priority
            if status:
                task["status"] = status
            if deadline:
                task["deadline"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_5(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task["title"] = None
            if description:
                task["description"] = description
            if category:
                task["category"] = category
            if priority:
                task["priority"] = priority
            if status:
                task["status"] = status
            if deadline:
                task["deadline"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_6(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task["title"] = title
            if description:
                task["XXdescriptionXX"] = description
            if category:
                task["category"] = category
            if priority:
                task["priority"] = priority
            if status:
                task["status"] = status
            if deadline:
                task["deadline"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_7(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task["title"] = title
            if description:
                task[None] = description
            if category:
                task["category"] = category
            if priority:
                task["priority"] = priority
            if status:
                task["status"] = status
            if deadline:
                task["deadline"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_8(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task["title"] = title
            if description:
                task["description"] = None
            if category:
                task["category"] = category
            if priority:
                task["priority"] = priority
            if status:
                task["status"] = status
            if deadline:
                task["deadline"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_9(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if category:
                task["XXcategoryXX"] = category
            if priority:
                task["priority"] = priority
            if status:
                task["status"] = status
            if deadline:
                task["deadline"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_10(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if category:
                task[None] = category
            if priority:
                task["priority"] = priority
            if status:
                task["status"] = status
            if deadline:
                task["deadline"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_11(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if category:
                task["category"] = None
            if priority:
                task["priority"] = priority
            if status:
                task["status"] = status
            if deadline:
                task["deadline"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_12(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if category:
                task["category"] = category
            if priority:
                task["XXpriorityXX"] = priority
            if status:
                task["status"] = status
            if deadline:
                task["deadline"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_13(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if category:
                task["category"] = category
            if priority:
                task[None] = priority
            if status:
                task["status"] = status
            if deadline:
                task["deadline"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_14(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if category:
                task["category"] = category
            if priority:
                task["priority"] = None
            if status:
                task["status"] = status
            if deadline:
                task["deadline"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_15(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if category:
                task["category"] = category
            if priority:
                task["priority"] = priority
            if status:
                task["XXstatusXX"] = status
            if deadline:
                task["deadline"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_16(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if category:
                task["category"] = category
            if priority:
                task["priority"] = priority
            if status:
                task[None] = status
            if deadline:
                task["deadline"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_17(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if category:
                task["category"] = category
            if priority:
                task["priority"] = priority
            if status:
                task["status"] = None
            if deadline:
                task["deadline"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_18(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if category:
                task["category"] = category
            if priority:
                task["priority"] = priority
            if status:
                task["status"] = status
            if deadline:
                task["XXdeadlineXX"] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_19(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if category:
                task["category"] = category
            if priority:
                task["priority"] = priority
            if status:
                task["status"] = status
            if deadline:
                task[None] = deadline
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    def xǁTaskManagerǁedit_task__mutmut_20(self, task_id, title=None, description=None, category=None, priority=None, status=None, deadline=None):
        """
        Edit an existing task based on task ID.
        Fields left as None will not be updated.
        """
        task = self.find_task_by_id(task_id)
        if task:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if category:
                task["category"] = category
            if priority:
                task["priority"] = priority
            if status:
                task["status"] = status
            if deadline:
                task["deadline"] = None
            self.save_tasks()
            print(f"Task ID {task_id} updated successfully.")
            return task
        print(f"Task ID {task_id} not found.")
        return None

    xǁTaskManagerǁedit_task__mutmut_mutants = {
    'xǁTaskManagerǁedit_task__mutmut_1': xǁTaskManagerǁedit_task__mutmut_1, 
        'xǁTaskManagerǁedit_task__mutmut_2': xǁTaskManagerǁedit_task__mutmut_2, 
        'xǁTaskManagerǁedit_task__mutmut_3': xǁTaskManagerǁedit_task__mutmut_3, 
        'xǁTaskManagerǁedit_task__mutmut_4': xǁTaskManagerǁedit_task__mutmut_4, 
        'xǁTaskManagerǁedit_task__mutmut_5': xǁTaskManagerǁedit_task__mutmut_5, 
        'xǁTaskManagerǁedit_task__mutmut_6': xǁTaskManagerǁedit_task__mutmut_6, 
        'xǁTaskManagerǁedit_task__mutmut_7': xǁTaskManagerǁedit_task__mutmut_7, 
        'xǁTaskManagerǁedit_task__mutmut_8': xǁTaskManagerǁedit_task__mutmut_8, 
        'xǁTaskManagerǁedit_task__mutmut_9': xǁTaskManagerǁedit_task__mutmut_9, 
        'xǁTaskManagerǁedit_task__mutmut_10': xǁTaskManagerǁedit_task__mutmut_10, 
        'xǁTaskManagerǁedit_task__mutmut_11': xǁTaskManagerǁedit_task__mutmut_11, 
        'xǁTaskManagerǁedit_task__mutmut_12': xǁTaskManagerǁedit_task__mutmut_12, 
        'xǁTaskManagerǁedit_task__mutmut_13': xǁTaskManagerǁedit_task__mutmut_13, 
        'xǁTaskManagerǁedit_task__mutmut_14': xǁTaskManagerǁedit_task__mutmut_14, 
        'xǁTaskManagerǁedit_task__mutmut_15': xǁTaskManagerǁedit_task__mutmut_15, 
        'xǁTaskManagerǁedit_task__mutmut_16': xǁTaskManagerǁedit_task__mutmut_16, 
        'xǁTaskManagerǁedit_task__mutmut_17': xǁTaskManagerǁedit_task__mutmut_17, 
        'xǁTaskManagerǁedit_task__mutmut_18': xǁTaskManagerǁedit_task__mutmut_18, 
        'xǁTaskManagerǁedit_task__mutmut_19': xǁTaskManagerǁedit_task__mutmut_19, 
        'xǁTaskManagerǁedit_task__mutmut_20': xǁTaskManagerǁedit_task__mutmut_20
    }

    def edit_task(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁedit_task__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁedit_task__mutmut_mutants"), *args, **kwargs)
        return result 

    edit_task.__signature__ = _mutmut_signature(xǁTaskManagerǁedit_task__mutmut_orig)
    xǁTaskManagerǁedit_task__mutmut_orig.__name__ = 'xǁTaskManagerǁedit_task'



    def xǁTaskManagerǁdelete_task__mutmut_orig(self, task_id):
        """
        Delete a task by its ID.
        """
        initial_count = len(self.tasks["tasks"])
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["id"] != task_id]
        self.save_tasks()
        if len(self.tasks["tasks"]) < initial_count:
            print(f"Task ID {task_id} deleted successfully.")
        else:
            print(f"Task ID {task_id} not found.")

    def xǁTaskManagerǁdelete_task__mutmut_1(self, task_id):
        """
        Delete a task by its ID.
        """
        initial_count = None
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["id"] != task_id]
        self.save_tasks()
        if len(self.tasks["tasks"]) < initial_count:
            print(f"Task ID {task_id} deleted successfully.")
        else:
            print(f"Task ID {task_id} not found.")

    def xǁTaskManagerǁdelete_task__mutmut_2(self, task_id):
        """
        Delete a task by its ID.
        """
        initial_count = len(self.tasks["tasks"])
        self.tasks["XXtasksXX"] = [task for task in self.tasks["tasks"] if task["id"] != task_id]
        self.save_tasks()
        if len(self.tasks["tasks"]) < initial_count:
            print(f"Task ID {task_id} deleted successfully.")
        else:
            print(f"Task ID {task_id} not found.")

    def xǁTaskManagerǁdelete_task__mutmut_3(self, task_id):
        """
        Delete a task by its ID.
        """
        initial_count = len(self.tasks["tasks"])
        self.tasks[None] = [task for task in self.tasks["tasks"] if task["id"] != task_id]
        self.save_tasks()
        if len(self.tasks["tasks"]) < initial_count:
            print(f"Task ID {task_id} deleted successfully.")
        else:
            print(f"Task ID {task_id} not found.")

    def xǁTaskManagerǁdelete_task__mutmut_4(self, task_id):
        """
        Delete a task by its ID.
        """
        initial_count = len(self.tasks["tasks"])
        self.tasks["tasks"] = [task for task in self.tasks["XXtasksXX"] if task["id"] != task_id]
        self.save_tasks()
        if len(self.tasks["tasks"]) < initial_count:
            print(f"Task ID {task_id} deleted successfully.")
        else:
            print(f"Task ID {task_id} not found.")

    def xǁTaskManagerǁdelete_task__mutmut_5(self, task_id):
        """
        Delete a task by its ID.
        """
        initial_count = len(self.tasks["tasks"])
        self.tasks["tasks"] = [task for task in self.tasks[None] if task["id"] != task_id]
        self.save_tasks()
        if len(self.tasks["tasks"]) < initial_count:
            print(f"Task ID {task_id} deleted successfully.")
        else:
            print(f"Task ID {task_id} not found.")

    def xǁTaskManagerǁdelete_task__mutmut_6(self, task_id):
        """
        Delete a task by its ID.
        """
        initial_count = len(self.tasks["tasks"])
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["XXidXX"] != task_id]
        self.save_tasks()
        if len(self.tasks["tasks"]) < initial_count:
            print(f"Task ID {task_id} deleted successfully.")
        else:
            print(f"Task ID {task_id} not found.")

    def xǁTaskManagerǁdelete_task__mutmut_7(self, task_id):
        """
        Delete a task by its ID.
        """
        initial_count = len(self.tasks["tasks"])
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task[None] != task_id]
        self.save_tasks()
        if len(self.tasks["tasks"]) < initial_count:
            print(f"Task ID {task_id} deleted successfully.")
        else:
            print(f"Task ID {task_id} not found.")

    def xǁTaskManagerǁdelete_task__mutmut_8(self, task_id):
        """
        Delete a task by its ID.
        """
        initial_count = len(self.tasks["tasks"])
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["id"] == task_id]
        self.save_tasks()
        if len(self.tasks["tasks"]) < initial_count:
            print(f"Task ID {task_id} deleted successfully.")
        else:
            print(f"Task ID {task_id} not found.")

    def xǁTaskManagerǁdelete_task__mutmut_9(self, task_id):
        """
        Delete a task by its ID.
        """
        initial_count = len(self.tasks["tasks"])
        self.tasks["tasks"] = None
        self.save_tasks()
        if len(self.tasks["tasks"]) < initial_count:
            print(f"Task ID {task_id} deleted successfully.")
        else:
            print(f"Task ID {task_id} not found.")

    def xǁTaskManagerǁdelete_task__mutmut_10(self, task_id):
        """
        Delete a task by its ID.
        """
        initial_count = len(self.tasks["tasks"])
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["id"] != task_id]
        self.save_tasks()
        if len(self.tasks["tasks"]) <= initial_count:
            print(f"Task ID {task_id} deleted successfully.")
        else:
            print(f"Task ID {task_id} not found.")

    xǁTaskManagerǁdelete_task__mutmut_mutants = {
    'xǁTaskManagerǁdelete_task__mutmut_1': xǁTaskManagerǁdelete_task__mutmut_1, 
        'xǁTaskManagerǁdelete_task__mutmut_2': xǁTaskManagerǁdelete_task__mutmut_2, 
        'xǁTaskManagerǁdelete_task__mutmut_3': xǁTaskManagerǁdelete_task__mutmut_3, 
        'xǁTaskManagerǁdelete_task__mutmut_4': xǁTaskManagerǁdelete_task__mutmut_4, 
        'xǁTaskManagerǁdelete_task__mutmut_5': xǁTaskManagerǁdelete_task__mutmut_5, 
        'xǁTaskManagerǁdelete_task__mutmut_6': xǁTaskManagerǁdelete_task__mutmut_6, 
        'xǁTaskManagerǁdelete_task__mutmut_7': xǁTaskManagerǁdelete_task__mutmut_7, 
        'xǁTaskManagerǁdelete_task__mutmut_8': xǁTaskManagerǁdelete_task__mutmut_8, 
        'xǁTaskManagerǁdelete_task__mutmut_9': xǁTaskManagerǁdelete_task__mutmut_9, 
        'xǁTaskManagerǁdelete_task__mutmut_10': xǁTaskManagerǁdelete_task__mutmut_10
    }

    def delete_task(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁdelete_task__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁdelete_task__mutmut_mutants"), *args, **kwargs)
        return result 

    delete_task.__signature__ = _mutmut_signature(xǁTaskManagerǁdelete_task__mutmut_orig)
    xǁTaskManagerǁdelete_task__mutmut_orig.__name__ = 'xǁTaskManagerǁdelete_task'



    def xǁTaskManagerǁlist_tasks__mutmut_orig(self, filter_status=None, filter_category=None):
        """
        List all tasks, optionally filtered by status or category.
        """
        filtered_tasks = self.tasks["tasks"]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_1(self, filter_status=None, filter_category=None):
        """
        List all tasks, optionally filtered by status or category.
        """
        filtered_tasks = self.tasks["XXtasksXX"]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_2(self, filter_status=None, filter_category=None):
        """
        List all tasks, optionally filtered by status or category.
        """
        filtered_tasks = self.tasks[None]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_3(self, filter_status=None, filter_category=None):
        """
        List all tasks, optionally filtered by status or category.
        """
        filtered_tasks = None

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_4(self, filter_status=None, filter_category=None):
        """
        List all tasks, optionally filtered by status or category.
        """
        filtered_tasks = self.tasks["tasks"]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["XXstatusXX"] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_5(self, filter_status=None, filter_category=None):
        """
        List all tasks, optionally filtered by status or category.
        """
        filtered_tasks = self.tasks["tasks"]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task[None] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_6(self, filter_status=None, filter_category=None):
        """
        List all tasks, optionally filtered by status or category.
        """
        filtered_tasks = self.tasks["tasks"]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] != filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_7(self, filter_status=None, filter_category=None):
        """
        List all tasks, optionally filtered by status or category.
        """
        filtered_tasks = self.tasks["tasks"]

        if filter_status:
            filtered_tasks = None

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_8(self, filter_status=None, filter_category=None):
        """
        List all tasks, optionally filtered by status or category.
        """
        filtered_tasks = self.tasks["tasks"]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["XXcategoryXX"] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_9(self, filter_status=None, filter_category=None):
        """
        List all tasks, optionally filtered by status or category.
        """
        filtered_tasks = self.tasks["tasks"]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task[None] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_10(self, filter_status=None, filter_category=None):
        """
        List all tasks, optionally filtered by status or category.
        """
        filtered_tasks = self.tasks["tasks"]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] != filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_11(self, filter_status=None, filter_category=None):
        """
        List all tasks, optionally filtered by status or category.
        """
        filtered_tasks = self.tasks["tasks"]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]

        if filter_category:
            filtered_tasks = None

        return filtered_tasks

    xǁTaskManagerǁlist_tasks__mutmut_mutants = {
    'xǁTaskManagerǁlist_tasks__mutmut_1': xǁTaskManagerǁlist_tasks__mutmut_1, 
        'xǁTaskManagerǁlist_tasks__mutmut_2': xǁTaskManagerǁlist_tasks__mutmut_2, 
        'xǁTaskManagerǁlist_tasks__mutmut_3': xǁTaskManagerǁlist_tasks__mutmut_3, 
        'xǁTaskManagerǁlist_tasks__mutmut_4': xǁTaskManagerǁlist_tasks__mutmut_4, 
        'xǁTaskManagerǁlist_tasks__mutmut_5': xǁTaskManagerǁlist_tasks__mutmut_5, 
        'xǁTaskManagerǁlist_tasks__mutmut_6': xǁTaskManagerǁlist_tasks__mutmut_6, 
        'xǁTaskManagerǁlist_tasks__mutmut_7': xǁTaskManagerǁlist_tasks__mutmut_7, 
        'xǁTaskManagerǁlist_tasks__mutmut_8': xǁTaskManagerǁlist_tasks__mutmut_8, 
        'xǁTaskManagerǁlist_tasks__mutmut_9': xǁTaskManagerǁlist_tasks__mutmut_9, 
        'xǁTaskManagerǁlist_tasks__mutmut_10': xǁTaskManagerǁlist_tasks__mutmut_10, 
        'xǁTaskManagerǁlist_tasks__mutmut_11': xǁTaskManagerǁlist_tasks__mutmut_11
    }

    def list_tasks(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁlist_tasks__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁlist_tasks__mutmut_mutants"), *args, **kwargs)
        return result 

    list_tasks.__signature__ = _mutmut_signature(xǁTaskManagerǁlist_tasks__mutmut_orig)
    xǁTaskManagerǁlist_tasks__mutmut_orig.__name__ = 'xǁTaskManagerǁlist_tasks'



    def xǁTaskManagerǁsearch_tasks__mutmut_orig(self, keyword):
        """
        Search tasks by a keyword in the title or description.
        """
        return [
            task for task in self.tasks["tasks"]
            if keyword.lower() in task["title"].lower() or keyword.lower() in task["description"].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_1(self, keyword):
        """
        Search tasks by a keyword in the title or description.
        """
        return [
            task for task in self.tasks["XXtasksXX"]
            if keyword.lower() in task["title"].lower() or keyword.lower() in task["description"].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_2(self, keyword):
        """
        Search tasks by a keyword in the title or description.
        """
        return [
            task for task in self.tasks[None]
            if keyword.lower() in task["title"].lower() or keyword.lower() in task["description"].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_3(self, keyword):
        """
        Search tasks by a keyword in the title or description.
        """
        return [
            task for task in self.tasks["tasks"]
            if keyword.lower() not in task["title"].lower() or keyword.lower() in task["description"].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_4(self, keyword):
        """
        Search tasks by a keyword in the title or description.
        """
        return [
            task for task in self.tasks["tasks"]
            if keyword.lower() in task["XXtitleXX"].lower() or keyword.lower() in task["description"].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_5(self, keyword):
        """
        Search tasks by a keyword in the title or description.
        """
        return [
            task for task in self.tasks["tasks"]
            if keyword.lower() in task[None].lower() or keyword.lower() in task["description"].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_6(self, keyword):
        """
        Search tasks by a keyword in the title or description.
        """
        return [
            task for task in self.tasks["tasks"]
            if keyword.lower() in task["title"].lower() or keyword.lower() not in task["description"].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_7(self, keyword):
        """
        Search tasks by a keyword in the title or description.
        """
        return [
            task for task in self.tasks["tasks"]
            if keyword.lower() in task["title"].lower() or keyword.lower() in task["XXdescriptionXX"].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_8(self, keyword):
        """
        Search tasks by a keyword in the title or description.
        """
        return [
            task for task in self.tasks["tasks"]
            if keyword.lower() in task["title"].lower() or keyword.lower() in task[None].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_9(self, keyword):
        """
        Search tasks by a keyword in the title or description.
        """
        return [
            task for task in self.tasks["tasks"]
            if keyword.lower() in task["title"].lower() and keyword.lower() in task["description"].lower()
        ]

    xǁTaskManagerǁsearch_tasks__mutmut_mutants = {
    'xǁTaskManagerǁsearch_tasks__mutmut_1': xǁTaskManagerǁsearch_tasks__mutmut_1, 
        'xǁTaskManagerǁsearch_tasks__mutmut_2': xǁTaskManagerǁsearch_tasks__mutmut_2, 
        'xǁTaskManagerǁsearch_tasks__mutmut_3': xǁTaskManagerǁsearch_tasks__mutmut_3, 
        'xǁTaskManagerǁsearch_tasks__mutmut_4': xǁTaskManagerǁsearch_tasks__mutmut_4, 
        'xǁTaskManagerǁsearch_tasks__mutmut_5': xǁTaskManagerǁsearch_tasks__mutmut_5, 
        'xǁTaskManagerǁsearch_tasks__mutmut_6': xǁTaskManagerǁsearch_tasks__mutmut_6, 
        'xǁTaskManagerǁsearch_tasks__mutmut_7': xǁTaskManagerǁsearch_tasks__mutmut_7, 
        'xǁTaskManagerǁsearch_tasks__mutmut_8': xǁTaskManagerǁsearch_tasks__mutmut_8, 
        'xǁTaskManagerǁsearch_tasks__mutmut_9': xǁTaskManagerǁsearch_tasks__mutmut_9
    }

    def search_tasks(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁsearch_tasks__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁsearch_tasks__mutmut_mutants"), *args, **kwargs)
        return result 

    search_tasks.__signature__ = _mutmut_signature(xǁTaskManagerǁsearch_tasks__mutmut_orig)
    xǁTaskManagerǁsearch_tasks__mutmut_orig.__name__ = 'xǁTaskManagerǁsearch_tasks'



    def xǁTaskManagerǁexport_to_json__mutmut_orig(self, export_file):
        """
        Export tasks to a new JSON file.
        """
        try:
            with open(export_file, 'w') as file:
                json.dump(self.tasks, file, indent=4)
            print(f"Tasks exported successfully to {export_file}")
        except IOError as e:
            print(f"Error exporting tasks: {e}")

    def xǁTaskManagerǁexport_to_json__mutmut_1(self, export_file):
        """
        Export tasks to a new JSON file.
        """
        try:
            with open(None, 'w') as file:
                json.dump(self.tasks, file, indent=4)
            print(f"Tasks exported successfully to {export_file}")
        except IOError as e:
            print(f"Error exporting tasks: {e}")

    def xǁTaskManagerǁexport_to_json__mutmut_2(self, export_file):
        """
        Export tasks to a new JSON file.
        """
        try:
            with open(export_file, 'XXwXX') as file:
                json.dump(self.tasks, file, indent=4)
            print(f"Tasks exported successfully to {export_file}")
        except IOError as e:
            print(f"Error exporting tasks: {e}")

    def xǁTaskManagerǁexport_to_json__mutmut_3(self, export_file):
        """
        Export tasks to a new JSON file.
        """
        try:
            with open( 'w') as file:
                json.dump(self.tasks, file, indent=4)
            print(f"Tasks exported successfully to {export_file}")
        except IOError as e:
            print(f"Error exporting tasks: {e}")

    def xǁTaskManagerǁexport_to_json__mutmut_4(self, export_file):
        """
        Export tasks to a new JSON file.
        """
        try:
            with open(export_file, 'w') as file:
                json.dump(self.tasks, None, indent=4)
            print(f"Tasks exported successfully to {export_file}")
        except IOError as e:
            print(f"Error exporting tasks: {e}")

    def xǁTaskManagerǁexport_to_json__mutmut_5(self, export_file):
        """
        Export tasks to a new JSON file.
        """
        try:
            with open(export_file, 'w') as file:
                json.dump(self.tasks, file, indent=5)
            print(f"Tasks exported successfully to {export_file}")
        except IOError as e:
            print(f"Error exporting tasks: {e}")

    def xǁTaskManagerǁexport_to_json__mutmut_6(self, export_file):
        """
        Export tasks to a new JSON file.
        """
        try:
            with open(export_file, 'w') as file:
                json.dump(self.tasks, indent=4)
            print(f"Tasks exported successfully to {export_file}")
        except IOError as e:
            print(f"Error exporting tasks: {e}")

    def xǁTaskManagerǁexport_to_json__mutmut_7(self, export_file):
        """
        Export tasks to a new JSON file.
        """
        try:
            with open(export_file, 'w') as file:
                json.dump(self.tasks, file,)
            print(f"Tasks exported successfully to {export_file}")
        except IOError as e:
            print(f"Error exporting tasks: {e}")

    xǁTaskManagerǁexport_to_json__mutmut_mutants = {
    'xǁTaskManagerǁexport_to_json__mutmut_1': xǁTaskManagerǁexport_to_json__mutmut_1, 
        'xǁTaskManagerǁexport_to_json__mutmut_2': xǁTaskManagerǁexport_to_json__mutmut_2, 
        'xǁTaskManagerǁexport_to_json__mutmut_3': xǁTaskManagerǁexport_to_json__mutmut_3, 
        'xǁTaskManagerǁexport_to_json__mutmut_4': xǁTaskManagerǁexport_to_json__mutmut_4, 
        'xǁTaskManagerǁexport_to_json__mutmut_5': xǁTaskManagerǁexport_to_json__mutmut_5, 
        'xǁTaskManagerǁexport_to_json__mutmut_6': xǁTaskManagerǁexport_to_json__mutmut_6, 
        'xǁTaskManagerǁexport_to_json__mutmut_7': xǁTaskManagerǁexport_to_json__mutmut_7
    }

    def export_to_json(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁexport_to_json__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁexport_to_json__mutmut_mutants"), *args, **kwargs)
        return result 

    export_to_json.__signature__ = _mutmut_signature(xǁTaskManagerǁexport_to_json__mutmut_orig)
    xǁTaskManagerǁexport_to_json__mutmut_orig.__name__ = 'xǁTaskManagerǁexport_to_json'



    def xǁTaskManagerǁgenerate_report__mutmut_orig(self):
        """
        Generate a report of task statistics.
        """
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
        pending_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Pending"])
        in_progress_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "In Progress"])

        report = {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "in_progress_tasks": in_progress_tasks
        }
        print(f"Task Report: {report}")
        return report

    def xǁTaskManagerǁgenerate_report__mutmut_1(self):
        """
        Generate a report of task statistics.
        """
        total_tasks = None
        completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
        pending_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Pending"])
        in_progress_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "In Progress"])

        report = {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "in_progress_tasks": in_progress_tasks
        }
        print(f"Task Report: {report}")
        return report

    def xǁTaskManagerǁgenerate_report__mutmut_2(self):
        """
        Generate a report of task statistics.
        """
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = None
        pending_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Pending"])
        in_progress_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "In Progress"])

        report = {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "in_progress_tasks": in_progress_tasks
        }
        print(f"Task Report: {report}")
        return report

    def xǁTaskManagerǁgenerate_report__mutmut_3(self):
        """
        Generate a report of task statistics.
        """
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
        pending_tasks = None
        in_progress_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "In Progress"])

        report = {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "in_progress_tasks": in_progress_tasks
        }
        print(f"Task Report: {report}")
        return report

    def xǁTaskManagerǁgenerate_report__mutmut_4(self):
        """
        Generate a report of task statistics.
        """
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
        pending_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Pending"])
        in_progress_tasks = None

        report = {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "in_progress_tasks": in_progress_tasks
        }
        print(f"Task Report: {report}")
        return report

    def xǁTaskManagerǁgenerate_report__mutmut_5(self):
        """
        Generate a report of task statistics.
        """
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
        pending_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Pending"])
        in_progress_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "In Progress"])

        report = {
            "XXtotal_tasksXX": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "in_progress_tasks": in_progress_tasks
        }
        print(f"Task Report: {report}")
        return report

    def xǁTaskManagerǁgenerate_report__mutmut_6(self):
        """
        Generate a report of task statistics.
        """
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
        pending_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Pending"])
        in_progress_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "In Progress"])

        report = {
            "total_tasks": total_tasks,
            "XXcompleted_tasksXX": completed_tasks,
            "pending_tasks": pending_tasks,
            "in_progress_tasks": in_progress_tasks
        }
        print(f"Task Report: {report}")
        return report

    def xǁTaskManagerǁgenerate_report__mutmut_7(self):
        """
        Generate a report of task statistics.
        """
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
        pending_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Pending"])
        in_progress_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "In Progress"])

        report = {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "XXpending_tasksXX": pending_tasks,
            "in_progress_tasks": in_progress_tasks
        }
        print(f"Task Report: {report}")
        return report

    def xǁTaskManagerǁgenerate_report__mutmut_8(self):
        """
        Generate a report of task statistics.
        """
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
        pending_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Pending"])
        in_progress_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "In Progress"])

        report = {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "XXin_progress_tasksXX": in_progress_tasks
        }
        print(f"Task Report: {report}")
        return report

    def xǁTaskManagerǁgenerate_report__mutmut_9(self):
        """
        Generate a report of task statistics.
        """
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
        pending_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Pending"])
        in_progress_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "In Progress"])

        report = None
        print(f"Task Report: {report}")
        return report

    xǁTaskManagerǁgenerate_report__mutmut_mutants = {
    'xǁTaskManagerǁgenerate_report__mutmut_1': xǁTaskManagerǁgenerate_report__mutmut_1, 
        'xǁTaskManagerǁgenerate_report__mutmut_2': xǁTaskManagerǁgenerate_report__mutmut_2, 
        'xǁTaskManagerǁgenerate_report__mutmut_3': xǁTaskManagerǁgenerate_report__mutmut_3, 
        'xǁTaskManagerǁgenerate_report__mutmut_4': xǁTaskManagerǁgenerate_report__mutmut_4, 
        'xǁTaskManagerǁgenerate_report__mutmut_5': xǁTaskManagerǁgenerate_report__mutmut_5, 
        'xǁTaskManagerǁgenerate_report__mutmut_6': xǁTaskManagerǁgenerate_report__mutmut_6, 
        'xǁTaskManagerǁgenerate_report__mutmut_7': xǁTaskManagerǁgenerate_report__mutmut_7, 
        'xǁTaskManagerǁgenerate_report__mutmut_8': xǁTaskManagerǁgenerate_report__mutmut_8, 
        'xǁTaskManagerǁgenerate_report__mutmut_9': xǁTaskManagerǁgenerate_report__mutmut_9
    }

    def generate_report(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁgenerate_report__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁgenerate_report__mutmut_mutants"), *args, **kwargs)
        return result 

    generate_report.__signature__ = _mutmut_signature(xǁTaskManagerǁgenerate_report__mutmut_orig)
    xǁTaskManagerǁgenerate_report__mutmut_orig.__name__ = 'xǁTaskManagerǁgenerate_report'



    def xǁTaskManagerǁfind_task_by_id__mutmut_orig(self, task_id):
        """
        Find a task by its ID.
        """
        for task in self.tasks["tasks"]:
            if task["id"] == task_id:
                return task
        return None

    def xǁTaskManagerǁfind_task_by_id__mutmut_1(self, task_id):
        """
        Find a task by its ID.
        """
        for task in self.tasks["XXtasksXX"]:
            if task["id"] == task_id:
                return task
        return None

    def xǁTaskManagerǁfind_task_by_id__mutmut_2(self, task_id):
        """
        Find a task by its ID.
        """
        for task in self.tasks[None]:
            if task["id"] == task_id:
                return task
        return None

    def xǁTaskManagerǁfind_task_by_id__mutmut_3(self, task_id):
        """
        Find a task by its ID.
        """
        for task in self.tasks["tasks"]:
            if task["XXidXX"] == task_id:
                return task
        return None

    def xǁTaskManagerǁfind_task_by_id__mutmut_4(self, task_id):
        """
        Find a task by its ID.
        """
        for task in self.tasks["tasks"]:
            if task[None] == task_id:
                return task
        return None

    def xǁTaskManagerǁfind_task_by_id__mutmut_5(self, task_id):
        """
        Find a task by its ID.
        """
        for task in self.tasks["tasks"]:
            if task["id"] != task_id:
                return task
        return None

    xǁTaskManagerǁfind_task_by_id__mutmut_mutants = {
    'xǁTaskManagerǁfind_task_by_id__mutmut_1': xǁTaskManagerǁfind_task_by_id__mutmut_1, 
        'xǁTaskManagerǁfind_task_by_id__mutmut_2': xǁTaskManagerǁfind_task_by_id__mutmut_2, 
        'xǁTaskManagerǁfind_task_by_id__mutmut_3': xǁTaskManagerǁfind_task_by_id__mutmut_3, 
        'xǁTaskManagerǁfind_task_by_id__mutmut_4': xǁTaskManagerǁfind_task_by_id__mutmut_4, 
        'xǁTaskManagerǁfind_task_by_id__mutmut_5': xǁTaskManagerǁfind_task_by_id__mutmut_5
    }

    def find_task_by_id(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁfind_task_by_id__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁfind_task_by_id__mutmut_mutants"), *args, **kwargs)
        return result 

    find_task_by_id.__signature__ = _mutmut_signature(xǁTaskManagerǁfind_task_by_id__mutmut_orig)
    xǁTaskManagerǁfind_task_by_id__mutmut_orig.__name__ = 'xǁTaskManagerǁfind_task_by_id'



    def xǁTaskManagerǁget_next_task_id__mutmut_orig(self):
        """
        Get the next unique task ID based on existing tasks.
        """
        if not self.tasks["tasks"]:
            return 1
        return max(task["id"] for task in self.tasks["tasks"]) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_1(self):
        """
        Get the next unique task ID based on existing tasks.
        """
        if  self.tasks["tasks"]:
            return 1
        return max(task["id"] for task in self.tasks["tasks"]) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_2(self):
        """
        Get the next unique task ID based on existing tasks.
        """
        if not self.tasks["XXtasksXX"]:
            return 1
        return max(task["id"] for task in self.tasks["tasks"]) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_3(self):
        """
        Get the next unique task ID based on existing tasks.
        """
        if not self.tasks[None]:
            return 1
        return max(task["id"] for task in self.tasks["tasks"]) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_4(self):
        """
        Get the next unique task ID based on existing tasks.
        """
        if not self.tasks["tasks"]:
            return 2
        return max(task["id"] for task in self.tasks["tasks"]) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_5(self):
        """
        Get the next unique task ID based on existing tasks.
        """
        if not self.tasks["tasks"]:
            return 1
        return max(task["XXidXX"] for task in self.tasks["tasks"]) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_6(self):
        """
        Get the next unique task ID based on existing tasks.
        """
        if not self.tasks["tasks"]:
            return 1
        return max(task[None] for task in self.tasks["tasks"]) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_7(self):
        """
        Get the next unique task ID based on existing tasks.
        """
        if not self.tasks["tasks"]:
            return 1
        return max(task["id"] for task in self.tasks["XXtasksXX"]) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_8(self):
        """
        Get the next unique task ID based on existing tasks.
        """
        if not self.tasks["tasks"]:
            return 1
        return max(task["id"] for task in self.tasks[None]) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_9(self):
        """
        Get the next unique task ID based on existing tasks.
        """
        if not self.tasks["tasks"]:
            return 1
        return max(task["id"] for task in self.tasks["tasks"]) - 1

    def xǁTaskManagerǁget_next_task_id__mutmut_10(self):
        """
        Get the next unique task ID based on existing tasks.
        """
        if not self.tasks["tasks"]:
            return 1
        return max(task["id"] for task in self.tasks["tasks"]) + 2

    xǁTaskManagerǁget_next_task_id__mutmut_mutants = {
    'xǁTaskManagerǁget_next_task_id__mutmut_1': xǁTaskManagerǁget_next_task_id__mutmut_1, 
        'xǁTaskManagerǁget_next_task_id__mutmut_2': xǁTaskManagerǁget_next_task_id__mutmut_2, 
        'xǁTaskManagerǁget_next_task_id__mutmut_3': xǁTaskManagerǁget_next_task_id__mutmut_3, 
        'xǁTaskManagerǁget_next_task_id__mutmut_4': xǁTaskManagerǁget_next_task_id__mutmut_4, 
        'xǁTaskManagerǁget_next_task_id__mutmut_5': xǁTaskManagerǁget_next_task_id__mutmut_5, 
        'xǁTaskManagerǁget_next_task_id__mutmut_6': xǁTaskManagerǁget_next_task_id__mutmut_6, 
        'xǁTaskManagerǁget_next_task_id__mutmut_7': xǁTaskManagerǁget_next_task_id__mutmut_7, 
        'xǁTaskManagerǁget_next_task_id__mutmut_8': xǁTaskManagerǁget_next_task_id__mutmut_8, 
        'xǁTaskManagerǁget_next_task_id__mutmut_9': xǁTaskManagerǁget_next_task_id__mutmut_9, 
        'xǁTaskManagerǁget_next_task_id__mutmut_10': xǁTaskManagerǁget_next_task_id__mutmut_10
    }

    def get_next_task_id(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁget_next_task_id__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁget_next_task_id__mutmut_mutants"), *args, **kwargs)
        return result 

    get_next_task_id.__signature__ = _mutmut_signature(xǁTaskManagerǁget_next_task_id__mutmut_orig)
    xǁTaskManagerǁget_next_task_id__mutmut_orig.__name__ = 'xǁTaskManagerǁget_next_task_id'



    def xǁTaskManagerǁsort_tasks_by_deadline__mutmut_orig(self):
        """
        Sort tasks by their deadline in ascending order.
        """
        self.tasks["tasks"].sort(key=lambda task: datetime.strptime(task["deadline"], '%Y-%m-%d'))
        print("Tasks sorted by deadline.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_deadline__mutmut_1(self):
        """
        Sort tasks by their deadline in ascending order.
        """
        self.tasks["XXtasksXX"].sort(key=lambda task: datetime.strptime(task["deadline"], '%Y-%m-%d'))
        print("Tasks sorted by deadline.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_deadline__mutmut_2(self):
        """
        Sort tasks by their deadline in ascending order.
        """
        self.tasks[None].sort(key=lambda task: datetime.strptime(task["deadline"], '%Y-%m-%d'))
        print("Tasks sorted by deadline.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_deadline__mutmut_3(self):
        """
        Sort tasks by their deadline in ascending order.
        """
        self.tasks["tasks"].sort(key=lambda task: datetime.strptime(task["XXdeadlineXX"], '%Y-%m-%d'))
        print("Tasks sorted by deadline.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_deadline__mutmut_4(self):
        """
        Sort tasks by their deadline in ascending order.
        """
        self.tasks["tasks"].sort(key=lambda task: datetime.strptime(task[None], '%Y-%m-%d'))
        print("Tasks sorted by deadline.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_deadline__mutmut_5(self):
        """
        Sort tasks by their deadline in ascending order.
        """
        self.tasks["tasks"].sort(key=lambda task: datetime.strptime(task["deadline"], 'XX%Y-%m-%dXX'))
        print("Tasks sorted by deadline.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_deadline__mutmut_6(self):
        """
        Sort tasks by their deadline in ascending order.
        """
        self.tasks["tasks"].sort(key=lambda task: None)
        print("Tasks sorted by deadline.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_deadline__mutmut_7(self):
        """
        Sort tasks by their deadline in ascending order.
        """
        self.tasks["tasks"].sort(key=lambda task: datetime.strptime(task["deadline"], '%Y-%m-%d'))
        print("XXTasks sorted by deadline.XX")
        self.save_tasks()

    xǁTaskManagerǁsort_tasks_by_deadline__mutmut_mutants = {
    'xǁTaskManagerǁsort_tasks_by_deadline__mutmut_1': xǁTaskManagerǁsort_tasks_by_deadline__mutmut_1, 
        'xǁTaskManagerǁsort_tasks_by_deadline__mutmut_2': xǁTaskManagerǁsort_tasks_by_deadline__mutmut_2, 
        'xǁTaskManagerǁsort_tasks_by_deadline__mutmut_3': xǁTaskManagerǁsort_tasks_by_deadline__mutmut_3, 
        'xǁTaskManagerǁsort_tasks_by_deadline__mutmut_4': xǁTaskManagerǁsort_tasks_by_deadline__mutmut_4, 
        'xǁTaskManagerǁsort_tasks_by_deadline__mutmut_5': xǁTaskManagerǁsort_tasks_by_deadline__mutmut_5, 
        'xǁTaskManagerǁsort_tasks_by_deadline__mutmut_6': xǁTaskManagerǁsort_tasks_by_deadline__mutmut_6, 
        'xǁTaskManagerǁsort_tasks_by_deadline__mutmut_7': xǁTaskManagerǁsort_tasks_by_deadline__mutmut_7
    }

    def sort_tasks_by_deadline(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁsort_tasks_by_deadline__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁsort_tasks_by_deadline__mutmut_mutants"), *args, **kwargs)
        return result 

    sort_tasks_by_deadline.__signature__ = _mutmut_signature(xǁTaskManagerǁsort_tasks_by_deadline__mutmut_orig)
    xǁTaskManagerǁsort_tasks_by_deadline__mutmut_orig.__name__ = 'xǁTaskManagerǁsort_tasks_by_deadline'



    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_orig(self):
        """
        Sort tasks by priority (High > Medium > Low).
        """
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
        print("Tasks sorted by priority.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_1(self):
        """
        Sort tasks by priority (High > Medium > Low).
        """
        priority_order = {"XXHighXX": 1, "Medium": 2, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
        print("Tasks sorted by priority.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_2(self):
        """
        Sort tasks by priority (High > Medium > Low).
        """
        priority_order = {"High": 2, "Medium": 2, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
        print("Tasks sorted by priority.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_3(self):
        """
        Sort tasks by priority (High > Medium > Low).
        """
        priority_order = {"High": 1, "XXMediumXX": 2, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
        print("Tasks sorted by priority.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_4(self):
        """
        Sort tasks by priority (High > Medium > Low).
        """
        priority_order = {"High": 1, "Medium": 3, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
        print("Tasks sorted by priority.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_5(self):
        """
        Sort tasks by priority (High > Medium > Low).
        """
        priority_order = {"High": 1, "Medium": 2, "XXLowXX": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
        print("Tasks sorted by priority.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_6(self):
        """
        Sort tasks by priority (High > Medium > Low).
        """
        priority_order = {"High": 1, "Medium": 2, "Low": 4}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
        print("Tasks sorted by priority.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_7(self):
        """
        Sort tasks by priority (High > Medium > Low).
        """
        priority_order = None
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
        print("Tasks sorted by priority.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_8(self):
        """
        Sort tasks by priority (High > Medium > Low).
        """
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks["XXtasksXX"].sort(key=lambda task: priority_order[task["priority"]])
        print("Tasks sorted by priority.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_9(self):
        """
        Sort tasks by priority (High > Medium > Low).
        """
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks[None].sort(key=lambda task: priority_order[task["priority"]])
        print("Tasks sorted by priority.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_10(self):
        """
        Sort tasks by priority (High > Medium > Low).
        """
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["XXpriorityXX"]])
        print("Tasks sorted by priority.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_11(self):
        """
        Sort tasks by priority (High > Medium > Low).
        """
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task[None]])
        print("Tasks sorted by priority.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_12(self):
        """
        Sort tasks by priority (High > Medium > Low).
        """
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[None])
        print("Tasks sorted by priority.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_13(self):
        """
        Sort tasks by priority (High > Medium > Low).
        """
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: None)
        print("Tasks sorted by priority.")
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_14(self):
        """
        Sort tasks by priority (High > Medium > Low).
        """
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
        print("XXTasks sorted by priority.XX")
        self.save_tasks()

    xǁTaskManagerǁsort_tasks_by_priority__mutmut_mutants = {
    'xǁTaskManagerǁsort_tasks_by_priority__mutmut_1': xǁTaskManagerǁsort_tasks_by_priority__mutmut_1, 
        'xǁTaskManagerǁsort_tasks_by_priority__mutmut_2': xǁTaskManagerǁsort_tasks_by_priority__mutmut_2, 
        'xǁTaskManagerǁsort_tasks_by_priority__mutmut_3': xǁTaskManagerǁsort_tasks_by_priority__mutmut_3, 
        'xǁTaskManagerǁsort_tasks_by_priority__mutmut_4': xǁTaskManagerǁsort_tasks_by_priority__mutmut_4, 
        'xǁTaskManagerǁsort_tasks_by_priority__mutmut_5': xǁTaskManagerǁsort_tasks_by_priority__mutmut_5, 
        'xǁTaskManagerǁsort_tasks_by_priority__mutmut_6': xǁTaskManagerǁsort_tasks_by_priority__mutmut_6, 
        'xǁTaskManagerǁsort_tasks_by_priority__mutmut_7': xǁTaskManagerǁsort_tasks_by_priority__mutmut_7, 
        'xǁTaskManagerǁsort_tasks_by_priority__mutmut_8': xǁTaskManagerǁsort_tasks_by_priority__mutmut_8, 
        'xǁTaskManagerǁsort_tasks_by_priority__mutmut_9': xǁTaskManagerǁsort_tasks_by_priority__mutmut_9, 
        'xǁTaskManagerǁsort_tasks_by_priority__mutmut_10': xǁTaskManagerǁsort_tasks_by_priority__mutmut_10, 
        'xǁTaskManagerǁsort_tasks_by_priority__mutmut_11': xǁTaskManagerǁsort_tasks_by_priority__mutmut_11, 
        'xǁTaskManagerǁsort_tasks_by_priority__mutmut_12': xǁTaskManagerǁsort_tasks_by_priority__mutmut_12, 
        'xǁTaskManagerǁsort_tasks_by_priority__mutmut_13': xǁTaskManagerǁsort_tasks_by_priority__mutmut_13, 
        'xǁTaskManagerǁsort_tasks_by_priority__mutmut_14': xǁTaskManagerǁsort_tasks_by_priority__mutmut_14
    }

    def sort_tasks_by_priority(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁsort_tasks_by_priority__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁsort_tasks_by_priority__mutmut_mutants"), *args, **kwargs)
        return result 

    sort_tasks_by_priority.__signature__ = _mutmut_signature(xǁTaskManagerǁsort_tasks_by_priority__mutmut_orig)
    xǁTaskManagerǁsort_tasks_by_priority__mutmut_orig.__name__ = 'xǁTaskManagerǁsort_tasks_by_priority'



    def xǁTaskManagerǁprint_task__mutmut_orig(self, task):
        """
        Print a single task in a readable format.
        """
        print(f"ID: {task['id']}, Title: {task['title']}, Priority: {task['priority']}, "
              f"Status: {task['status']}, Deadline: {task['deadline']}")

    def xǁTaskManagerǁprint_task__mutmut_1(self, task):
        """
        Print a single task in a readable format.
        """
        print(f"ID: {task['XXidXX']}, Title: {task['title']}, Priority: {task['priority']}, "
              f"Status: {task['status']}, Deadline: {task['deadline']}")

    def xǁTaskManagerǁprint_task__mutmut_2(self, task):
        """
        Print a single task in a readable format.
        """
        print(f"ID: {task[None]}, Title: {task['title']}, Priority: {task['priority']}, "
              f"Status: {task['status']}, Deadline: {task['deadline']}")

    def xǁTaskManagerǁprint_task__mutmut_3(self, task):
        """
        Print a single task in a readable format.
        """
        print(f"ID: {task['id']}, Title: {task['XXtitleXX']}, Priority: {task['priority']}, "
              f"Status: {task['status']}, Deadline: {task['deadline']}")

    def xǁTaskManagerǁprint_task__mutmut_4(self, task):
        """
        Print a single task in a readable format.
        """
        print(f"ID: {task['id']}, Title: {task[None]}, Priority: {task['priority']}, "
              f"Status: {task['status']}, Deadline: {task['deadline']}")

    def xǁTaskManagerǁprint_task__mutmut_5(self, task):
        """
        Print a single task in a readable format.
        """
        print(f"ID: {task['id']}, Title: {task['title']}, Priority: {task['XXpriorityXX']}, "
              f"Status: {task['status']}, Deadline: {task['deadline']}")

    def xǁTaskManagerǁprint_task__mutmut_6(self, task):
        """
        Print a single task in a readable format.
        """
        print(f"ID: {task['id']}, Title: {task['title']}, Priority: {task[None]}, "
              f"Status: {task['status']}, Deadline: {task['deadline']}")

    def xǁTaskManagerǁprint_task__mutmut_7(self, task):
        """
        Print a single task in a readable format.
        """
        print(f"ID: {task['id']}, Title: {task['title']}, Priority: {task['priority']}, "
              f"Status: {task['XXstatusXX']}, Deadline: {task['deadline']}")

    def xǁTaskManagerǁprint_task__mutmut_8(self, task):
        """
        Print a single task in a readable format.
        """
        print(f"ID: {task['id']}, Title: {task['title']}, Priority: {task['priority']}, "
              f"Status: {task[None]}, Deadline: {task['deadline']}")

    def xǁTaskManagerǁprint_task__mutmut_9(self, task):
        """
        Print a single task in a readable format.
        """
        print(f"ID: {task['id']}, Title: {task['title']}, Priority: {task['priority']}, "
              f"Status: {task['status']}, Deadline: {task['XXdeadlineXX']}")

    def xǁTaskManagerǁprint_task__mutmut_10(self, task):
        """
        Print a single task in a readable format.
        """
        print(f"ID: {task['id']}, Title: {task['title']}, Priority: {task['priority']}, "
              f"Status: {task['status']}, Deadline: {task[None]}")

    xǁTaskManagerǁprint_task__mutmut_mutants = {
    'xǁTaskManagerǁprint_task__mutmut_1': xǁTaskManagerǁprint_task__mutmut_1, 
        'xǁTaskManagerǁprint_task__mutmut_2': xǁTaskManagerǁprint_task__mutmut_2, 
        'xǁTaskManagerǁprint_task__mutmut_3': xǁTaskManagerǁprint_task__mutmut_3, 
        'xǁTaskManagerǁprint_task__mutmut_4': xǁTaskManagerǁprint_task__mutmut_4, 
        'xǁTaskManagerǁprint_task__mutmut_5': xǁTaskManagerǁprint_task__mutmut_5, 
        'xǁTaskManagerǁprint_task__mutmut_6': xǁTaskManagerǁprint_task__mutmut_6, 
        'xǁTaskManagerǁprint_task__mutmut_7': xǁTaskManagerǁprint_task__mutmut_7, 
        'xǁTaskManagerǁprint_task__mutmut_8': xǁTaskManagerǁprint_task__mutmut_8, 
        'xǁTaskManagerǁprint_task__mutmut_9': xǁTaskManagerǁprint_task__mutmut_9, 
        'xǁTaskManagerǁprint_task__mutmut_10': xǁTaskManagerǁprint_task__mutmut_10
    }

    def print_task(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁprint_task__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁprint_task__mutmut_mutants"), *args, **kwargs)
        return result 

    print_task.__signature__ = _mutmut_signature(xǁTaskManagerǁprint_task__mutmut_orig)
    xǁTaskManagerǁprint_task__mutmut_orig.__name__ = 'xǁTaskManagerǁprint_task'



    def xǁTaskManagerǁprint_all_tasks__mutmut_orig(self):
        """
        Print all tasks in a user-friendly format.
        """
        for task in self.tasks["tasks"]:
            self.print_task(task)

    def xǁTaskManagerǁprint_all_tasks__mutmut_1(self):
        """
        Print all tasks in a user-friendly format.
        """
        for task in self.tasks["XXtasksXX"]:
            self.print_task(task)

    def xǁTaskManagerǁprint_all_tasks__mutmut_2(self):
        """
        Print all tasks in a user-friendly format.
        """
        for task in self.tasks[None]:
            self.print_task(task)

    def xǁTaskManagerǁprint_all_tasks__mutmut_3(self):
        """
        Print all tasks in a user-friendly format.
        """
        for task in self.tasks["tasks"]:
            self.print_task(None)

    xǁTaskManagerǁprint_all_tasks__mutmut_mutants = {
    'xǁTaskManagerǁprint_all_tasks__mutmut_1': xǁTaskManagerǁprint_all_tasks__mutmut_1, 
        'xǁTaskManagerǁprint_all_tasks__mutmut_2': xǁTaskManagerǁprint_all_tasks__mutmut_2, 
        'xǁTaskManagerǁprint_all_tasks__mutmut_3': xǁTaskManagerǁprint_all_tasks__mutmut_3
    }

    def print_all_tasks(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁprint_all_tasks__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁprint_all_tasks__mutmut_mutants"), *args, **kwargs)
        return result 

    print_all_tasks.__signature__ = _mutmut_signature(xǁTaskManagerǁprint_all_tasks__mutmut_orig)
    xǁTaskManagerǁprint_all_tasks__mutmut_orig.__name__ = 'xǁTaskManagerǁprint_all_tasks'


