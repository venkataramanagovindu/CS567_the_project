
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


# V4
import json
import os
from datetime import datetime, timedelta



class TaskManager:
    def xǁTaskManagerǁ__init____mutmut_orig(self, file_path):
        self.file_path = file_path
        self.tasks = self.load_tasks()
    def xǁTaskManagerǁ__init____mutmut_1(self, file_path):
        self.file_path = None
        self.tasks = self.load_tasks()
    def xǁTaskManagerǁ__init____mutmut_2(self, file_path):
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

    def xǁTaskManagerǁload_tasks__mutmut_1(self):
        if  os.path.exists(self.file_path):
            self._initialize_task_file()
            return {"tasks": []}

        try:
            with open(self.file_path, 'r') as file:
                task_data = json.load(file)
                return task_data
        except json.JSONDecodeError:
            self._initialize_task_file()
            return {"tasks": []}

    def xǁTaskManagerǁload_tasks__mutmut_2(self):
        if not os.path.exists(self.file_path):
            self._initialize_task_file()
            return {"XXtasksXX": []}

        try:
            with open(self.file_path, 'r') as file:
                task_data = json.load(file)
                return task_data
        except json.JSONDecodeError:
            self._initialize_task_file()
            return {"tasks": []}

    def xǁTaskManagerǁload_tasks__mutmut_3(self):
        if not os.path.exists(self.file_path):
            self._initialize_task_file()
            return {"tasks": []}

        try:
            with open(self.file_path, 'XXrXX') as file:
                task_data = json.load(file)
                return task_data
        except json.JSONDecodeError:
            self._initialize_task_file()
            return {"tasks": []}

    def xǁTaskManagerǁload_tasks__mutmut_4(self):
        if not os.path.exists(self.file_path):
            self._initialize_task_file()
            return {"tasks": []}

        try:
            with open(self.file_path, 'r') as file:
                task_data = json.load(None)
                return task_data
        except json.JSONDecodeError:
            self._initialize_task_file()
            return {"tasks": []}

    def xǁTaskManagerǁload_tasks__mutmut_5(self):
        if not os.path.exists(self.file_path):
            self._initialize_task_file()
            return {"tasks": []}

        try:
            with open(self.file_path, 'r') as file:
                task_data = None
                return task_data
        except json.JSONDecodeError:
            self._initialize_task_file()
            return {"tasks": []}

    def xǁTaskManagerǁload_tasks__mutmut_6(self):
        if not os.path.exists(self.file_path):
            self._initialize_task_file()
            return {"tasks": []}

        try:
            with open(self.file_path, 'r') as file:
                task_data = json.load(file)
                return task_data
        except json.JSONDecodeError:
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
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            self.log_error(f"Error saving tasks to file: {e}")

    def xǁTaskManagerǁsave_tasks__mutmut_1(self):
        try:
            with open(self.file_path, 'XXwXX') as file:
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            self.log_error(f"Error saving tasks to file: {e}")

    def xǁTaskManagerǁsave_tasks__mutmut_2(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.tasks, None, indent=4)
        except IOError as e:
            self.log_error(f"Error saving tasks to file: {e}")

    def xǁTaskManagerǁsave_tasks__mutmut_3(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.tasks, file, indent=5)
        except IOError as e:
            self.log_error(f"Error saving tasks to file: {e}")

    def xǁTaskManagerǁsave_tasks__mutmut_4(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.tasks, indent=4)
        except IOError as e:
            self.log_error(f"Error saving tasks to file: {e}")

    def xǁTaskManagerǁsave_tasks__mutmut_5(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.tasks, file,)
        except IOError as e:
            self.log_error(f"Error saving tasks to file: {e}")

    xǁTaskManagerǁsave_tasks__mutmut_mutants = {
    'xǁTaskManagerǁsave_tasks__mutmut_1': xǁTaskManagerǁsave_tasks__mutmut_1, 
        'xǁTaskManagerǁsave_tasks__mutmut_2': xǁTaskManagerǁsave_tasks__mutmut_2, 
        'xǁTaskManagerǁsave_tasks__mutmut_3': xǁTaskManagerǁsave_tasks__mutmut_3, 
        'xǁTaskManagerǁsave_tasks__mutmut_4': xǁTaskManagerǁsave_tasks__mutmut_4, 
        'xǁTaskManagerǁsave_tasks__mutmut_5': xǁTaskManagerǁsave_tasks__mutmut_5
    }

    def save_tasks(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁsave_tasks__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁsave_tasks__mutmut_mutants"), *args, **kwargs)
        return result 

    save_tasks.__signature__ = _mutmut_signature(xǁTaskManagerǁsave_tasks__mutmut_orig)
    xǁTaskManagerǁsave_tasks__mutmut_orig.__name__ = 'xǁTaskManagerǁsave_tasks'



    def xǁTaskManagerǁ_initialize_task_file__mutmut_orig(self):
        with open(self.file_path, 'w') as file:
            default_content = {"tasks": []}
            json.dump(default_content, file, indent=4)

    def xǁTaskManagerǁ_initialize_task_file__mutmut_1(self):
        with open(self.file_path, 'XXwXX') as file:
            default_content = {"tasks": []}
            json.dump(default_content, file, indent=4)

    def xǁTaskManagerǁ_initialize_task_file__mutmut_2(self):
        with open(self.file_path, 'w') as file:
            default_content = {"XXtasksXX": []}
            json.dump(default_content, file, indent=4)

    def xǁTaskManagerǁ_initialize_task_file__mutmut_3(self):
        with open(self.file_path, 'w') as file:
            default_content = None
            json.dump(default_content, file, indent=4)

    def xǁTaskManagerǁ_initialize_task_file__mutmut_4(self):
        with open(self.file_path, 'w') as file:
            default_content = {"tasks": []}
            json.dump(None, file, indent=4)

    def xǁTaskManagerǁ_initialize_task_file__mutmut_5(self):
        with open(self.file_path, 'w') as file:
            default_content = {"tasks": []}
            json.dump(default_content, None, indent=4)

    def xǁTaskManagerǁ_initialize_task_file__mutmut_6(self):
        with open(self.file_path, 'w') as file:
            default_content = {"tasks": []}
            json.dump(default_content, file, indent=5)

    def xǁTaskManagerǁ_initialize_task_file__mutmut_7(self):
        with open(self.file_path, 'w') as file:
            default_content = {"tasks": []}
            json.dump( file, indent=4)

    def xǁTaskManagerǁ_initialize_task_file__mutmut_8(self):
        with open(self.file_path, 'w') as file:
            default_content = {"tasks": []}
            json.dump(default_content, indent=4)

    def xǁTaskManagerǁ_initialize_task_file__mutmut_9(self):
        with open(self.file_path, 'w') as file:
            default_content = {"tasks": []}
            json.dump(default_content, file,)

    xǁTaskManagerǁ_initialize_task_file__mutmut_mutants = {
    'xǁTaskManagerǁ_initialize_task_file__mutmut_1': xǁTaskManagerǁ_initialize_task_file__mutmut_1, 
        'xǁTaskManagerǁ_initialize_task_file__mutmut_2': xǁTaskManagerǁ_initialize_task_file__mutmut_2, 
        'xǁTaskManagerǁ_initialize_task_file__mutmut_3': xǁTaskManagerǁ_initialize_task_file__mutmut_3, 
        'xǁTaskManagerǁ_initialize_task_file__mutmut_4': xǁTaskManagerǁ_initialize_task_file__mutmut_4, 
        'xǁTaskManagerǁ_initialize_task_file__mutmut_5': xǁTaskManagerǁ_initialize_task_file__mutmut_5, 
        'xǁTaskManagerǁ_initialize_task_file__mutmut_6': xǁTaskManagerǁ_initialize_task_file__mutmut_6, 
        'xǁTaskManagerǁ_initialize_task_file__mutmut_7': xǁTaskManagerǁ_initialize_task_file__mutmut_7, 
        'xǁTaskManagerǁ_initialize_task_file__mutmut_8': xǁTaskManagerǁ_initialize_task_file__mutmut_8, 
        'xǁTaskManagerǁ_initialize_task_file__mutmut_9': xǁTaskManagerǁ_initialize_task_file__mutmut_9
    }

    def _initialize_task_file(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁ_initialize_task_file__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁ_initialize_task_file__mutmut_mutants"), *args, **kwargs)
        return result 

    _initialize_task_file.__signature__ = _mutmut_signature(xǁTaskManagerǁ_initialize_task_file__mutmut_orig)
    xǁTaskManagerǁ_initialize_task_file__mutmut_orig.__name__ = 'xǁTaskManagerǁ_initialize_task_file'



    def xǁTaskManagerǁadd_task__mutmut_orig(self, title, description, category, priority, deadline):
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

    def xǁTaskManagerǁadd_task__mutmut_1(self, title, description, category, priority, deadline):
        if  self._validate_title(title):
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

    def xǁTaskManagerǁadd_task__mutmut_2(self, title, description, category, priority, deadline):
        if not self._validate_title(None):
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

    def xǁTaskManagerǁadd_task__mutmut_3(self, title, description, category, priority, deadline):
        if not self._validate_title(title):
            return

        if  self._validate_description(description):
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

    def xǁTaskManagerǁadd_task__mutmut_4(self, title, description, category, priority, deadline):
        if not self._validate_title(title):
            return

        if not self._validate_description(None):
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

    def xǁTaskManagerǁadd_task__mutmut_5(self, title, description, category, priority, deadline):
        if not self._validate_title(title):
            return

        if not self._validate_description(description):
            return

        if  self._is_priority_valid(priority):
            return
        if not self._validate_category(category):
            return

        if not self._validate_date_format(deadline):
            return

        task_id = self.get_next_task_id()
        new_task = self._build_task(task_id, title, description, category, priority, deadline)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_6(self, title, description, category, priority, deadline):
        if not self._validate_title(title):
            return

        if not self._validate_description(description):
            return

        if not self._is_priority_valid(None):
            return
        if not self._validate_category(category):
            return

        if not self._validate_date_format(deadline):
            return

        task_id = self.get_next_task_id()
        new_task = self._build_task(task_id, title, description, category, priority, deadline)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_7(self, title, description, category, priority, deadline):
        if not self._validate_title(title):
            return

        if not self._validate_description(description):
            return

        if not self._is_priority_valid(priority):
            return
        if  self._validate_category(category):
            return

        if not self._validate_date_format(deadline):
            return

        task_id = self.get_next_task_id()
        new_task = self._build_task(task_id, title, description, category, priority, deadline)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_8(self, title, description, category, priority, deadline):
        if not self._validate_title(title):
            return

        if not self._validate_description(description):
            return

        if not self._is_priority_valid(priority):
            return
        if not self._validate_category(None):
            return

        if not self._validate_date_format(deadline):
            return

        task_id = self.get_next_task_id()
        new_task = self._build_task(task_id, title, description, category, priority, deadline)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_9(self, title, description, category, priority, deadline):
        if not self._validate_title(title):
            return

        if not self._validate_description(description):
            return

        if not self._is_priority_valid(priority):
            return
        if not self._validate_category(category):
            return

        if  self._validate_date_format(deadline):
            return

        task_id = self.get_next_task_id()
        new_task = self._build_task(task_id, title, description, category, priority, deadline)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_10(self, title, description, category, priority, deadline):
        if not self._validate_title(title):
            return

        if not self._validate_description(description):
            return

        if not self._is_priority_valid(priority):
            return
        if not self._validate_category(category):
            return

        if not self._validate_date_format(None):
            return

        task_id = self.get_next_task_id()
        new_task = self._build_task(task_id, title, description, category, priority, deadline)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_11(self, title, description, category, priority, deadline):
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

        task_id = None
        new_task = self._build_task(task_id, title, description, category, priority, deadline)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_12(self, title, description, category, priority, deadline):
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
        new_task = self._build_task(None, title, description, category, priority, deadline)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_13(self, title, description, category, priority, deadline):
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
        new_task = self._build_task(task_id, None, description, category, priority, deadline)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_14(self, title, description, category, priority, deadline):
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
        new_task = self._build_task(task_id, title, None, category, priority, deadline)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_15(self, title, description, category, priority, deadline):
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
        new_task = self._build_task(task_id, title, description, None, priority, deadline)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_16(self, title, description, category, priority, deadline):
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
        new_task = self._build_task(task_id, title, description, category, None, deadline)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_17(self, title, description, category, priority, deadline):
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
        new_task = self._build_task(task_id, title, description, category, priority, None)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_18(self, title, description, category, priority, deadline):
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
        new_task = self._build_task( title, description, category, priority, deadline)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_19(self, title, description, category, priority, deadline):
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
        new_task = self._build_task(task_id, description, category, priority, deadline)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_20(self, title, description, category, priority, deadline):
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
        new_task = self._build_task(task_id, title, category, priority, deadline)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_21(self, title, description, category, priority, deadline):
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
        new_task = self._build_task(task_id, title, description, priority, deadline)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_22(self, title, description, category, priority, deadline):
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
        new_task = self._build_task(task_id, title, description, category, deadline)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_23(self, title, description, category, priority, deadline):
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
        new_task = self._build_task(task_id, title, description, category, priority,)
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_24(self, title, description, category, priority, deadline):
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
        new_task = None
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_25(self, title, description, category, priority, deadline):
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
        self.tasks["XXtasksXX"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_26(self, title, description, category, priority, deadline):
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
        self.tasks[None].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁadd_task__mutmut_27(self, title, description, category, priority, deadline):
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
        self.tasks["tasks"].append(None)
        self.save_tasks()

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
        'xǁTaskManagerǁadd_task__mutmut_15': xǁTaskManagerǁadd_task__mutmut_15, 
        'xǁTaskManagerǁadd_task__mutmut_16': xǁTaskManagerǁadd_task__mutmut_16, 
        'xǁTaskManagerǁadd_task__mutmut_17': xǁTaskManagerǁadd_task__mutmut_17, 
        'xǁTaskManagerǁadd_task__mutmut_18': xǁTaskManagerǁadd_task__mutmut_18, 
        'xǁTaskManagerǁadd_task__mutmut_19': xǁTaskManagerǁadd_task__mutmut_19, 
        'xǁTaskManagerǁadd_task__mutmut_20': xǁTaskManagerǁadd_task__mutmut_20, 
        'xǁTaskManagerǁadd_task__mutmut_21': xǁTaskManagerǁadd_task__mutmut_21, 
        'xǁTaskManagerǁadd_task__mutmut_22': xǁTaskManagerǁadd_task__mutmut_22, 
        'xǁTaskManagerǁadd_task__mutmut_23': xǁTaskManagerǁadd_task__mutmut_23, 
        'xǁTaskManagerǁadd_task__mutmut_24': xǁTaskManagerǁadd_task__mutmut_24, 
        'xǁTaskManagerǁadd_task__mutmut_25': xǁTaskManagerǁadd_task__mutmut_25, 
        'xǁTaskManagerǁadd_task__mutmut_26': xǁTaskManagerǁadd_task__mutmut_26, 
        'xǁTaskManagerǁadd_task__mutmut_27': xǁTaskManagerǁadd_task__mutmut_27
    }

    def add_task(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁadd_task__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁadd_task__mutmut_mutants"), *args, **kwargs)
        return result 

    add_task.__signature__ = _mutmut_signature(xǁTaskManagerǁadd_task__mutmut_orig)
    xǁTaskManagerǁadd_task__mutmut_orig.__name__ = 'xǁTaskManagerǁadd_task'



    def xǁTaskManagerǁ_validate_title__mutmut_orig(self, title):
        if not title or len(title.strip()) < 3:
            print("Invalid title: Title must be at least 3 characters long.")
            return False
        return True

    def xǁTaskManagerǁ_validate_title__mutmut_1(self, title):
        if  title or len(title.strip()) < 3:
            print("Invalid title: Title must be at least 3 characters long.")
            return False
        return True

    def xǁTaskManagerǁ_validate_title__mutmut_2(self, title):
        if not title or len(title.strip()) <= 3:
            print("Invalid title: Title must be at least 3 characters long.")
            return False
        return True

    def xǁTaskManagerǁ_validate_title__mutmut_3(self, title):
        if not title or len(title.strip()) < 4:
            print("Invalid title: Title must be at least 3 characters long.")
            return False
        return True

    def xǁTaskManagerǁ_validate_title__mutmut_4(self, title):
        if not title and len(title.strip()) < 3:
            print("Invalid title: Title must be at least 3 characters long.")
            return False
        return True

    def xǁTaskManagerǁ_validate_title__mutmut_5(self, title):
        if not title or len(title.strip()) < 3:
            print("XXInvalid title: Title must be at least 3 characters long.XX")
            return False
        return True

    def xǁTaskManagerǁ_validate_title__mutmut_6(self, title):
        if not title or len(title.strip()) < 3:
            print("Invalid title: Title must be at least 3 characters long.")
            return True
        return True

    def xǁTaskManagerǁ_validate_title__mutmut_7(self, title):
        if not title or len(title.strip()) < 3:
            print("Invalid title: Title must be at least 3 characters long.")
            return False
        return False

    xǁTaskManagerǁ_validate_title__mutmut_mutants = {
    'xǁTaskManagerǁ_validate_title__mutmut_1': xǁTaskManagerǁ_validate_title__mutmut_1, 
        'xǁTaskManagerǁ_validate_title__mutmut_2': xǁTaskManagerǁ_validate_title__mutmut_2, 
        'xǁTaskManagerǁ_validate_title__mutmut_3': xǁTaskManagerǁ_validate_title__mutmut_3, 
        'xǁTaskManagerǁ_validate_title__mutmut_4': xǁTaskManagerǁ_validate_title__mutmut_4, 
        'xǁTaskManagerǁ_validate_title__mutmut_5': xǁTaskManagerǁ_validate_title__mutmut_5, 
        'xǁTaskManagerǁ_validate_title__mutmut_6': xǁTaskManagerǁ_validate_title__mutmut_6, 
        'xǁTaskManagerǁ_validate_title__mutmut_7': xǁTaskManagerǁ_validate_title__mutmut_7
    }

    def _validate_title(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁ_validate_title__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁ_validate_title__mutmut_mutants"), *args, **kwargs)
        return result 

    _validate_title.__signature__ = _mutmut_signature(xǁTaskManagerǁ_validate_title__mutmut_orig)
    xǁTaskManagerǁ_validate_title__mutmut_orig.__name__ = 'xǁTaskManagerǁ_validate_title'



    def xǁTaskManagerǁ_validate_description__mutmut_orig(self, description):
        if not description or len(description.strip()) < 5:
            print("Invalid description: Description must be at least 5 characters long.")
            return False
        return True

    def xǁTaskManagerǁ_validate_description__mutmut_1(self, description):
        if  description or len(description.strip()) < 5:
            print("Invalid description: Description must be at least 5 characters long.")
            return False
        return True

    def xǁTaskManagerǁ_validate_description__mutmut_2(self, description):
        if not description or len(description.strip()) <= 5:
            print("Invalid description: Description must be at least 5 characters long.")
            return False
        return True

    def xǁTaskManagerǁ_validate_description__mutmut_3(self, description):
        if not description or len(description.strip()) < 6:
            print("Invalid description: Description must be at least 5 characters long.")
            return False
        return True

    def xǁTaskManagerǁ_validate_description__mutmut_4(self, description):
        if not description and len(description.strip()) < 5:
            print("Invalid description: Description must be at least 5 characters long.")
            return False
        return True

    def xǁTaskManagerǁ_validate_description__mutmut_5(self, description):
        if not description or len(description.strip()) < 5:
            print("XXInvalid description: Description must be at least 5 characters long.XX")
            return False
        return True

    def xǁTaskManagerǁ_validate_description__mutmut_6(self, description):
        if not description or len(description.strip()) < 5:
            print("Invalid description: Description must be at least 5 characters long.")
            return True
        return True

    def xǁTaskManagerǁ_validate_description__mutmut_7(self, description):
        if not description or len(description.strip()) < 5:
            print("Invalid description: Description must be at least 5 characters long.")
            return False
        return False

    xǁTaskManagerǁ_validate_description__mutmut_mutants = {
    'xǁTaskManagerǁ_validate_description__mutmut_1': xǁTaskManagerǁ_validate_description__mutmut_1, 
        'xǁTaskManagerǁ_validate_description__mutmut_2': xǁTaskManagerǁ_validate_description__mutmut_2, 
        'xǁTaskManagerǁ_validate_description__mutmut_3': xǁTaskManagerǁ_validate_description__mutmut_3, 
        'xǁTaskManagerǁ_validate_description__mutmut_4': xǁTaskManagerǁ_validate_description__mutmut_4, 
        'xǁTaskManagerǁ_validate_description__mutmut_5': xǁTaskManagerǁ_validate_description__mutmut_5, 
        'xǁTaskManagerǁ_validate_description__mutmut_6': xǁTaskManagerǁ_validate_description__mutmut_6, 
        'xǁTaskManagerǁ_validate_description__mutmut_7': xǁTaskManagerǁ_validate_description__mutmut_7
    }

    def _validate_description(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁ_validate_description__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁ_validate_description__mutmut_mutants"), *args, **kwargs)
        return result 

    _validate_description.__signature__ = _mutmut_signature(xǁTaskManagerǁ_validate_description__mutmut_orig)
    xǁTaskManagerǁ_validate_description__mutmut_orig.__name__ = 'xǁTaskManagerǁ_validate_description'



    def xǁTaskManagerǁ_is_priority_valid__mutmut_orig(self, priority):
        valid_priorities = ["High", "Medium", "Low"]
        if priority not in valid_priorities:
            print("Invalid priority level.")
            return False
        return True

    def xǁTaskManagerǁ_is_priority_valid__mutmut_1(self, priority):
        valid_priorities = ["XXHighXX", "Medium", "Low"]
        if priority not in valid_priorities:
            print("Invalid priority level.")
            return False
        return True

    def xǁTaskManagerǁ_is_priority_valid__mutmut_2(self, priority):
        valid_priorities = ["High", "XXMediumXX", "Low"]
        if priority not in valid_priorities:
            print("Invalid priority level.")
            return False
        return True

    def xǁTaskManagerǁ_is_priority_valid__mutmut_3(self, priority):
        valid_priorities = ["High", "Medium", "XXLowXX"]
        if priority not in valid_priorities:
            print("Invalid priority level.")
            return False
        return True

    def xǁTaskManagerǁ_is_priority_valid__mutmut_4(self, priority):
        valid_priorities = None
        if priority not in valid_priorities:
            print("Invalid priority level.")
            return False
        return True

    def xǁTaskManagerǁ_is_priority_valid__mutmut_5(self, priority):
        valid_priorities = ["High", "Medium", "Low"]
        if priority  in valid_priorities:
            print("Invalid priority level.")
            return False
        return True

    def xǁTaskManagerǁ_is_priority_valid__mutmut_6(self, priority):
        valid_priorities = ["High", "Medium", "Low"]
        if priority not in valid_priorities:
            print("XXInvalid priority level.XX")
            return False
        return True

    def xǁTaskManagerǁ_is_priority_valid__mutmut_7(self, priority):
        valid_priorities = ["High", "Medium", "Low"]
        if priority not in valid_priorities:
            print("Invalid priority level.")
            return True
        return True

    def xǁTaskManagerǁ_is_priority_valid__mutmut_8(self, priority):
        valid_priorities = ["High", "Medium", "Low"]
        if priority not in valid_priorities:
            print("Invalid priority level.")
            return False
        return False

    xǁTaskManagerǁ_is_priority_valid__mutmut_mutants = {
    'xǁTaskManagerǁ_is_priority_valid__mutmut_1': xǁTaskManagerǁ_is_priority_valid__mutmut_1, 
        'xǁTaskManagerǁ_is_priority_valid__mutmut_2': xǁTaskManagerǁ_is_priority_valid__mutmut_2, 
        'xǁTaskManagerǁ_is_priority_valid__mutmut_3': xǁTaskManagerǁ_is_priority_valid__mutmut_3, 
        'xǁTaskManagerǁ_is_priority_valid__mutmut_4': xǁTaskManagerǁ_is_priority_valid__mutmut_4, 
        'xǁTaskManagerǁ_is_priority_valid__mutmut_5': xǁTaskManagerǁ_is_priority_valid__mutmut_5, 
        'xǁTaskManagerǁ_is_priority_valid__mutmut_6': xǁTaskManagerǁ_is_priority_valid__mutmut_6, 
        'xǁTaskManagerǁ_is_priority_valid__mutmut_7': xǁTaskManagerǁ_is_priority_valid__mutmut_7, 
        'xǁTaskManagerǁ_is_priority_valid__mutmut_8': xǁTaskManagerǁ_is_priority_valid__mutmut_8
    }

    def _is_priority_valid(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁ_is_priority_valid__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁ_is_priority_valid__mutmut_mutants"), *args, **kwargs)
        return result 

    _is_priority_valid.__signature__ = _mutmut_signature(xǁTaskManagerǁ_is_priority_valid__mutmut_orig)
    xǁTaskManagerǁ_is_priority_valid__mutmut_orig.__name__ = 'xǁTaskManagerǁ_is_priority_valid'



    def xǁTaskManagerǁ_build_task__mutmut_orig(self, task_id, title, description, category, priority, deadline):
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

    def xǁTaskManagerǁ_build_task__mutmut_1(self, task_id, title, description, category, priority, deadline):
        creation_time = datetime.now().strftime('XX%Y-%m-%dT%H:%M:%SXX')
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

    def xǁTaskManagerǁ_build_task__mutmut_2(self, task_id, title, description, category, priority, deadline):
        creation_time = None
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

    def xǁTaskManagerǁ_build_task__mutmut_3(self, task_id, title, description, category, priority, deadline):
        creation_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        task = {
            "XXidXX": task_id,
            "title": title,
            "description": description,
            "category": category,
            "priority": priority,
            "status": "Pending",
            "deadline": deadline,
            "created_at": creation_time
        }
        return task

    def xǁTaskManagerǁ_build_task__mutmut_4(self, task_id, title, description, category, priority, deadline):
        creation_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        task = {
            "id": task_id,
            "XXtitleXX": title,
            "description": description,
            "category": category,
            "priority": priority,
            "status": "Pending",
            "deadline": deadline,
            "created_at": creation_time
        }
        return task

    def xǁTaskManagerǁ_build_task__mutmut_5(self, task_id, title, description, category, priority, deadline):
        creation_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        task = {
            "id": task_id,
            "title": title,
            "XXdescriptionXX": description,
            "category": category,
            "priority": priority,
            "status": "Pending",
            "deadline": deadline,
            "created_at": creation_time
        }
        return task

    def xǁTaskManagerǁ_build_task__mutmut_6(self, task_id, title, description, category, priority, deadline):
        creation_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "XXcategoryXX": category,
            "priority": priority,
            "status": "Pending",
            "deadline": deadline,
            "created_at": creation_time
        }
        return task

    def xǁTaskManagerǁ_build_task__mutmut_7(self, task_id, title, description, category, priority, deadline):
        creation_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "category": category,
            "XXpriorityXX": priority,
            "status": "Pending",
            "deadline": deadline,
            "created_at": creation_time
        }
        return task

    def xǁTaskManagerǁ_build_task__mutmut_8(self, task_id, title, description, category, priority, deadline):
        creation_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "category": category,
            "priority": priority,
            "XXstatusXX": "Pending",
            "deadline": deadline,
            "created_at": creation_time
        }
        return task

    def xǁTaskManagerǁ_build_task__mutmut_9(self, task_id, title, description, category, priority, deadline):
        creation_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "category": category,
            "priority": priority,
            "status": "XXPendingXX",
            "deadline": deadline,
            "created_at": creation_time
        }
        return task

    def xǁTaskManagerǁ_build_task__mutmut_10(self, task_id, title, description, category, priority, deadline):
        creation_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "category": category,
            "priority": priority,
            "status": "Pending",
            "XXdeadlineXX": deadline,
            "created_at": creation_time
        }
        return task

    def xǁTaskManagerǁ_build_task__mutmut_11(self, task_id, title, description, category, priority, deadline):
        creation_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "category": category,
            "priority": priority,
            "status": "Pending",
            "deadline": deadline,
            "XXcreated_atXX": creation_time
        }
        return task

    def xǁTaskManagerǁ_build_task__mutmut_12(self, task_id, title, description, category, priority, deadline):
        creation_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        task = None
        return task

    xǁTaskManagerǁ_build_task__mutmut_mutants = {
    'xǁTaskManagerǁ_build_task__mutmut_1': xǁTaskManagerǁ_build_task__mutmut_1, 
        'xǁTaskManagerǁ_build_task__mutmut_2': xǁTaskManagerǁ_build_task__mutmut_2, 
        'xǁTaskManagerǁ_build_task__mutmut_3': xǁTaskManagerǁ_build_task__mutmut_3, 
        'xǁTaskManagerǁ_build_task__mutmut_4': xǁTaskManagerǁ_build_task__mutmut_4, 
        'xǁTaskManagerǁ_build_task__mutmut_5': xǁTaskManagerǁ_build_task__mutmut_5, 
        'xǁTaskManagerǁ_build_task__mutmut_6': xǁTaskManagerǁ_build_task__mutmut_6, 
        'xǁTaskManagerǁ_build_task__mutmut_7': xǁTaskManagerǁ_build_task__mutmut_7, 
        'xǁTaskManagerǁ_build_task__mutmut_8': xǁTaskManagerǁ_build_task__mutmut_8, 
        'xǁTaskManagerǁ_build_task__mutmut_9': xǁTaskManagerǁ_build_task__mutmut_9, 
        'xǁTaskManagerǁ_build_task__mutmut_10': xǁTaskManagerǁ_build_task__mutmut_10, 
        'xǁTaskManagerǁ_build_task__mutmut_11': xǁTaskManagerǁ_build_task__mutmut_11, 
        'xǁTaskManagerǁ_build_task__mutmut_12': xǁTaskManagerǁ_build_task__mutmut_12
    }

    def _build_task(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁ_build_task__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁ_build_task__mutmut_mutants"), *args, **kwargs)
        return result 

    _build_task.__signature__ = _mutmut_signature(xǁTaskManagerǁ_build_task__mutmut_orig)
    xǁTaskManagerǁ_build_task__mutmut_orig.__name__ = 'xǁTaskManagerǁ_build_task'



    def xǁTaskManagerǁedit_task__mutmut_orig(self, task_id, **kwargs):
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

    def xǁTaskManagerǁedit_task__mutmut_1(self, task_id, **kwargs):
        task = self.find_task_by_id(None)
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

    def xǁTaskManagerǁedit_task__mutmut_2(self, task_id, **kwargs):
        task = None
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

    def xǁTaskManagerǁedit_task__mutmut_3(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if  task:
            print(f"Task with ID {task_id} not found.")
            return

        for key, value in kwargs.items():
            if key in task and value is not None:
                if key == "deadline" and not self._validate_date_format(value):
                    continue
                task[key] = value
        self.log_task_history(task_id, "Edited", kwargs)
        self.save_tasks()

    def xǁTaskManagerǁedit_task__mutmut_4(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        for key, value in kwargs.items():
            if key not in task and value is not None:
                if key == "deadline" and not self._validate_date_format(value):
                    continue
                task[key] = value
        self.log_task_history(task_id, "Edited", kwargs)
        self.save_tasks()

    def xǁTaskManagerǁedit_task__mutmut_5(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        for key, value in kwargs.items():
            if key in task and value is  None:
                if key == "deadline" and not self._validate_date_format(value):
                    continue
                task[key] = value
        self.log_task_history(task_id, "Edited", kwargs)
        self.save_tasks()

    def xǁTaskManagerǁedit_task__mutmut_6(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        for key, value in kwargs.items():
            if key in task or value is not None:
                if key == "deadline" and not self._validate_date_format(value):
                    continue
                task[key] = value
        self.log_task_history(task_id, "Edited", kwargs)
        self.save_tasks()

    def xǁTaskManagerǁedit_task__mutmut_7(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        for key, value in kwargs.items():
            if key in task and value is not None:
                if key != "deadline" and not self._validate_date_format(value):
                    continue
                task[key] = value
        self.log_task_history(task_id, "Edited", kwargs)
        self.save_tasks()

    def xǁTaskManagerǁedit_task__mutmut_8(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        for key, value in kwargs.items():
            if key in task and value is not None:
                if key == "XXdeadlineXX" and not self._validate_date_format(value):
                    continue
                task[key] = value
        self.log_task_history(task_id, "Edited", kwargs)
        self.save_tasks()

    def xǁTaskManagerǁedit_task__mutmut_9(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        for key, value in kwargs.items():
            if key in task and value is not None:
                if key == "deadline" and  self._validate_date_format(value):
                    continue
                task[key] = value
        self.log_task_history(task_id, "Edited", kwargs)
        self.save_tasks()

    def xǁTaskManagerǁedit_task__mutmut_10(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        for key, value in kwargs.items():
            if key in task and value is not None:
                if key == "deadline" and not self._validate_date_format(None):
                    continue
                task[key] = value
        self.log_task_history(task_id, "Edited", kwargs)
        self.save_tasks()

    def xǁTaskManagerǁedit_task__mutmut_11(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        for key, value in kwargs.items():
            if key in task and value is not None:
                if key == "deadline" or not self._validate_date_format(value):
                    continue
                task[key] = value
        self.log_task_history(task_id, "Edited", kwargs)
        self.save_tasks()

    def xǁTaskManagerǁedit_task__mutmut_12(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        for key, value in kwargs.items():
            if key in task and value is not None:
                if key == "deadline" and not self._validate_date_format(value):
                    break
                task[key] = value
        self.log_task_history(task_id, "Edited", kwargs)
        self.save_tasks()

    def xǁTaskManagerǁedit_task__mutmut_13(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        for key, value in kwargs.items():
            if key in task and value is not None:
                if key == "deadline" and not self._validate_date_format(value):
                    continue
                task[None] = value
        self.log_task_history(task_id, "Edited", kwargs)
        self.save_tasks()

    def xǁTaskManagerǁedit_task__mutmut_14(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        for key, value in kwargs.items():
            if key in task and value is not None:
                if key == "deadline" and not self._validate_date_format(value):
                    continue
                task[key] = None
        self.log_task_history(task_id, "Edited", kwargs)
        self.save_tasks()

    def xǁTaskManagerǁedit_task__mutmut_15(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        for key, value in kwargs.items():
            if key in task and value is not None:
                if key == "deadline" and not self._validate_date_format(value):
                    continue
                task[key] = value
        self.log_task_history(None, "Edited", kwargs)
        self.save_tasks()

    def xǁTaskManagerǁedit_task__mutmut_16(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        for key, value in kwargs.items():
            if key in task and value is not None:
                if key == "deadline" and not self._validate_date_format(value):
                    continue
                task[key] = value
        self.log_task_history(task_id, "XXEditedXX", kwargs)
        self.save_tasks()

    def xǁTaskManagerǁedit_task__mutmut_17(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        for key, value in kwargs.items():
            if key in task and value is not None:
                if key == "deadline" and not self._validate_date_format(value):
                    continue
                task[key] = value
        self.log_task_history(task_id, "Edited", None)
        self.save_tasks()

    def xǁTaskManagerǁedit_task__mutmut_18(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        for key, value in kwargs.items():
            if key in task and value is not None:
                if key == "deadline" and not self._validate_date_format(value):
                    continue
                task[key] = value
        self.log_task_history( "Edited", kwargs)
        self.save_tasks()

    def xǁTaskManagerǁedit_task__mutmut_19(self, task_id, **kwargs):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        for key, value in kwargs.items():
            if key in task and value is not None:
                if key == "deadline" and not self._validate_date_format(value):
                    continue
                task[key] = value
        self.log_task_history(task_id, "Edited",)
        self.save_tasks()

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
        'xǁTaskManagerǁedit_task__mutmut_19': xǁTaskManagerǁedit_task__mutmut_19
    }

    def edit_task(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁedit_task__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁedit_task__mutmut_mutants"), *args, **kwargs)
        return result 

    edit_task.__signature__ = _mutmut_signature(xǁTaskManagerǁedit_task__mutmut_orig)
    xǁTaskManagerǁedit_task__mutmut_orig.__name__ = 'xǁTaskManagerǁedit_task'



    def xǁTaskManagerǁlog_task_history__mutmut_orig(self, task_id, action, details):
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

    def xǁTaskManagerǁlog_task_history__mutmut_1(self, task_id, action, details):
        log_entry = {
            "XXtask_idXX": task_id,
            "action": action,
            "details": details,
            "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        try:
            with open("task_history.log", 'a') as log_file:
                log_file.write(json.dumps(log_entry) + "\n")
        except IOError as e:
            print(f"Error logging task history: {e}")

    def xǁTaskManagerǁlog_task_history__mutmut_2(self, task_id, action, details):
        log_entry = {
            "task_id": task_id,
            "XXactionXX": action,
            "details": details,
            "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        try:
            with open("task_history.log", 'a') as log_file:
                log_file.write(json.dumps(log_entry) + "\n")
        except IOError as e:
            print(f"Error logging task history: {e}")

    def xǁTaskManagerǁlog_task_history__mutmut_3(self, task_id, action, details):
        log_entry = {
            "task_id": task_id,
            "action": action,
            "XXdetailsXX": details,
            "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        try:
            with open("task_history.log", 'a') as log_file:
                log_file.write(json.dumps(log_entry) + "\n")
        except IOError as e:
            print(f"Error logging task history: {e}")

    def xǁTaskManagerǁlog_task_history__mutmut_4(self, task_id, action, details):
        log_entry = {
            "task_id": task_id,
            "action": action,
            "details": details,
            "XXtimestampXX": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        try:
            with open("task_history.log", 'a') as log_file:
                log_file.write(json.dumps(log_entry) + "\n")
        except IOError as e:
            print(f"Error logging task history: {e}")

    def xǁTaskManagerǁlog_task_history__mutmut_5(self, task_id, action, details):
        log_entry = {
            "task_id": task_id,
            "action": action,
            "details": details,
            "timestamp": datetime.now().strftime('XX%Y-%m-%dT%H:%M:%SXX')
        }
        try:
            with open("task_history.log", 'a') as log_file:
                log_file.write(json.dumps(log_entry) + "\n")
        except IOError as e:
            print(f"Error logging task history: {e}")

    def xǁTaskManagerǁlog_task_history__mutmut_6(self, task_id, action, details):
        log_entry = None
        try:
            with open("task_history.log", 'a') as log_file:
                log_file.write(json.dumps(log_entry) + "\n")
        except IOError as e:
            print(f"Error logging task history: {e}")

    def xǁTaskManagerǁlog_task_history__mutmut_7(self, task_id, action, details):
        log_entry = {
            "task_id": task_id,
            "action": action,
            "details": details,
            "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        try:
            with open("XXtask_history.logXX", 'a') as log_file:
                log_file.write(json.dumps(log_entry) + "\n")
        except IOError as e:
            print(f"Error logging task history: {e}")

    def xǁTaskManagerǁlog_task_history__mutmut_8(self, task_id, action, details):
        log_entry = {
            "task_id": task_id,
            "action": action,
            "details": details,
            "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        try:
            with open("task_history.log", 'XXaXX') as log_file:
                log_file.write(json.dumps(log_entry) + "\n")
        except IOError as e:
            print(f"Error logging task history: {e}")

    def xǁTaskManagerǁlog_task_history__mutmut_9(self, task_id, action, details):
        log_entry = {
            "task_id": task_id,
            "action": action,
            "details": details,
            "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        try:
            with open("task_history.log", 'a') as log_file:
                log_file.write(json.dumps(None) + "\n")
        except IOError as e:
            print(f"Error logging task history: {e}")

    def xǁTaskManagerǁlog_task_history__mutmut_10(self, task_id, action, details):
        log_entry = {
            "task_id": task_id,
            "action": action,
            "details": details,
            "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        try:
            with open("task_history.log", 'a') as log_file:
                log_file.write(json.dumps(log_entry) - "\n")
        except IOError as e:
            print(f"Error logging task history: {e}")

    def xǁTaskManagerǁlog_task_history__mutmut_11(self, task_id, action, details):
        log_entry = {
            "task_id": task_id,
            "action": action,
            "details": details,
            "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
        try:
            with open("task_history.log", 'a') as log_file:
                log_file.write(json.dumps(log_entry) + "XX\nXX")
        except IOError as e:
            print(f"Error logging task history: {e}")

    xǁTaskManagerǁlog_task_history__mutmut_mutants = {
    'xǁTaskManagerǁlog_task_history__mutmut_1': xǁTaskManagerǁlog_task_history__mutmut_1, 
        'xǁTaskManagerǁlog_task_history__mutmut_2': xǁTaskManagerǁlog_task_history__mutmut_2, 
        'xǁTaskManagerǁlog_task_history__mutmut_3': xǁTaskManagerǁlog_task_history__mutmut_3, 
        'xǁTaskManagerǁlog_task_history__mutmut_4': xǁTaskManagerǁlog_task_history__mutmut_4, 
        'xǁTaskManagerǁlog_task_history__mutmut_5': xǁTaskManagerǁlog_task_history__mutmut_5, 
        'xǁTaskManagerǁlog_task_history__mutmut_6': xǁTaskManagerǁlog_task_history__mutmut_6, 
        'xǁTaskManagerǁlog_task_history__mutmut_7': xǁTaskManagerǁlog_task_history__mutmut_7, 
        'xǁTaskManagerǁlog_task_history__mutmut_8': xǁTaskManagerǁlog_task_history__mutmut_8, 
        'xǁTaskManagerǁlog_task_history__mutmut_9': xǁTaskManagerǁlog_task_history__mutmut_9, 
        'xǁTaskManagerǁlog_task_history__mutmut_10': xǁTaskManagerǁlog_task_history__mutmut_10, 
        'xǁTaskManagerǁlog_task_history__mutmut_11': xǁTaskManagerǁlog_task_history__mutmut_11
    }

    def log_task_history(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁlog_task_history__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁlog_task_history__mutmut_mutants"), *args, **kwargs)
        return result 

    log_task_history.__signature__ = _mutmut_signature(xǁTaskManagerǁlog_task_history__mutmut_orig)
    xǁTaskManagerǁlog_task_history__mutmut_orig.__name__ = 'xǁTaskManagerǁlog_task_history'



    def xǁTaskManagerǁdelete_task__mutmut_orig(self, task_id):
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["id"] != task_id]
        self.log_task_history(task_id, "Deleted", {})
        self.save_tasks()

    def xǁTaskManagerǁdelete_task__mutmut_1(self, task_id):
        self.tasks["XXtasksXX"] = [task for task in self.tasks["tasks"] if task["id"] != task_id]
        self.log_task_history(task_id, "Deleted", {})
        self.save_tasks()

    def xǁTaskManagerǁdelete_task__mutmut_2(self, task_id):
        self.tasks[None] = [task for task in self.tasks["tasks"] if task["id"] != task_id]
        self.log_task_history(task_id, "Deleted", {})
        self.save_tasks()

    def xǁTaskManagerǁdelete_task__mutmut_3(self, task_id):
        self.tasks["tasks"] = [task for task in self.tasks["XXtasksXX"] if task["id"] != task_id]
        self.log_task_history(task_id, "Deleted", {})
        self.save_tasks()

    def xǁTaskManagerǁdelete_task__mutmut_4(self, task_id):
        self.tasks["tasks"] = [task for task in self.tasks[None] if task["id"] != task_id]
        self.log_task_history(task_id, "Deleted", {})
        self.save_tasks()

    def xǁTaskManagerǁdelete_task__mutmut_5(self, task_id):
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["XXidXX"] != task_id]
        self.log_task_history(task_id, "Deleted", {})
        self.save_tasks()

    def xǁTaskManagerǁdelete_task__mutmut_6(self, task_id):
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task[None] != task_id]
        self.log_task_history(task_id, "Deleted", {})
        self.save_tasks()

    def xǁTaskManagerǁdelete_task__mutmut_7(self, task_id):
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["id"] == task_id]
        self.log_task_history(task_id, "Deleted", {})
        self.save_tasks()

    def xǁTaskManagerǁdelete_task__mutmut_8(self, task_id):
        self.tasks["tasks"] = None
        self.log_task_history(task_id, "Deleted", {})
        self.save_tasks()

    def xǁTaskManagerǁdelete_task__mutmut_9(self, task_id):
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["id"] != task_id]
        self.log_task_history(None, "Deleted", {})
        self.save_tasks()

    def xǁTaskManagerǁdelete_task__mutmut_10(self, task_id):
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["id"] != task_id]
        self.log_task_history(task_id, "XXDeletedXX", {})
        self.save_tasks()

    def xǁTaskManagerǁdelete_task__mutmut_11(self, task_id):
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["id"] != task_id]
        self.log_task_history( "Deleted", {})
        self.save_tasks()

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
        'xǁTaskManagerǁdelete_task__mutmut_10': xǁTaskManagerǁdelete_task__mutmut_10, 
        'xǁTaskManagerǁdelete_task__mutmut_11': xǁTaskManagerǁdelete_task__mutmut_11
    }

    def delete_task(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁdelete_task__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁdelete_task__mutmut_mutants"), *args, **kwargs)
        return result 

    delete_task.__signature__ = _mutmut_signature(xǁTaskManagerǁdelete_task__mutmut_orig)
    xǁTaskManagerǁdelete_task__mutmut_orig.__name__ = 'xǁTaskManagerǁdelete_task'



    def xǁTaskManagerǁreset_task_file__mutmut_orig(self):
        self.tasks = {"tasks": []}
        self.save_tasks()

    def xǁTaskManagerǁreset_task_file__mutmut_1(self):
        self.tasks = {"XXtasksXX": []}
        self.save_tasks()

    def xǁTaskManagerǁreset_task_file__mutmut_2(self):
        self.tasks = None
        self.save_tasks()

    xǁTaskManagerǁreset_task_file__mutmut_mutants = {
    'xǁTaskManagerǁreset_task_file__mutmut_1': xǁTaskManagerǁreset_task_file__mutmut_1, 
        'xǁTaskManagerǁreset_task_file__mutmut_2': xǁTaskManagerǁreset_task_file__mutmut_2
    }

    def reset_task_file(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁreset_task_file__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁreset_task_file__mutmut_mutants"), *args, **kwargs)
        return result 

    reset_task_file.__signature__ = _mutmut_signature(xǁTaskManagerǁreset_task_file__mutmut_orig)
    xǁTaskManagerǁreset_task_file__mutmut_orig.__name__ = 'xǁTaskManagerǁreset_task_file'



    def xǁTaskManagerǁclone_task__mutmut_orig(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        new_task = task.copy()
        new_task["id"] = self.get_next_task_id()
        new_task["created_at"] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁclone_task__mutmut_1(self, task_id):
        task = self.find_task_by_id(None)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        new_task = task.copy()
        new_task["id"] = self.get_next_task_id()
        new_task["created_at"] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁclone_task__mutmut_2(self, task_id):
        task = None
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        new_task = task.copy()
        new_task["id"] = self.get_next_task_id()
        new_task["created_at"] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁclone_task__mutmut_3(self, task_id):
        task = self.find_task_by_id(task_id)
        if  task:
            print(f"Task with ID {task_id} not found.")
            return

        new_task = task.copy()
        new_task["id"] = self.get_next_task_id()
        new_task["created_at"] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁclone_task__mutmut_4(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        new_task = None
        new_task["id"] = self.get_next_task_id()
        new_task["created_at"] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁclone_task__mutmut_5(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        new_task = task.copy()
        new_task["XXidXX"] = self.get_next_task_id()
        new_task["created_at"] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁclone_task__mutmut_6(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        new_task = task.copy()
        new_task[None] = self.get_next_task_id()
        new_task["created_at"] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁclone_task__mutmut_7(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        new_task = task.copy()
        new_task["id"] = None
        new_task["created_at"] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁclone_task__mutmut_8(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        new_task = task.copy()
        new_task["id"] = self.get_next_task_id()
        new_task["XXcreated_atXX"] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁclone_task__mutmut_9(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        new_task = task.copy()
        new_task["id"] = self.get_next_task_id()
        new_task[None] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁclone_task__mutmut_10(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        new_task = task.copy()
        new_task["id"] = self.get_next_task_id()
        new_task["created_at"] = datetime.now().strftime('XX%Y-%m-%dT%H:%M:%SXX')
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁclone_task__mutmut_11(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        new_task = task.copy()
        new_task["id"] = self.get_next_task_id()
        new_task["created_at"] = None
        self.tasks["tasks"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁclone_task__mutmut_12(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        new_task = task.copy()
        new_task["id"] = self.get_next_task_id()
        new_task["created_at"] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.tasks["XXtasksXX"].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁclone_task__mutmut_13(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        new_task = task.copy()
        new_task["id"] = self.get_next_task_id()
        new_task["created_at"] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.tasks[None].append(new_task)
        self.save_tasks()

    def xǁTaskManagerǁclone_task__mutmut_14(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        new_task = task.copy()
        new_task["id"] = self.get_next_task_id()
        new_task["created_at"] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.tasks["tasks"].append(None)
        self.save_tasks()

    xǁTaskManagerǁclone_task__mutmut_mutants = {
    'xǁTaskManagerǁclone_task__mutmut_1': xǁTaskManagerǁclone_task__mutmut_1, 
        'xǁTaskManagerǁclone_task__mutmut_2': xǁTaskManagerǁclone_task__mutmut_2, 
        'xǁTaskManagerǁclone_task__mutmut_3': xǁTaskManagerǁclone_task__mutmut_3, 
        'xǁTaskManagerǁclone_task__mutmut_4': xǁTaskManagerǁclone_task__mutmut_4, 
        'xǁTaskManagerǁclone_task__mutmut_5': xǁTaskManagerǁclone_task__mutmut_5, 
        'xǁTaskManagerǁclone_task__mutmut_6': xǁTaskManagerǁclone_task__mutmut_6, 
        'xǁTaskManagerǁclone_task__mutmut_7': xǁTaskManagerǁclone_task__mutmut_7, 
        'xǁTaskManagerǁclone_task__mutmut_8': xǁTaskManagerǁclone_task__mutmut_8, 
        'xǁTaskManagerǁclone_task__mutmut_9': xǁTaskManagerǁclone_task__mutmut_9, 
        'xǁTaskManagerǁclone_task__mutmut_10': xǁTaskManagerǁclone_task__mutmut_10, 
        'xǁTaskManagerǁclone_task__mutmut_11': xǁTaskManagerǁclone_task__mutmut_11, 
        'xǁTaskManagerǁclone_task__mutmut_12': xǁTaskManagerǁclone_task__mutmut_12, 
        'xǁTaskManagerǁclone_task__mutmut_13': xǁTaskManagerǁclone_task__mutmut_13, 
        'xǁTaskManagerǁclone_task__mutmut_14': xǁTaskManagerǁclone_task__mutmut_14
    }

    def clone_task(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁclone_task__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁclone_task__mutmut_mutants"), *args, **kwargs)
        return result 

    clone_task.__signature__ = _mutmut_signature(xǁTaskManagerǁclone_task__mutmut_orig)
    xǁTaskManagerǁclone_task__mutmut_orig.__name__ = 'xǁTaskManagerǁclone_task'



    def xǁTaskManagerǁlist_tasks__mutmut_orig(self, filter_status=None, filter_category=None):
        filtered_tasks = self.tasks["tasks"]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_1(self, filter_status=None, filter_category=None):
        filtered_tasks = self.tasks["XXtasksXX"]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_2(self, filter_status=None, filter_category=None):
        filtered_tasks = self.tasks[None]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_3(self, filter_status=None, filter_category=None):
        filtered_tasks = None

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_4(self, filter_status=None, filter_category=None):
        filtered_tasks = self.tasks["tasks"]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["XXstatusXX"] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_5(self, filter_status=None, filter_category=None):
        filtered_tasks = self.tasks["tasks"]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task[None] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_6(self, filter_status=None, filter_category=None):
        filtered_tasks = self.tasks["tasks"]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] != filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_7(self, filter_status=None, filter_category=None):
        filtered_tasks = self.tasks["tasks"]

        if filter_status:
            filtered_tasks = None

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_8(self, filter_status=None, filter_category=None):
        filtered_tasks = self.tasks["tasks"]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["XXcategoryXX"] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_9(self, filter_status=None, filter_category=None):
        filtered_tasks = self.tasks["tasks"]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task[None] == filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_10(self, filter_status=None, filter_category=None):
        filtered_tasks = self.tasks["tasks"]

        if filter_status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]

        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] != filter_category]

        return filtered_tasks

    def xǁTaskManagerǁlist_tasks__mutmut_11(self, filter_status=None, filter_category=None):
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
        keyword = keyword.lower()
        return [
            task for task in self.tasks["tasks"]
            if keyword in task["title"].lower() or keyword in task["description"].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_1(self, keyword):
        keyword = None
        return [
            task for task in self.tasks["tasks"]
            if keyword in task["title"].lower() or keyword in task["description"].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_2(self, keyword):
        keyword = keyword.lower()
        return [
            task for task in self.tasks["XXtasksXX"]
            if keyword in task["title"].lower() or keyword in task["description"].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_3(self, keyword):
        keyword = keyword.lower()
        return [
            task for task in self.tasks[None]
            if keyword in task["title"].lower() or keyword in task["description"].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_4(self, keyword):
        keyword = keyword.lower()
        return [
            task for task in self.tasks["tasks"]
            if keyword not in task["title"].lower() or keyword in task["description"].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_5(self, keyword):
        keyword = keyword.lower()
        return [
            task for task in self.tasks["tasks"]
            if keyword in task["XXtitleXX"].lower() or keyword in task["description"].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_6(self, keyword):
        keyword = keyword.lower()
        return [
            task for task in self.tasks["tasks"]
            if keyword in task[None].lower() or keyword in task["description"].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_7(self, keyword):
        keyword = keyword.lower()
        return [
            task for task in self.tasks["tasks"]
            if keyword in task["title"].lower() or keyword not in task["description"].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_8(self, keyword):
        keyword = keyword.lower()
        return [
            task for task in self.tasks["tasks"]
            if keyword in task["title"].lower() or keyword in task["XXdescriptionXX"].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_9(self, keyword):
        keyword = keyword.lower()
        return [
            task for task in self.tasks["tasks"]
            if keyword in task["title"].lower() or keyword in task[None].lower()
        ]

    def xǁTaskManagerǁsearch_tasks__mutmut_10(self, keyword):
        keyword = keyword.lower()
        return [
            task for task in self.tasks["tasks"]
            if keyword in task["title"].lower() and keyword in task["description"].lower()
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
        'xǁTaskManagerǁsearch_tasks__mutmut_9': xǁTaskManagerǁsearch_tasks__mutmut_9, 
        'xǁTaskManagerǁsearch_tasks__mutmut_10': xǁTaskManagerǁsearch_tasks__mutmut_10
    }

    def search_tasks(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁsearch_tasks__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁsearch_tasks__mutmut_mutants"), *args, **kwargs)
        return result 

    search_tasks.__signature__ = _mutmut_signature(xǁTaskManagerǁsearch_tasks__mutmut_orig)
    xǁTaskManagerǁsearch_tasks__mutmut_orig.__name__ = 'xǁTaskManagerǁsearch_tasks'



    def xǁTaskManagerǁexport_to_json__mutmut_orig(self, export_file):
        try:
            with open(export_file, 'w') as file:
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            print(f"Error exporting tasks: {e}")

    def xǁTaskManagerǁexport_to_json__mutmut_1(self, export_file):
        try:
            with open(None, 'w') as file:
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            print(f"Error exporting tasks: {e}")

    def xǁTaskManagerǁexport_to_json__mutmut_2(self, export_file):
        try:
            with open(export_file, 'XXwXX') as file:
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            print(f"Error exporting tasks: {e}")

    def xǁTaskManagerǁexport_to_json__mutmut_3(self, export_file):
        try:
            with open( 'w') as file:
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            print(f"Error exporting tasks: {e}")

    def xǁTaskManagerǁexport_to_json__mutmut_4(self, export_file):
        try:
            with open(export_file, 'w') as file:
                json.dump(self.tasks, None, indent=4)
        except IOError as e:
            print(f"Error exporting tasks: {e}")

    def xǁTaskManagerǁexport_to_json__mutmut_5(self, export_file):
        try:
            with open(export_file, 'w') as file:
                json.dump(self.tasks, file, indent=5)
        except IOError as e:
            print(f"Error exporting tasks: {e}")

    def xǁTaskManagerǁexport_to_json__mutmut_6(self, export_file):
        try:
            with open(export_file, 'w') as file:
                json.dump(self.tasks, indent=4)
        except IOError as e:
            print(f"Error exporting tasks: {e}")

    def xǁTaskManagerǁexport_to_json__mutmut_7(self, export_file):
        try:
            with open(export_file, 'w') as file:
                json.dump(self.tasks, file,)
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

    def xǁTaskManagerǁgenerate_report__mutmut_1(self):
        total_tasks = None
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

    def xǁTaskManagerǁgenerate_report__mutmut_2(self):
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = None
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

    def xǁTaskManagerǁgenerate_report__mutmut_3(self):
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
        pending_tasks = None
        in_progress_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "In Progress"])
        overdue_tasks = len(self.get_overdue_tasks())
        return {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "in_progress_tasks": in_progress_tasks,
            "overdue_tasks": overdue_tasks
        }

    def xǁTaskManagerǁgenerate_report__mutmut_4(self):
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
        pending_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Pending"])
        in_progress_tasks = None
        overdue_tasks = len(self.get_overdue_tasks())
        return {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "in_progress_tasks": in_progress_tasks,
            "overdue_tasks": overdue_tasks
        }

    def xǁTaskManagerǁgenerate_report__mutmut_5(self):
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
        pending_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Pending"])
        in_progress_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "In Progress"])
        overdue_tasks = None
        return {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "in_progress_tasks": in_progress_tasks,
            "overdue_tasks": overdue_tasks
        }

    def xǁTaskManagerǁgenerate_report__mutmut_6(self):
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
        pending_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Pending"])
        in_progress_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "In Progress"])
        overdue_tasks = len(self.get_overdue_tasks())
        return {
            "XXtotal_tasksXX": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "in_progress_tasks": in_progress_tasks,
            "overdue_tasks": overdue_tasks
        }

    def xǁTaskManagerǁgenerate_report__mutmut_7(self):
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
        pending_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Pending"])
        in_progress_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "In Progress"])
        overdue_tasks = len(self.get_overdue_tasks())
        return {
            "total_tasks": total_tasks,
            "XXcompleted_tasksXX": completed_tasks,
            "pending_tasks": pending_tasks,
            "in_progress_tasks": in_progress_tasks,
            "overdue_tasks": overdue_tasks
        }

    def xǁTaskManagerǁgenerate_report__mutmut_8(self):
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
        pending_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Pending"])
        in_progress_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "In Progress"])
        overdue_tasks = len(self.get_overdue_tasks())
        return {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "XXpending_tasksXX": pending_tasks,
            "in_progress_tasks": in_progress_tasks,
            "overdue_tasks": overdue_tasks
        }

    def xǁTaskManagerǁgenerate_report__mutmut_9(self):
        total_tasks = len(self.tasks["tasks"])
        completed_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Completed"])
        pending_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "Pending"])
        in_progress_tasks = len([task for task in self.tasks["tasks"] if task["status"] == "In Progress"])
        overdue_tasks = len(self.get_overdue_tasks())
        return {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "XXin_progress_tasksXX": in_progress_tasks,
            "overdue_tasks": overdue_tasks
        }

    def xǁTaskManagerǁgenerate_report__mutmut_10(self):
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
            "XXoverdue_tasksXX": overdue_tasks
        }

    xǁTaskManagerǁgenerate_report__mutmut_mutants = {
    'xǁTaskManagerǁgenerate_report__mutmut_1': xǁTaskManagerǁgenerate_report__mutmut_1, 
        'xǁTaskManagerǁgenerate_report__mutmut_2': xǁTaskManagerǁgenerate_report__mutmut_2, 
        'xǁTaskManagerǁgenerate_report__mutmut_3': xǁTaskManagerǁgenerate_report__mutmut_3, 
        'xǁTaskManagerǁgenerate_report__mutmut_4': xǁTaskManagerǁgenerate_report__mutmut_4, 
        'xǁTaskManagerǁgenerate_report__mutmut_5': xǁTaskManagerǁgenerate_report__mutmut_5, 
        'xǁTaskManagerǁgenerate_report__mutmut_6': xǁTaskManagerǁgenerate_report__mutmut_6, 
        'xǁTaskManagerǁgenerate_report__mutmut_7': xǁTaskManagerǁgenerate_report__mutmut_7, 
        'xǁTaskManagerǁgenerate_report__mutmut_8': xǁTaskManagerǁgenerate_report__mutmut_8, 
        'xǁTaskManagerǁgenerate_report__mutmut_9': xǁTaskManagerǁgenerate_report__mutmut_9, 
        'xǁTaskManagerǁgenerate_report__mutmut_10': xǁTaskManagerǁgenerate_report__mutmut_10
    }

    def generate_report(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁgenerate_report__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁgenerate_report__mutmut_mutants"), *args, **kwargs)
        return result 

    generate_report.__signature__ = _mutmut_signature(xǁTaskManagerǁgenerate_report__mutmut_orig)
    xǁTaskManagerǁgenerate_report__mutmut_orig.__name__ = 'xǁTaskManagerǁgenerate_report'



    def xǁTaskManagerǁsort_tasks_by_deadline__mutmut_orig(self):
        self.tasks["tasks"].sort(key=lambda task: self._parse_date(task["deadline"]))
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_deadline__mutmut_1(self):
        self.tasks["XXtasksXX"].sort(key=lambda task: self._parse_date(task["deadline"]))
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_deadline__mutmut_2(self):
        self.tasks[None].sort(key=lambda task: self._parse_date(task["deadline"]))
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_deadline__mutmut_3(self):
        self.tasks["tasks"].sort(key=lambda task: self._parse_date(task["XXdeadlineXX"]))
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_deadline__mutmut_4(self):
        self.tasks["tasks"].sort(key=lambda task: self._parse_date(task[None]))
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_deadline__mutmut_5(self):
        self.tasks["tasks"].sort(key=lambda task: None)
        self.save_tasks()

    xǁTaskManagerǁsort_tasks_by_deadline__mutmut_mutants = {
    'xǁTaskManagerǁsort_tasks_by_deadline__mutmut_1': xǁTaskManagerǁsort_tasks_by_deadline__mutmut_1, 
        'xǁTaskManagerǁsort_tasks_by_deadline__mutmut_2': xǁTaskManagerǁsort_tasks_by_deadline__mutmut_2, 
        'xǁTaskManagerǁsort_tasks_by_deadline__mutmut_3': xǁTaskManagerǁsort_tasks_by_deadline__mutmut_3, 
        'xǁTaskManagerǁsort_tasks_by_deadline__mutmut_4': xǁTaskManagerǁsort_tasks_by_deadline__mutmut_4, 
        'xǁTaskManagerǁsort_tasks_by_deadline__mutmut_5': xǁTaskManagerǁsort_tasks_by_deadline__mutmut_5
    }

    def sort_tasks_by_deadline(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁsort_tasks_by_deadline__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁsort_tasks_by_deadline__mutmut_mutants"), *args, **kwargs)
        return result 

    sort_tasks_by_deadline.__signature__ = _mutmut_signature(xǁTaskManagerǁsort_tasks_by_deadline__mutmut_orig)
    xǁTaskManagerǁsort_tasks_by_deadline__mutmut_orig.__name__ = 'xǁTaskManagerǁsort_tasks_by_deadline'



    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_orig(self):
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_1(self):
        priority_order = {"XXHighXX": 1, "Medium": 2, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_2(self):
        priority_order = {"High": 2, "Medium": 2, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_3(self):
        priority_order = {"High": 1, "XXMediumXX": 2, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_4(self):
        priority_order = {"High": 1, "Medium": 3, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_5(self):
        priority_order = {"High": 1, "Medium": 2, "XXLowXX": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_6(self):
        priority_order = {"High": 1, "Medium": 2, "Low": 4}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_7(self):
        priority_order = None
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["priority"]])
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_8(self):
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks["XXtasksXX"].sort(key=lambda task: priority_order[task["priority"]])
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_9(self):
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks[None].sort(key=lambda task: priority_order[task["priority"]])
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_10(self):
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task["XXpriorityXX"]])
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_11(self):
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[task[None]])
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_12(self):
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: priority_order[None])
        self.save_tasks()

    def xǁTaskManagerǁsort_tasks_by_priority__mutmut_13(self):
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks["tasks"].sort(key=lambda task: None)
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
        'xǁTaskManagerǁsort_tasks_by_priority__mutmut_13': xǁTaskManagerǁsort_tasks_by_priority__mutmut_13
    }

    def sort_tasks_by_priority(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁsort_tasks_by_priority__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁsort_tasks_by_priority__mutmut_mutants"), *args, **kwargs)
        return result 

    sort_tasks_by_priority.__signature__ = _mutmut_signature(xǁTaskManagerǁsort_tasks_by_priority__mutmut_orig)
    xǁTaskManagerǁsort_tasks_by_priority__mutmut_orig.__name__ = 'xǁTaskManagerǁsort_tasks_by_priority'



    def xǁTaskManagerǁfind_task_by_id__mutmut_orig(self, task_id):
        for task in self.tasks["tasks"]:
            if task["id"] == task_id:
                return task
        return None

    def xǁTaskManagerǁfind_task_by_id__mutmut_1(self, task_id):
        for task in self.tasks["XXtasksXX"]:
            if task["id"] == task_id:
                return task
        return None

    def xǁTaskManagerǁfind_task_by_id__mutmut_2(self, task_id):
        for task in self.tasks[None]:
            if task["id"] == task_id:
                return task
        return None

    def xǁTaskManagerǁfind_task_by_id__mutmut_3(self, task_id):
        for task in self.tasks["tasks"]:
            if task["XXidXX"] == task_id:
                return task
        return None

    def xǁTaskManagerǁfind_task_by_id__mutmut_4(self, task_id):
        for task in self.tasks["tasks"]:
            if task[None] == task_id:
                return task
        return None

    def xǁTaskManagerǁfind_task_by_id__mutmut_5(self, task_id):
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
        if not self.tasks["tasks"]:
            return 1
        task_ids = [task["id"] for task in self.tasks["tasks"]]
        return max(task_ids) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_1(self):
        if  self.tasks["tasks"]:
            return 1
        task_ids = [task["id"] for task in self.tasks["tasks"]]
        return max(task_ids) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_2(self):
        if not self.tasks["XXtasksXX"]:
            return 1
        task_ids = [task["id"] for task in self.tasks["tasks"]]
        return max(task_ids) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_3(self):
        if not self.tasks[None]:
            return 1
        task_ids = [task["id"] for task in self.tasks["tasks"]]
        return max(task_ids) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_4(self):
        if not self.tasks["tasks"]:
            return 2
        task_ids = [task["id"] for task in self.tasks["tasks"]]
        return max(task_ids) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_5(self):
        if not self.tasks["tasks"]:
            return 1
        task_ids = [task["XXidXX"] for task in self.tasks["tasks"]]
        return max(task_ids) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_6(self):
        if not self.tasks["tasks"]:
            return 1
        task_ids = [task[None] for task in self.tasks["tasks"]]
        return max(task_ids) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_7(self):
        if not self.tasks["tasks"]:
            return 1
        task_ids = [task["id"] for task in self.tasks["XXtasksXX"]]
        return max(task_ids) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_8(self):
        if not self.tasks["tasks"]:
            return 1
        task_ids = [task["id"] for task in self.tasks[None]]
        return max(task_ids) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_9(self):
        if not self.tasks["tasks"]:
            return 1
        task_ids = None
        return max(task_ids) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_10(self):
        if not self.tasks["tasks"]:
            return 1
        task_ids = [task["id"] for task in self.tasks["tasks"]]
        return max(None) + 1

    def xǁTaskManagerǁget_next_task_id__mutmut_11(self):
        if not self.tasks["tasks"]:
            return 1
        task_ids = [task["id"] for task in self.tasks["tasks"]]
        return max(task_ids) - 1

    def xǁTaskManagerǁget_next_task_id__mutmut_12(self):
        if not self.tasks["tasks"]:
            return 1
        task_ids = [task["id"] for task in self.tasks["tasks"]]
        return max(task_ids) + 2

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
        'xǁTaskManagerǁget_next_task_id__mutmut_10': xǁTaskManagerǁget_next_task_id__mutmut_10, 
        'xǁTaskManagerǁget_next_task_id__mutmut_11': xǁTaskManagerǁget_next_task_id__mutmut_11, 
        'xǁTaskManagerǁget_next_task_id__mutmut_12': xǁTaskManagerǁget_next_task_id__mutmut_12
    }

    def get_next_task_id(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁget_next_task_id__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁget_next_task_id__mutmut_mutants"), *args, **kwargs)
        return result 

    get_next_task_id.__signature__ = _mutmut_signature(xǁTaskManagerǁget_next_task_id__mutmut_orig)
    xǁTaskManagerǁget_next_task_id__mutmut_orig.__name__ = 'xǁTaskManagerǁget_next_task_id'



    def xǁTaskManagerǁ_validate_date_format__mutmut_orig(self, date_string):
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            print(f"Invalid date format: {date_string}")
            return False

    def xǁTaskManagerǁ_validate_date_format__mutmut_1(self, date_string):
        try:
            datetime.strptime(None, '%Y-%m-%d')
            return True
        except ValueError:
            print(f"Invalid date format: {date_string}")
            return False

    def xǁTaskManagerǁ_validate_date_format__mutmut_2(self, date_string):
        try:
            datetime.strptime(date_string, 'XX%Y-%m-%dXX')
            return True
        except ValueError:
            print(f"Invalid date format: {date_string}")
            return False

    def xǁTaskManagerǁ_validate_date_format__mutmut_3(self, date_string):
        try:
            datetime.strptime( '%Y-%m-%d')
            return True
        except ValueError:
            print(f"Invalid date format: {date_string}")
            return False

    def xǁTaskManagerǁ_validate_date_format__mutmut_4(self, date_string):
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return False
        except ValueError:
            print(f"Invalid date format: {date_string}")
            return False

    def xǁTaskManagerǁ_validate_date_format__mutmut_5(self, date_string):
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            print(f"Invalid date format: {date_string}")
            return True

    xǁTaskManagerǁ_validate_date_format__mutmut_mutants = {
    'xǁTaskManagerǁ_validate_date_format__mutmut_1': xǁTaskManagerǁ_validate_date_format__mutmut_1, 
        'xǁTaskManagerǁ_validate_date_format__mutmut_2': xǁTaskManagerǁ_validate_date_format__mutmut_2, 
        'xǁTaskManagerǁ_validate_date_format__mutmut_3': xǁTaskManagerǁ_validate_date_format__mutmut_3, 
        'xǁTaskManagerǁ_validate_date_format__mutmut_4': xǁTaskManagerǁ_validate_date_format__mutmut_4, 
        'xǁTaskManagerǁ_validate_date_format__mutmut_5': xǁTaskManagerǁ_validate_date_format__mutmut_5
    }

    def _validate_date_format(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁ_validate_date_format__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁ_validate_date_format__mutmut_mutants"), *args, **kwargs)
        return result 

    _validate_date_format.__signature__ = _mutmut_signature(xǁTaskManagerǁ_validate_date_format__mutmut_orig)
    xǁTaskManagerǁ_validate_date_format__mutmut_orig.__name__ = 'xǁTaskManagerǁ_validate_date_format'



    def xǁTaskManagerǁ_parse_date__mutmut_orig(self, date_string):
        return datetime.strptime(date_string, '%Y-%m-%d')

    def xǁTaskManagerǁ_parse_date__mutmut_1(self, date_string):
        return datetime.strptime(None, '%Y-%m-%d')

    def xǁTaskManagerǁ_parse_date__mutmut_2(self, date_string):
        return datetime.strptime(date_string, 'XX%Y-%m-%dXX')

    def xǁTaskManagerǁ_parse_date__mutmut_3(self, date_string):
        return datetime.strptime( '%Y-%m-%d')

    xǁTaskManagerǁ_parse_date__mutmut_mutants = {
    'xǁTaskManagerǁ_parse_date__mutmut_1': xǁTaskManagerǁ_parse_date__mutmut_1, 
        'xǁTaskManagerǁ_parse_date__mutmut_2': xǁTaskManagerǁ_parse_date__mutmut_2, 
        'xǁTaskManagerǁ_parse_date__mutmut_3': xǁTaskManagerǁ_parse_date__mutmut_3
    }

    def _parse_date(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁ_parse_date__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁ_parse_date__mutmut_mutants"), *args, **kwargs)
        return result 

    _parse_date.__signature__ = _mutmut_signature(xǁTaskManagerǁ_parse_date__mutmut_orig)
    xǁTaskManagerǁ_parse_date__mutmut_orig.__name__ = 'xǁTaskManagerǁ_parse_date'



    def xǁTaskManagerǁarchive_completed_tasks__mutmut_orig(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_1(self, archive_file):
        completed_tasks = [task for task in self.tasks["XXtasksXX"] if task["status"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_2(self, archive_file):
        completed_tasks = [task for task in self.tasks[None] if task["status"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_3(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["XXstatusXX"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_4(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task[None] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_5(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_6(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "XXCompletedXX"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_7(self, archive_file):
        completed_tasks = None
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_8(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks["XXtasksXX"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_9(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks[None] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_10(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["XXtasksXX"] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_11(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks[None] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_12(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["XXstatusXX"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_13(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task[None] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_14(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_15(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "XXCompletedXX"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_16(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks["tasks"] = None
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_17(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open(None, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_18(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'XXwXX') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_19(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open( 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_20(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"XXarchived_tasksXX": completed_tasks}, file, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_21(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, None, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_22(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file, indent=5)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_23(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, indent=4)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    def xǁTaskManagerǁarchive_completed_tasks__mutmut_24(self, archive_file):
        completed_tasks = [task for task in self.tasks["tasks"] if task["status"] == "Completed"]
        self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["status"] != "Completed"]
        try:
            with open(archive_file, 'w') as file:
                json.dump({"archived_tasks": completed_tasks}, file,)
            self.save_tasks()
        except IOError as e:
            print(f"Error archiving tasks: {e}")

    xǁTaskManagerǁarchive_completed_tasks__mutmut_mutants = {
    'xǁTaskManagerǁarchive_completed_tasks__mutmut_1': xǁTaskManagerǁarchive_completed_tasks__mutmut_1, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_2': xǁTaskManagerǁarchive_completed_tasks__mutmut_2, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_3': xǁTaskManagerǁarchive_completed_tasks__mutmut_3, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_4': xǁTaskManagerǁarchive_completed_tasks__mutmut_4, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_5': xǁTaskManagerǁarchive_completed_tasks__mutmut_5, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_6': xǁTaskManagerǁarchive_completed_tasks__mutmut_6, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_7': xǁTaskManagerǁarchive_completed_tasks__mutmut_7, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_8': xǁTaskManagerǁarchive_completed_tasks__mutmut_8, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_9': xǁTaskManagerǁarchive_completed_tasks__mutmut_9, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_10': xǁTaskManagerǁarchive_completed_tasks__mutmut_10, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_11': xǁTaskManagerǁarchive_completed_tasks__mutmut_11, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_12': xǁTaskManagerǁarchive_completed_tasks__mutmut_12, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_13': xǁTaskManagerǁarchive_completed_tasks__mutmut_13, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_14': xǁTaskManagerǁarchive_completed_tasks__mutmut_14, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_15': xǁTaskManagerǁarchive_completed_tasks__mutmut_15, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_16': xǁTaskManagerǁarchive_completed_tasks__mutmut_16, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_17': xǁTaskManagerǁarchive_completed_tasks__mutmut_17, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_18': xǁTaskManagerǁarchive_completed_tasks__mutmut_18, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_19': xǁTaskManagerǁarchive_completed_tasks__mutmut_19, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_20': xǁTaskManagerǁarchive_completed_tasks__mutmut_20, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_21': xǁTaskManagerǁarchive_completed_tasks__mutmut_21, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_22': xǁTaskManagerǁarchive_completed_tasks__mutmut_22, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_23': xǁTaskManagerǁarchive_completed_tasks__mutmut_23, 
        'xǁTaskManagerǁarchive_completed_tasks__mutmut_24': xǁTaskManagerǁarchive_completed_tasks__mutmut_24
    }

    def archive_completed_tasks(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁarchive_completed_tasks__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁarchive_completed_tasks__mutmut_mutants"), *args, **kwargs)
        return result 

    archive_completed_tasks.__signature__ = _mutmut_signature(xǁTaskManagerǁarchive_completed_tasks__mutmut_orig)
    xǁTaskManagerǁarchive_completed_tasks__mutmut_orig.__name__ = 'xǁTaskManagerǁarchive_completed_tasks'



    def xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_orig(self, start_date, end_date):
        if not self._validate_date_format(start_date) or not self._validate_date_format(end_date):
            return []
        start = self._parse_date(start_date)
        end = self._parse_date(end_date)
        return [
            task for task in self.tasks["tasks"]
            if start <= self._parse_date(task["deadline"]) <= end
        ]

    def xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_1(self, start_date, end_date):
        if  self._validate_date_format(start_date) or not self._validate_date_format(end_date):
            return []
        start = self._parse_date(start_date)
        end = self._parse_date(end_date)
        return [
            task for task in self.tasks["tasks"]
            if start <= self._parse_date(task["deadline"]) <= end
        ]

    def xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_2(self, start_date, end_date):
        if not self._validate_date_format(None) or not self._validate_date_format(end_date):
            return []
        start = self._parse_date(start_date)
        end = self._parse_date(end_date)
        return [
            task for task in self.tasks["tasks"]
            if start <= self._parse_date(task["deadline"]) <= end
        ]

    def xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_3(self, start_date, end_date):
        if not self._validate_date_format(start_date) or  self._validate_date_format(end_date):
            return []
        start = self._parse_date(start_date)
        end = self._parse_date(end_date)
        return [
            task for task in self.tasks["tasks"]
            if start <= self._parse_date(task["deadline"]) <= end
        ]

    def xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_4(self, start_date, end_date):
        if not self._validate_date_format(start_date) or not self._validate_date_format(None):
            return []
        start = self._parse_date(start_date)
        end = self._parse_date(end_date)
        return [
            task for task in self.tasks["tasks"]
            if start <= self._parse_date(task["deadline"]) <= end
        ]

    def xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_5(self, start_date, end_date):
        if not self._validate_date_format(start_date) and not self._validate_date_format(end_date):
            return []
        start = self._parse_date(start_date)
        end = self._parse_date(end_date)
        return [
            task for task in self.tasks["tasks"]
            if start <= self._parse_date(task["deadline"]) <= end
        ]

    def xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_6(self, start_date, end_date):
        if not self._validate_date_format(start_date) or not self._validate_date_format(end_date):
            return []
        start = self._parse_date(None)
        end = self._parse_date(end_date)
        return [
            task for task in self.tasks["tasks"]
            if start <= self._parse_date(task["deadline"]) <= end
        ]

    def xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_7(self, start_date, end_date):
        if not self._validate_date_format(start_date) or not self._validate_date_format(end_date):
            return []
        start = None
        end = self._parse_date(end_date)
        return [
            task for task in self.tasks["tasks"]
            if start <= self._parse_date(task["deadline"]) <= end
        ]

    def xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_8(self, start_date, end_date):
        if not self._validate_date_format(start_date) or not self._validate_date_format(end_date):
            return []
        start = self._parse_date(start_date)
        end = self._parse_date(None)
        return [
            task for task in self.tasks["tasks"]
            if start <= self._parse_date(task["deadline"]) <= end
        ]

    def xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_9(self, start_date, end_date):
        if not self._validate_date_format(start_date) or not self._validate_date_format(end_date):
            return []
        start = self._parse_date(start_date)
        end = None
        return [
            task for task in self.tasks["tasks"]
            if start <= self._parse_date(task["deadline"]) <= end
        ]

    def xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_10(self, start_date, end_date):
        if not self._validate_date_format(start_date) or not self._validate_date_format(end_date):
            return []
        start = self._parse_date(start_date)
        end = self._parse_date(end_date)
        return [
            task for task in self.tasks["XXtasksXX"]
            if start <= self._parse_date(task["deadline"]) <= end
        ]

    def xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_11(self, start_date, end_date):
        if not self._validate_date_format(start_date) or not self._validate_date_format(end_date):
            return []
        start = self._parse_date(start_date)
        end = self._parse_date(end_date)
        return [
            task for task in self.tasks[None]
            if start <= self._parse_date(task["deadline"]) <= end
        ]

    def xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_12(self, start_date, end_date):
        if not self._validate_date_format(start_date) or not self._validate_date_format(end_date):
            return []
        start = self._parse_date(start_date)
        end = self._parse_date(end_date)
        return [
            task for task in self.tasks["tasks"]
            if start < self._parse_date(task["deadline"]) <= end
        ]

    def xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_13(self, start_date, end_date):
        if not self._validate_date_format(start_date) or not self._validate_date_format(end_date):
            return []
        start = self._parse_date(start_date)
        end = self._parse_date(end_date)
        return [
            task for task in self.tasks["tasks"]
            if start <= self._parse_date(task["XXdeadlineXX"]) <= end
        ]

    def xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_14(self, start_date, end_date):
        if not self._validate_date_format(start_date) or not self._validate_date_format(end_date):
            return []
        start = self._parse_date(start_date)
        end = self._parse_date(end_date)
        return [
            task for task in self.tasks["tasks"]
            if start <= self._parse_date(task[None]) <= end
        ]

    def xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_15(self, start_date, end_date):
        if not self._validate_date_format(start_date) or not self._validate_date_format(end_date):
            return []
        start = self._parse_date(start_date)
        end = self._parse_date(end_date)
        return [
            task for task in self.tasks["tasks"]
            if start <= self._parse_date(task["deadline"]) < end
        ]

    xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_mutants = {
    'xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_1': xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_1, 
        'xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_2': xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_2, 
        'xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_3': xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_3, 
        'xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_4': xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_4, 
        'xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_5': xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_5, 
        'xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_6': xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_6, 
        'xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_7': xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_7, 
        'xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_8': xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_8, 
        'xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_9': xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_9, 
        'xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_10': xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_10, 
        'xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_11': xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_11, 
        'xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_12': xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_12, 
        'xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_13': xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_13, 
        'xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_14': xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_14, 
        'xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_15': xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_15
    }

    def filter_tasks_by_date_range(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_mutants"), *args, **kwargs)
        return result 

    filter_tasks_by_date_range.__signature__ = _mutmut_signature(xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_orig)
    xǁTaskManagerǁfilter_tasks_by_date_range__mutmut_orig.__name__ = 'xǁTaskManagerǁfilter_tasks_by_date_range'



    def xǁTaskManagerǁcount_tasks_by_category__mutmut_orig(self):
        category_count = {}
        for task in self.tasks["tasks"]:
            category = task["category"]
            category_count[category] = category_count.get(category, 0) + 1
        return category_count

    def xǁTaskManagerǁcount_tasks_by_category__mutmut_1(self):
        category_count = None
        for task in self.tasks["tasks"]:
            category = task["category"]
            category_count[category] = category_count.get(category, 0) + 1
        return category_count

    def xǁTaskManagerǁcount_tasks_by_category__mutmut_2(self):
        category_count = {}
        for task in self.tasks["XXtasksXX"]:
            category = task["category"]
            category_count[category] = category_count.get(category, 0) + 1
        return category_count

    def xǁTaskManagerǁcount_tasks_by_category__mutmut_3(self):
        category_count = {}
        for task in self.tasks[None]:
            category = task["category"]
            category_count[category] = category_count.get(category, 0) + 1
        return category_count

    def xǁTaskManagerǁcount_tasks_by_category__mutmut_4(self):
        category_count = {}
        for task in self.tasks["tasks"]:
            category = task["XXcategoryXX"]
            category_count[category] = category_count.get(category, 0) + 1
        return category_count

    def xǁTaskManagerǁcount_tasks_by_category__mutmut_5(self):
        category_count = {}
        for task in self.tasks["tasks"]:
            category = task[None]
            category_count[category] = category_count.get(category, 0) + 1
        return category_count

    def xǁTaskManagerǁcount_tasks_by_category__mutmut_6(self):
        category_count = {}
        for task in self.tasks["tasks"]:
            category = None
            category_count[category] = category_count.get(category, 0) + 1
        return category_count

    def xǁTaskManagerǁcount_tasks_by_category__mutmut_7(self):
        category_count = {}
        for task in self.tasks["tasks"]:
            category = task["category"]
            category_count[None] = category_count.get(category, 0) + 1
        return category_count

    def xǁTaskManagerǁcount_tasks_by_category__mutmut_8(self):
        category_count = {}
        for task in self.tasks["tasks"]:
            category = task["category"]
            category_count[category] = category_count.get(None, 0) + 1
        return category_count

    def xǁTaskManagerǁcount_tasks_by_category__mutmut_9(self):
        category_count = {}
        for task in self.tasks["tasks"]:
            category = task["category"]
            category_count[category] = category_count.get(category, 1) + 1
        return category_count

    def xǁTaskManagerǁcount_tasks_by_category__mutmut_10(self):
        category_count = {}
        for task in self.tasks["tasks"]:
            category = task["category"]
            category_count[category] = category_count.get( 0) + 1
        return category_count

    def xǁTaskManagerǁcount_tasks_by_category__mutmut_11(self):
        category_count = {}
        for task in self.tasks["tasks"]:
            category = task["category"]
            category_count[category] = category_count.get(category, 0) - 1
        return category_count

    def xǁTaskManagerǁcount_tasks_by_category__mutmut_12(self):
        category_count = {}
        for task in self.tasks["tasks"]:
            category = task["category"]
            category_count[category] = category_count.get(category, 0) + 2
        return category_count

    def xǁTaskManagerǁcount_tasks_by_category__mutmut_13(self):
        category_count = {}
        for task in self.tasks["tasks"]:
            category = task["category"]
            category_count[category] = None
        return category_count

    xǁTaskManagerǁcount_tasks_by_category__mutmut_mutants = {
    'xǁTaskManagerǁcount_tasks_by_category__mutmut_1': xǁTaskManagerǁcount_tasks_by_category__mutmut_1, 
        'xǁTaskManagerǁcount_tasks_by_category__mutmut_2': xǁTaskManagerǁcount_tasks_by_category__mutmut_2, 
        'xǁTaskManagerǁcount_tasks_by_category__mutmut_3': xǁTaskManagerǁcount_tasks_by_category__mutmut_3, 
        'xǁTaskManagerǁcount_tasks_by_category__mutmut_4': xǁTaskManagerǁcount_tasks_by_category__mutmut_4, 
        'xǁTaskManagerǁcount_tasks_by_category__mutmut_5': xǁTaskManagerǁcount_tasks_by_category__mutmut_5, 
        'xǁTaskManagerǁcount_tasks_by_category__mutmut_6': xǁTaskManagerǁcount_tasks_by_category__mutmut_6, 
        'xǁTaskManagerǁcount_tasks_by_category__mutmut_7': xǁTaskManagerǁcount_tasks_by_category__mutmut_7, 
        'xǁTaskManagerǁcount_tasks_by_category__mutmut_8': xǁTaskManagerǁcount_tasks_by_category__mutmut_8, 
        'xǁTaskManagerǁcount_tasks_by_category__mutmut_9': xǁTaskManagerǁcount_tasks_by_category__mutmut_9, 
        'xǁTaskManagerǁcount_tasks_by_category__mutmut_10': xǁTaskManagerǁcount_tasks_by_category__mutmut_10, 
        'xǁTaskManagerǁcount_tasks_by_category__mutmut_11': xǁTaskManagerǁcount_tasks_by_category__mutmut_11, 
        'xǁTaskManagerǁcount_tasks_by_category__mutmut_12': xǁTaskManagerǁcount_tasks_by_category__mutmut_12, 
        'xǁTaskManagerǁcount_tasks_by_category__mutmut_13': xǁTaskManagerǁcount_tasks_by_category__mutmut_13
    }

    def count_tasks_by_category(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁcount_tasks_by_category__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁcount_tasks_by_category__mutmut_mutants"), *args, **kwargs)
        return result 

    count_tasks_by_category.__signature__ = _mutmut_signature(xǁTaskManagerǁcount_tasks_by_category__mutmut_orig)
    xǁTaskManagerǁcount_tasks_by_category__mutmut_orig.__name__ = 'xǁTaskManagerǁcount_tasks_by_category'



    def xǁTaskManagerǁupdate_task_status_bulk__mutmut_orig(self, task_ids, new_status):
        if not self._validate_status(new_status):
            print(f"Bulk update failed: Invalid status '{new_status}'.")
            return
        for task_id in task_ids:
            task = self.find_task_by_id(task_id)
            if task:
                task["status"] = new_status
        self.save_tasks()

    def xǁTaskManagerǁupdate_task_status_bulk__mutmut_1(self, task_ids, new_status):
        if  self._validate_status(new_status):
            print(f"Bulk update failed: Invalid status '{new_status}'.")
            return
        for task_id in task_ids:
            task = self.find_task_by_id(task_id)
            if task:
                task["status"] = new_status
        self.save_tasks()

    def xǁTaskManagerǁupdate_task_status_bulk__mutmut_2(self, task_ids, new_status):
        if not self._validate_status(None):
            print(f"Bulk update failed: Invalid status '{new_status}'.")
            return
        for task_id in task_ids:
            task = self.find_task_by_id(task_id)
            if task:
                task["status"] = new_status
        self.save_tasks()

    def xǁTaskManagerǁupdate_task_status_bulk__mutmut_3(self, task_ids, new_status):
        if not self._validate_status(new_status):
            print(f"Bulk update failed: Invalid status '{new_status}'.")
            return
        for task_id in task_ids:
            task = self.find_task_by_id(None)
            if task:
                task["status"] = new_status
        self.save_tasks()

    def xǁTaskManagerǁupdate_task_status_bulk__mutmut_4(self, task_ids, new_status):
        if not self._validate_status(new_status):
            print(f"Bulk update failed: Invalid status '{new_status}'.")
            return
        for task_id in task_ids:
            task = None
            if task:
                task["status"] = new_status
        self.save_tasks()

    def xǁTaskManagerǁupdate_task_status_bulk__mutmut_5(self, task_ids, new_status):
        if not self._validate_status(new_status):
            print(f"Bulk update failed: Invalid status '{new_status}'.")
            return
        for task_id in task_ids:
            task = self.find_task_by_id(task_id)
            if task:
                task["XXstatusXX"] = new_status
        self.save_tasks()

    def xǁTaskManagerǁupdate_task_status_bulk__mutmut_6(self, task_ids, new_status):
        if not self._validate_status(new_status):
            print(f"Bulk update failed: Invalid status '{new_status}'.")
            return
        for task_id in task_ids:
            task = self.find_task_by_id(task_id)
            if task:
                task[None] = new_status
        self.save_tasks()

    def xǁTaskManagerǁupdate_task_status_bulk__mutmut_7(self, task_ids, new_status):
        if not self._validate_status(new_status):
            print(f"Bulk update failed: Invalid status '{new_status}'.")
            return
        for task_id in task_ids:
            task = self.find_task_by_id(task_id)
            if task:
                task["status"] = None
        self.save_tasks()

    xǁTaskManagerǁupdate_task_status_bulk__mutmut_mutants = {
    'xǁTaskManagerǁupdate_task_status_bulk__mutmut_1': xǁTaskManagerǁupdate_task_status_bulk__mutmut_1, 
        'xǁTaskManagerǁupdate_task_status_bulk__mutmut_2': xǁTaskManagerǁupdate_task_status_bulk__mutmut_2, 
        'xǁTaskManagerǁupdate_task_status_bulk__mutmut_3': xǁTaskManagerǁupdate_task_status_bulk__mutmut_3, 
        'xǁTaskManagerǁupdate_task_status_bulk__mutmut_4': xǁTaskManagerǁupdate_task_status_bulk__mutmut_4, 
        'xǁTaskManagerǁupdate_task_status_bulk__mutmut_5': xǁTaskManagerǁupdate_task_status_bulk__mutmut_5, 
        'xǁTaskManagerǁupdate_task_status_bulk__mutmut_6': xǁTaskManagerǁupdate_task_status_bulk__mutmut_6, 
        'xǁTaskManagerǁupdate_task_status_bulk__mutmut_7': xǁTaskManagerǁupdate_task_status_bulk__mutmut_7
    }

    def update_task_status_bulk(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁupdate_task_status_bulk__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁupdate_task_status_bulk__mutmut_mutants"), *args, **kwargs)
        return result 

    update_task_status_bulk.__signature__ = _mutmut_signature(xǁTaskManagerǁupdate_task_status_bulk__mutmut_orig)
    xǁTaskManagerǁupdate_task_status_bulk__mutmut_orig.__name__ = 'xǁTaskManagerǁupdate_task_status_bulk'



    def xǁTaskManagerǁ_validate_category__mutmut_orig(self, category):
        allowed_categories = ["Work", "Personal", "Health", "Education", "Misc"]
        if category not in allowed_categories:
            print(f"Invalid category: {category}. Allowed categories are: {', '.join(allowed_categories)}")
            return False
        return True

    def xǁTaskManagerǁ_validate_category__mutmut_1(self, category):
        allowed_categories = ["XXWorkXX", "Personal", "Health", "Education", "Misc"]
        if category not in allowed_categories:
            print(f"Invalid category: {category}. Allowed categories are: {', '.join(allowed_categories)}")
            return False
        return True

    def xǁTaskManagerǁ_validate_category__mutmut_2(self, category):
        allowed_categories = ["Work", "XXPersonalXX", "Health", "Education", "Misc"]
        if category not in allowed_categories:
            print(f"Invalid category: {category}. Allowed categories are: {', '.join(allowed_categories)}")
            return False
        return True

    def xǁTaskManagerǁ_validate_category__mutmut_3(self, category):
        allowed_categories = ["Work", "Personal", "XXHealthXX", "Education", "Misc"]
        if category not in allowed_categories:
            print(f"Invalid category: {category}. Allowed categories are: {', '.join(allowed_categories)}")
            return False
        return True

    def xǁTaskManagerǁ_validate_category__mutmut_4(self, category):
        allowed_categories = ["Work", "Personal", "Health", "XXEducationXX", "Misc"]
        if category not in allowed_categories:
            print(f"Invalid category: {category}. Allowed categories are: {', '.join(allowed_categories)}")
            return False
        return True

    def xǁTaskManagerǁ_validate_category__mutmut_5(self, category):
        allowed_categories = ["Work", "Personal", "Health", "Education", "XXMiscXX"]
        if category not in allowed_categories:
            print(f"Invalid category: {category}. Allowed categories are: {', '.join(allowed_categories)}")
            return False
        return True

    def xǁTaskManagerǁ_validate_category__mutmut_6(self, category):
        allowed_categories = None
        if category not in allowed_categories:
            print(f"Invalid category: {category}. Allowed categories are: {', '.join(allowed_categories)}")
            return False
        return True

    def xǁTaskManagerǁ_validate_category__mutmut_7(self, category):
        allowed_categories = ["Work", "Personal", "Health", "Education", "Misc"]
        if category  in allowed_categories:
            print(f"Invalid category: {category}. Allowed categories are: {', '.join(allowed_categories)}")
            return False
        return True

    def xǁTaskManagerǁ_validate_category__mutmut_8(self, category):
        allowed_categories = ["Work", "Personal", "Health", "Education", "Misc"]
        if category not in allowed_categories:
            print(f"Invalid category: {category}. Allowed categories are: {'XX, XX'.join(allowed_categories)}")
            return False
        return True

    def xǁTaskManagerǁ_validate_category__mutmut_9(self, category):
        allowed_categories = ["Work", "Personal", "Health", "Education", "Misc"]
        if category not in allowed_categories:
            print(f"Invalid category: {category}. Allowed categories are: {', '.join(None)}")
            return False
        return True

    def xǁTaskManagerǁ_validate_category__mutmut_10(self, category):
        allowed_categories = ["Work", "Personal", "Health", "Education", "Misc"]
        if category not in allowed_categories:
            print(f"Invalid category: {category}. Allowed categories are: {', '.join(allowed_categories)}")
            return True
        return True

    def xǁTaskManagerǁ_validate_category__mutmut_11(self, category):
        allowed_categories = ["Work", "Personal", "Health", "Education", "Misc"]
        if category not in allowed_categories:
            print(f"Invalid category: {category}. Allowed categories are: {', '.join(allowed_categories)}")
            return False
        return False

    xǁTaskManagerǁ_validate_category__mutmut_mutants = {
    'xǁTaskManagerǁ_validate_category__mutmut_1': xǁTaskManagerǁ_validate_category__mutmut_1, 
        'xǁTaskManagerǁ_validate_category__mutmut_2': xǁTaskManagerǁ_validate_category__mutmut_2, 
        'xǁTaskManagerǁ_validate_category__mutmut_3': xǁTaskManagerǁ_validate_category__mutmut_3, 
        'xǁTaskManagerǁ_validate_category__mutmut_4': xǁTaskManagerǁ_validate_category__mutmut_4, 
        'xǁTaskManagerǁ_validate_category__mutmut_5': xǁTaskManagerǁ_validate_category__mutmut_5, 
        'xǁTaskManagerǁ_validate_category__mutmut_6': xǁTaskManagerǁ_validate_category__mutmut_6, 
        'xǁTaskManagerǁ_validate_category__mutmut_7': xǁTaskManagerǁ_validate_category__mutmut_7, 
        'xǁTaskManagerǁ_validate_category__mutmut_8': xǁTaskManagerǁ_validate_category__mutmut_8, 
        'xǁTaskManagerǁ_validate_category__mutmut_9': xǁTaskManagerǁ_validate_category__mutmut_9, 
        'xǁTaskManagerǁ_validate_category__mutmut_10': xǁTaskManagerǁ_validate_category__mutmut_10, 
        'xǁTaskManagerǁ_validate_category__mutmut_11': xǁTaskManagerǁ_validate_category__mutmut_11
    }

    def _validate_category(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁ_validate_category__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁ_validate_category__mutmut_mutants"), *args, **kwargs)
        return result 

    _validate_category.__signature__ = _mutmut_signature(xǁTaskManagerǁ_validate_category__mutmut_orig)
    xǁTaskManagerǁ_validate_category__mutmut_orig.__name__ = 'xǁTaskManagerǁ_validate_category'


    
    def xǁTaskManagerǁ_validate_status__mutmut_orig(self, status):
        allowed_statuses = ["Pending", "In Progress", "Completed", "Archived"]
        if status not in allowed_statuses:
            print(f"Invalid status: {status}. Allowed statuses are: {', '.join(allowed_statuses)}")
            return False
        return True
    
    def xǁTaskManagerǁ_validate_status__mutmut_1(self, status):
        allowed_statuses = ["XXPendingXX", "In Progress", "Completed", "Archived"]
        if status not in allowed_statuses:
            print(f"Invalid status: {status}. Allowed statuses are: {', '.join(allowed_statuses)}")
            return False
        return True
    
    def xǁTaskManagerǁ_validate_status__mutmut_2(self, status):
        allowed_statuses = ["Pending", "XXIn ProgressXX", "Completed", "Archived"]
        if status not in allowed_statuses:
            print(f"Invalid status: {status}. Allowed statuses are: {', '.join(allowed_statuses)}")
            return False
        return True
    
    def xǁTaskManagerǁ_validate_status__mutmut_3(self, status):
        allowed_statuses = ["Pending", "In Progress", "XXCompletedXX", "Archived"]
        if status not in allowed_statuses:
            print(f"Invalid status: {status}. Allowed statuses are: {', '.join(allowed_statuses)}")
            return False
        return True
    
    def xǁTaskManagerǁ_validate_status__mutmut_4(self, status):
        allowed_statuses = ["Pending", "In Progress", "Completed", "XXArchivedXX"]
        if status not in allowed_statuses:
            print(f"Invalid status: {status}. Allowed statuses are: {', '.join(allowed_statuses)}")
            return False
        return True
    
    def xǁTaskManagerǁ_validate_status__mutmut_5(self, status):
        allowed_statuses = None
        if status not in allowed_statuses:
            print(f"Invalid status: {status}. Allowed statuses are: {', '.join(allowed_statuses)}")
            return False
        return True
    
    def xǁTaskManagerǁ_validate_status__mutmut_6(self, status):
        allowed_statuses = ["Pending", "In Progress", "Completed", "Archived"]
        if status  in allowed_statuses:
            print(f"Invalid status: {status}. Allowed statuses are: {', '.join(allowed_statuses)}")
            return False
        return True
    
    def xǁTaskManagerǁ_validate_status__mutmut_7(self, status):
        allowed_statuses = ["Pending", "In Progress", "Completed", "Archived"]
        if status not in allowed_statuses:
            print(f"Invalid status: {status}. Allowed statuses are: {'XX, XX'.join(allowed_statuses)}")
            return False
        return True
    
    def xǁTaskManagerǁ_validate_status__mutmut_8(self, status):
        allowed_statuses = ["Pending", "In Progress", "Completed", "Archived"]
        if status not in allowed_statuses:
            print(f"Invalid status: {status}. Allowed statuses are: {', '.join(None)}")
            return False
        return True
    
    def xǁTaskManagerǁ_validate_status__mutmut_9(self, status):
        allowed_statuses = ["Pending", "In Progress", "Completed", "Archived"]
        if status not in allowed_statuses:
            print(f"Invalid status: {status}. Allowed statuses are: {', '.join(allowed_statuses)}")
            return True
        return True
    
    def xǁTaskManagerǁ_validate_status__mutmut_10(self, status):
        allowed_statuses = ["Pending", "In Progress", "Completed", "Archived"]
        if status not in allowed_statuses:
            print(f"Invalid status: {status}. Allowed statuses are: {', '.join(allowed_statuses)}")
            return False
        return False

    xǁTaskManagerǁ_validate_status__mutmut_mutants = {
    'xǁTaskManagerǁ_validate_status__mutmut_1': xǁTaskManagerǁ_validate_status__mutmut_1, 
        'xǁTaskManagerǁ_validate_status__mutmut_2': xǁTaskManagerǁ_validate_status__mutmut_2, 
        'xǁTaskManagerǁ_validate_status__mutmut_3': xǁTaskManagerǁ_validate_status__mutmut_3, 
        'xǁTaskManagerǁ_validate_status__mutmut_4': xǁTaskManagerǁ_validate_status__mutmut_4, 
        'xǁTaskManagerǁ_validate_status__mutmut_5': xǁTaskManagerǁ_validate_status__mutmut_5, 
        'xǁTaskManagerǁ_validate_status__mutmut_6': xǁTaskManagerǁ_validate_status__mutmut_6, 
        'xǁTaskManagerǁ_validate_status__mutmut_7': xǁTaskManagerǁ_validate_status__mutmut_7, 
        'xǁTaskManagerǁ_validate_status__mutmut_8': xǁTaskManagerǁ_validate_status__mutmut_8, 
        'xǁTaskManagerǁ_validate_status__mutmut_9': xǁTaskManagerǁ_validate_status__mutmut_9, 
        'xǁTaskManagerǁ_validate_status__mutmut_10': xǁTaskManagerǁ_validate_status__mutmut_10
    }

    def _validate_status(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁ_validate_status__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁ_validate_status__mutmut_mutants"), *args, **kwargs)
        return result 

    _validate_status.__signature__ = _mutmut_signature(xǁTaskManagerǁ_validate_status__mutmut_orig)
    xǁTaskManagerǁ_validate_status__mutmut_orig.__name__ = 'xǁTaskManagerǁ_validate_status'



    def xǁTaskManagerǁget_tasks_by_priority__mutmut_orig(self, priority):
        if not self._is_priority_valid(priority):
            return []
        return [task for task in self.tasks["tasks"] if task["priority"] == priority]

    def xǁTaskManagerǁget_tasks_by_priority__mutmut_1(self, priority):
        if  self._is_priority_valid(priority):
            return []
        return [task for task in self.tasks["tasks"] if task["priority"] == priority]

    def xǁTaskManagerǁget_tasks_by_priority__mutmut_2(self, priority):
        if not self._is_priority_valid(None):
            return []
        return [task for task in self.tasks["tasks"] if task["priority"] == priority]

    def xǁTaskManagerǁget_tasks_by_priority__mutmut_3(self, priority):
        if not self._is_priority_valid(priority):
            return []
        return [task for task in self.tasks["XXtasksXX"] if task["priority"] == priority]

    def xǁTaskManagerǁget_tasks_by_priority__mutmut_4(self, priority):
        if not self._is_priority_valid(priority):
            return []
        return [task for task in self.tasks[None] if task["priority"] == priority]

    def xǁTaskManagerǁget_tasks_by_priority__mutmut_5(self, priority):
        if not self._is_priority_valid(priority):
            return []
        return [task for task in self.tasks["tasks"] if task["XXpriorityXX"] == priority]

    def xǁTaskManagerǁget_tasks_by_priority__mutmut_6(self, priority):
        if not self._is_priority_valid(priority):
            return []
        return [task for task in self.tasks["tasks"] if task[None] == priority]

    def xǁTaskManagerǁget_tasks_by_priority__mutmut_7(self, priority):
        if not self._is_priority_valid(priority):
            return []
        return [task for task in self.tasks["tasks"] if task["priority"] != priority]

    xǁTaskManagerǁget_tasks_by_priority__mutmut_mutants = {
    'xǁTaskManagerǁget_tasks_by_priority__mutmut_1': xǁTaskManagerǁget_tasks_by_priority__mutmut_1, 
        'xǁTaskManagerǁget_tasks_by_priority__mutmut_2': xǁTaskManagerǁget_tasks_by_priority__mutmut_2, 
        'xǁTaskManagerǁget_tasks_by_priority__mutmut_3': xǁTaskManagerǁget_tasks_by_priority__mutmut_3, 
        'xǁTaskManagerǁget_tasks_by_priority__mutmut_4': xǁTaskManagerǁget_tasks_by_priority__mutmut_4, 
        'xǁTaskManagerǁget_tasks_by_priority__mutmut_5': xǁTaskManagerǁget_tasks_by_priority__mutmut_5, 
        'xǁTaskManagerǁget_tasks_by_priority__mutmut_6': xǁTaskManagerǁget_tasks_by_priority__mutmut_6, 
        'xǁTaskManagerǁget_tasks_by_priority__mutmut_7': xǁTaskManagerǁget_tasks_by_priority__mutmut_7
    }

    def get_tasks_by_priority(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁget_tasks_by_priority__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁget_tasks_by_priority__mutmut_mutants"), *args, **kwargs)
        return result 

    get_tasks_by_priority.__signature__ = _mutmut_signature(xǁTaskManagerǁget_tasks_by_priority__mutmut_orig)
    xǁTaskManagerǁget_tasks_by_priority__mutmut_orig.__name__ = 'xǁTaskManagerǁget_tasks_by_priority'


    
    def xǁTaskManagerǁcount_tasks_by_status__mutmut_orig(self):
        status_count = {}
        for task in self.tasks["tasks"]:
            status = task["status"]
            status_count[status] = status_count.get(status, 0) + 1
        return status_count
    
    def xǁTaskManagerǁcount_tasks_by_status__mutmut_1(self):
        status_count = None
        for task in self.tasks["tasks"]:
            status = task["status"]
            status_count[status] = status_count.get(status, 0) + 1
        return status_count
    
    def xǁTaskManagerǁcount_tasks_by_status__mutmut_2(self):
        status_count = {}
        for task in self.tasks["XXtasksXX"]:
            status = task["status"]
            status_count[status] = status_count.get(status, 0) + 1
        return status_count
    
    def xǁTaskManagerǁcount_tasks_by_status__mutmut_3(self):
        status_count = {}
        for task in self.tasks[None]:
            status = task["status"]
            status_count[status] = status_count.get(status, 0) + 1
        return status_count
    
    def xǁTaskManagerǁcount_tasks_by_status__mutmut_4(self):
        status_count = {}
        for task in self.tasks["tasks"]:
            status = task["XXstatusXX"]
            status_count[status] = status_count.get(status, 0) + 1
        return status_count
    
    def xǁTaskManagerǁcount_tasks_by_status__mutmut_5(self):
        status_count = {}
        for task in self.tasks["tasks"]:
            status = task[None]
            status_count[status] = status_count.get(status, 0) + 1
        return status_count
    
    def xǁTaskManagerǁcount_tasks_by_status__mutmut_6(self):
        status_count = {}
        for task in self.tasks["tasks"]:
            status = None
            status_count[status] = status_count.get(status, 0) + 1
        return status_count
    
    def xǁTaskManagerǁcount_tasks_by_status__mutmut_7(self):
        status_count = {}
        for task in self.tasks["tasks"]:
            status = task["status"]
            status_count[None] = status_count.get(status, 0) + 1
        return status_count
    
    def xǁTaskManagerǁcount_tasks_by_status__mutmut_8(self):
        status_count = {}
        for task in self.tasks["tasks"]:
            status = task["status"]
            status_count[status] = status_count.get(None, 0) + 1
        return status_count
    
    def xǁTaskManagerǁcount_tasks_by_status__mutmut_9(self):
        status_count = {}
        for task in self.tasks["tasks"]:
            status = task["status"]
            status_count[status] = status_count.get(status, 1) + 1
        return status_count
    
    def xǁTaskManagerǁcount_tasks_by_status__mutmut_10(self):
        status_count = {}
        for task in self.tasks["tasks"]:
            status = task["status"]
            status_count[status] = status_count.get( 0) + 1
        return status_count
    
    def xǁTaskManagerǁcount_tasks_by_status__mutmut_11(self):
        status_count = {}
        for task in self.tasks["tasks"]:
            status = task["status"]
            status_count[status] = status_count.get(status, 0) - 1
        return status_count
    
    def xǁTaskManagerǁcount_tasks_by_status__mutmut_12(self):
        status_count = {}
        for task in self.tasks["tasks"]:
            status = task["status"]
            status_count[status] = status_count.get(status, 0) + 2
        return status_count
    
    def xǁTaskManagerǁcount_tasks_by_status__mutmut_13(self):
        status_count = {}
        for task in self.tasks["tasks"]:
            status = task["status"]
            status_count[status] = None
        return status_count

    xǁTaskManagerǁcount_tasks_by_status__mutmut_mutants = {
    'xǁTaskManagerǁcount_tasks_by_status__mutmut_1': xǁTaskManagerǁcount_tasks_by_status__mutmut_1, 
        'xǁTaskManagerǁcount_tasks_by_status__mutmut_2': xǁTaskManagerǁcount_tasks_by_status__mutmut_2, 
        'xǁTaskManagerǁcount_tasks_by_status__mutmut_3': xǁTaskManagerǁcount_tasks_by_status__mutmut_3, 
        'xǁTaskManagerǁcount_tasks_by_status__mutmut_4': xǁTaskManagerǁcount_tasks_by_status__mutmut_4, 
        'xǁTaskManagerǁcount_tasks_by_status__mutmut_5': xǁTaskManagerǁcount_tasks_by_status__mutmut_5, 
        'xǁTaskManagerǁcount_tasks_by_status__mutmut_6': xǁTaskManagerǁcount_tasks_by_status__mutmut_6, 
        'xǁTaskManagerǁcount_tasks_by_status__mutmut_7': xǁTaskManagerǁcount_tasks_by_status__mutmut_7, 
        'xǁTaskManagerǁcount_tasks_by_status__mutmut_8': xǁTaskManagerǁcount_tasks_by_status__mutmut_8, 
        'xǁTaskManagerǁcount_tasks_by_status__mutmut_9': xǁTaskManagerǁcount_tasks_by_status__mutmut_9, 
        'xǁTaskManagerǁcount_tasks_by_status__mutmut_10': xǁTaskManagerǁcount_tasks_by_status__mutmut_10, 
        'xǁTaskManagerǁcount_tasks_by_status__mutmut_11': xǁTaskManagerǁcount_tasks_by_status__mutmut_11, 
        'xǁTaskManagerǁcount_tasks_by_status__mutmut_12': xǁTaskManagerǁcount_tasks_by_status__mutmut_12, 
        'xǁTaskManagerǁcount_tasks_by_status__mutmut_13': xǁTaskManagerǁcount_tasks_by_status__mutmut_13
    }

    def count_tasks_by_status(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁcount_tasks_by_status__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁcount_tasks_by_status__mutmut_mutants"), *args, **kwargs)
        return result 

    count_tasks_by_status.__signature__ = _mutmut_signature(xǁTaskManagerǁcount_tasks_by_status__mutmut_orig)
    xǁTaskManagerǁcount_tasks_by_status__mutmut_orig.__name__ = 'xǁTaskManagerǁcount_tasks_by_status'



    def xǁTaskManagerǁmark_task_as_completed__mutmut_orig(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
        task["status"] = "Completed"
        self.save_tasks()
        print(f"Task with ID {task_id} marked as Completed.")

    def xǁTaskManagerǁmark_task_as_completed__mutmut_1(self, task_id):
        task = self.find_task_by_id(None)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
        task["status"] = "Completed"
        self.save_tasks()
        print(f"Task with ID {task_id} marked as Completed.")

    def xǁTaskManagerǁmark_task_as_completed__mutmut_2(self, task_id):
        task = None
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
        task["status"] = "Completed"
        self.save_tasks()
        print(f"Task with ID {task_id} marked as Completed.")

    def xǁTaskManagerǁmark_task_as_completed__mutmut_3(self, task_id):
        task = self.find_task_by_id(task_id)
        if  task:
            print(f"Task with ID {task_id} not found.")
            return
        task["status"] = "Completed"
        self.save_tasks()
        print(f"Task with ID {task_id} marked as Completed.")

    def xǁTaskManagerǁmark_task_as_completed__mutmut_4(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
        task["XXstatusXX"] = "Completed"
        self.save_tasks()
        print(f"Task with ID {task_id} marked as Completed.")

    def xǁTaskManagerǁmark_task_as_completed__mutmut_5(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
        task[None] = "Completed"
        self.save_tasks()
        print(f"Task with ID {task_id} marked as Completed.")

    def xǁTaskManagerǁmark_task_as_completed__mutmut_6(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
        task["status"] = "XXCompletedXX"
        self.save_tasks()
        print(f"Task with ID {task_id} marked as Completed.")

    def xǁTaskManagerǁmark_task_as_completed__mutmut_7(self, task_id):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
        task["status"] = None
        self.save_tasks()
        print(f"Task with ID {task_id} marked as Completed.")

    xǁTaskManagerǁmark_task_as_completed__mutmut_mutants = {
    'xǁTaskManagerǁmark_task_as_completed__mutmut_1': xǁTaskManagerǁmark_task_as_completed__mutmut_1, 
        'xǁTaskManagerǁmark_task_as_completed__mutmut_2': xǁTaskManagerǁmark_task_as_completed__mutmut_2, 
        'xǁTaskManagerǁmark_task_as_completed__mutmut_3': xǁTaskManagerǁmark_task_as_completed__mutmut_3, 
        'xǁTaskManagerǁmark_task_as_completed__mutmut_4': xǁTaskManagerǁmark_task_as_completed__mutmut_4, 
        'xǁTaskManagerǁmark_task_as_completed__mutmut_5': xǁTaskManagerǁmark_task_as_completed__mutmut_5, 
        'xǁTaskManagerǁmark_task_as_completed__mutmut_6': xǁTaskManagerǁmark_task_as_completed__mutmut_6, 
        'xǁTaskManagerǁmark_task_as_completed__mutmut_7': xǁTaskManagerǁmark_task_as_completed__mutmut_7
    }

    def mark_task_as_completed(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁmark_task_as_completed__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁmark_task_as_completed__mutmut_mutants"), *args, **kwargs)
        return result 

    mark_task_as_completed.__signature__ = _mutmut_signature(xǁTaskManagerǁmark_task_as_completed__mutmut_orig)
    xǁTaskManagerǁmark_task_as_completed__mutmut_orig.__name__ = 'xǁTaskManagerǁmark_task_as_completed'




    def xǁTaskManagerǁget_overdue_tasks__mutmut_orig(self):
        now = datetime.now()
        return [
            task for task in self.tasks["tasks"]
            if task["status"] != "Completed" and self._parse_date(task["deadline"]) < now
        ]


    def xǁTaskManagerǁget_overdue_tasks__mutmut_1(self):
        now = None
        return [
            task for task in self.tasks["tasks"]
            if task["status"] != "Completed" and self._parse_date(task["deadline"]) < now
        ]


    def xǁTaskManagerǁget_overdue_tasks__mutmut_2(self):
        now = datetime.now()
        return [
            task for task in self.tasks["XXtasksXX"]
            if task["status"] != "Completed" and self._parse_date(task["deadline"]) < now
        ]


    def xǁTaskManagerǁget_overdue_tasks__mutmut_3(self):
        now = datetime.now()
        return [
            task for task in self.tasks[None]
            if task["status"] != "Completed" and self._parse_date(task["deadline"]) < now
        ]


    def xǁTaskManagerǁget_overdue_tasks__mutmut_4(self):
        now = datetime.now()
        return [
            task for task in self.tasks["tasks"]
            if task["XXstatusXX"] != "Completed" and self._parse_date(task["deadline"]) < now
        ]


    def xǁTaskManagerǁget_overdue_tasks__mutmut_5(self):
        now = datetime.now()
        return [
            task for task in self.tasks["tasks"]
            if task[None] != "Completed" and self._parse_date(task["deadline"]) < now
        ]


    def xǁTaskManagerǁget_overdue_tasks__mutmut_6(self):
        now = datetime.now()
        return [
            task for task in self.tasks["tasks"]
            if task["status"] == "Completed" and self._parse_date(task["deadline"]) < now
        ]


    def xǁTaskManagerǁget_overdue_tasks__mutmut_7(self):
        now = datetime.now()
        return [
            task for task in self.tasks["tasks"]
            if task["status"] != "XXCompletedXX" and self._parse_date(task["deadline"]) < now
        ]


    def xǁTaskManagerǁget_overdue_tasks__mutmut_8(self):
        now = datetime.now()
        return [
            task for task in self.tasks["tasks"]
            if task["status"] != "Completed" and self._parse_date(task["XXdeadlineXX"]) < now
        ]


    def xǁTaskManagerǁget_overdue_tasks__mutmut_9(self):
        now = datetime.now()
        return [
            task for task in self.tasks["tasks"]
            if task["status"] != "Completed" and self._parse_date(task[None]) < now
        ]


    def xǁTaskManagerǁget_overdue_tasks__mutmut_10(self):
        now = datetime.now()
        return [
            task for task in self.tasks["tasks"]
            if task["status"] != "Completed" and self._parse_date(task["deadline"]) <= now
        ]


    def xǁTaskManagerǁget_overdue_tasks__mutmut_11(self):
        now = datetime.now()
        return [
            task for task in self.tasks["tasks"]
            if task["status"] != "Completed" or self._parse_date(task["deadline"]) < now
        ]

    xǁTaskManagerǁget_overdue_tasks__mutmut_mutants = {
    'xǁTaskManagerǁget_overdue_tasks__mutmut_1': xǁTaskManagerǁget_overdue_tasks__mutmut_1, 
        'xǁTaskManagerǁget_overdue_tasks__mutmut_2': xǁTaskManagerǁget_overdue_tasks__mutmut_2, 
        'xǁTaskManagerǁget_overdue_tasks__mutmut_3': xǁTaskManagerǁget_overdue_tasks__mutmut_3, 
        'xǁTaskManagerǁget_overdue_tasks__mutmut_4': xǁTaskManagerǁget_overdue_tasks__mutmut_4, 
        'xǁTaskManagerǁget_overdue_tasks__mutmut_5': xǁTaskManagerǁget_overdue_tasks__mutmut_5, 
        'xǁTaskManagerǁget_overdue_tasks__mutmut_6': xǁTaskManagerǁget_overdue_tasks__mutmut_6, 
        'xǁTaskManagerǁget_overdue_tasks__mutmut_7': xǁTaskManagerǁget_overdue_tasks__mutmut_7, 
        'xǁTaskManagerǁget_overdue_tasks__mutmut_8': xǁTaskManagerǁget_overdue_tasks__mutmut_8, 
        'xǁTaskManagerǁget_overdue_tasks__mutmut_9': xǁTaskManagerǁget_overdue_tasks__mutmut_9, 
        'xǁTaskManagerǁget_overdue_tasks__mutmut_10': xǁTaskManagerǁget_overdue_tasks__mutmut_10, 
        'xǁTaskManagerǁget_overdue_tasks__mutmut_11': xǁTaskManagerǁget_overdue_tasks__mutmut_11
    }

    def get_overdue_tasks(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁget_overdue_tasks__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁget_overdue_tasks__mutmut_mutants"), *args, **kwargs)
        return result 

    get_overdue_tasks.__signature__ = _mutmut_signature(xǁTaskManagerǁget_overdue_tasks__mutmut_orig)
    xǁTaskManagerǁget_overdue_tasks__mutmut_orig.__name__ = 'xǁTaskManagerǁget_overdue_tasks'



    def xǁTaskManagerǁextend_task_deadline__mutmut_orig(self, task_id, days=0, hours=0):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task["deadline"])
        new_deadline = current_deadline + timedelta(days=days, hours=hours)
        task["deadline"] = new_deadline.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def xǁTaskManagerǁextend_task_deadline__mutmut_1(self, task_id, days=1, hours=0):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task["deadline"])
        new_deadline = current_deadline + timedelta(days=days, hours=hours)
        task["deadline"] = new_deadline.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def xǁTaskManagerǁextend_task_deadline__mutmut_2(self, task_id, days=0, hours=1):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task["deadline"])
        new_deadline = current_deadline + timedelta(days=days, hours=hours)
        task["deadline"] = new_deadline.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def xǁTaskManagerǁextend_task_deadline__mutmut_3(self, task_id, days=0, hours=0):
        task = self.find_task_by_id(None)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task["deadline"])
        new_deadline = current_deadline + timedelta(days=days, hours=hours)
        task["deadline"] = new_deadline.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def xǁTaskManagerǁextend_task_deadline__mutmut_4(self, task_id, days=0, hours=0):
        task = None
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task["deadline"])
        new_deadline = current_deadline + timedelta(days=days, hours=hours)
        task["deadline"] = new_deadline.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def xǁTaskManagerǁextend_task_deadline__mutmut_5(self, task_id, days=0, hours=0):
        task = self.find_task_by_id(task_id)
        if  task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task["deadline"])
        new_deadline = current_deadline + timedelta(days=days, hours=hours)
        task["deadline"] = new_deadline.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def xǁTaskManagerǁextend_task_deadline__mutmut_6(self, task_id, days=0, hours=0):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task["XXdeadlineXX"])
        new_deadline = current_deadline + timedelta(days=days, hours=hours)
        task["deadline"] = new_deadline.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def xǁTaskManagerǁextend_task_deadline__mutmut_7(self, task_id, days=0, hours=0):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task[None])
        new_deadline = current_deadline + timedelta(days=days, hours=hours)
        task["deadline"] = new_deadline.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def xǁTaskManagerǁextend_task_deadline__mutmut_8(self, task_id, days=0, hours=0):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = None
        new_deadline = current_deadline + timedelta(days=days, hours=hours)
        task["deadline"] = new_deadline.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def xǁTaskManagerǁextend_task_deadline__mutmut_9(self, task_id, days=0, hours=0):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task["deadline"])
        new_deadline = current_deadline - timedelta(days=days, hours=hours)
        task["deadline"] = new_deadline.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def xǁTaskManagerǁextend_task_deadline__mutmut_10(self, task_id, days=0, hours=0):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task["deadline"])
        new_deadline = current_deadline + timedelta(days=None, hours=hours)
        task["deadline"] = new_deadline.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def xǁTaskManagerǁextend_task_deadline__mutmut_11(self, task_id, days=0, hours=0):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task["deadline"])
        new_deadline = current_deadline + timedelta(days=days, hours=None)
        task["deadline"] = new_deadline.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def xǁTaskManagerǁextend_task_deadline__mutmut_12(self, task_id, days=0, hours=0):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task["deadline"])
        new_deadline = current_deadline + timedelta( hours=hours)
        task["deadline"] = new_deadline.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def xǁTaskManagerǁextend_task_deadline__mutmut_13(self, task_id, days=0, hours=0):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task["deadline"])
        new_deadline = current_deadline + timedelta(days=days,)
        task["deadline"] = new_deadline.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def xǁTaskManagerǁextend_task_deadline__mutmut_14(self, task_id, days=0, hours=0):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task["deadline"])
        new_deadline = None
        task["deadline"] = new_deadline.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def xǁTaskManagerǁextend_task_deadline__mutmut_15(self, task_id, days=0, hours=0):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task["deadline"])
        new_deadline = current_deadline + timedelta(days=days, hours=hours)
        task["XXdeadlineXX"] = new_deadline.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def xǁTaskManagerǁextend_task_deadline__mutmut_16(self, task_id, days=0, hours=0):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task["deadline"])
        new_deadline = current_deadline + timedelta(days=days, hours=hours)
        task[None] = new_deadline.strftime('%Y-%m-%d %H:%M:%S')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def xǁTaskManagerǁextend_task_deadline__mutmut_17(self, task_id, days=0, hours=0):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task["deadline"])
        new_deadline = current_deadline + timedelta(days=days, hours=hours)
        task["deadline"] = new_deadline.strftime('XX%Y-%m-%d %H:%M:%SXX')
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    def xǁTaskManagerǁextend_task_deadline__mutmut_18(self, task_id, days=0, hours=0):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_deadline = self._parse_date(task["deadline"])
        new_deadline = current_deadline + timedelta(days=days, hours=hours)
        task["deadline"] = None
        self.save_tasks()
        print(f"Deadline for Task ID {task_id} extended by {days} days and {hours} hours.")

    xǁTaskManagerǁextend_task_deadline__mutmut_mutants = {
    'xǁTaskManagerǁextend_task_deadline__mutmut_1': xǁTaskManagerǁextend_task_deadline__mutmut_1, 
        'xǁTaskManagerǁextend_task_deadline__mutmut_2': xǁTaskManagerǁextend_task_deadline__mutmut_2, 
        'xǁTaskManagerǁextend_task_deadline__mutmut_3': xǁTaskManagerǁextend_task_deadline__mutmut_3, 
        'xǁTaskManagerǁextend_task_deadline__mutmut_4': xǁTaskManagerǁextend_task_deadline__mutmut_4, 
        'xǁTaskManagerǁextend_task_deadline__mutmut_5': xǁTaskManagerǁextend_task_deadline__mutmut_5, 
        'xǁTaskManagerǁextend_task_deadline__mutmut_6': xǁTaskManagerǁextend_task_deadline__mutmut_6, 
        'xǁTaskManagerǁextend_task_deadline__mutmut_7': xǁTaskManagerǁextend_task_deadline__mutmut_7, 
        'xǁTaskManagerǁextend_task_deadline__mutmut_8': xǁTaskManagerǁextend_task_deadline__mutmut_8, 
        'xǁTaskManagerǁextend_task_deadline__mutmut_9': xǁTaskManagerǁextend_task_deadline__mutmut_9, 
        'xǁTaskManagerǁextend_task_deadline__mutmut_10': xǁTaskManagerǁextend_task_deadline__mutmut_10, 
        'xǁTaskManagerǁextend_task_deadline__mutmut_11': xǁTaskManagerǁextend_task_deadline__mutmut_11, 
        'xǁTaskManagerǁextend_task_deadline__mutmut_12': xǁTaskManagerǁextend_task_deadline__mutmut_12, 
        'xǁTaskManagerǁextend_task_deadline__mutmut_13': xǁTaskManagerǁextend_task_deadline__mutmut_13, 
        'xǁTaskManagerǁextend_task_deadline__mutmut_14': xǁTaskManagerǁextend_task_deadline__mutmut_14, 
        'xǁTaskManagerǁextend_task_deadline__mutmut_15': xǁTaskManagerǁextend_task_deadline__mutmut_15, 
        'xǁTaskManagerǁextend_task_deadline__mutmut_16': xǁTaskManagerǁextend_task_deadline__mutmut_16, 
        'xǁTaskManagerǁextend_task_deadline__mutmut_17': xǁTaskManagerǁextend_task_deadline__mutmut_17, 
        'xǁTaskManagerǁextend_task_deadline__mutmut_18': xǁTaskManagerǁextend_task_deadline__mutmut_18
    }

    def extend_task_deadline(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁextend_task_deadline__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁextend_task_deadline__mutmut_mutants"), *args, **kwargs)
        return result 

    extend_task_deadline.__signature__ = _mutmut_signature(xǁTaskManagerǁextend_task_deadline__mutmut_orig)
    xǁTaskManagerǁextend_task_deadline__mutmut_orig.__name__ = 'xǁTaskManagerǁextend_task_deadline'



    def xǁTaskManagerǁgenerate_priority_report__mutmut_orig(self):
        priority_count = {"High": 0, "Medium": 0, "Low": 0}
        for task in self.tasks["tasks"]:
            if task["priority"] in priority_count:
                priority_count[task["priority"]] += 1
        return priority_count

    def xǁTaskManagerǁgenerate_priority_report__mutmut_1(self):
        priority_count = {"XXHighXX": 0, "Medium": 0, "Low": 0}
        for task in self.tasks["tasks"]:
            if task["priority"] in priority_count:
                priority_count[task["priority"]] += 1
        return priority_count

    def xǁTaskManagerǁgenerate_priority_report__mutmut_2(self):
        priority_count = {"High": 1, "Medium": 0, "Low": 0}
        for task in self.tasks["tasks"]:
            if task["priority"] in priority_count:
                priority_count[task["priority"]] += 1
        return priority_count

    def xǁTaskManagerǁgenerate_priority_report__mutmut_3(self):
        priority_count = {"High": 0, "XXMediumXX": 0, "Low": 0}
        for task in self.tasks["tasks"]:
            if task["priority"] in priority_count:
                priority_count[task["priority"]] += 1
        return priority_count

    def xǁTaskManagerǁgenerate_priority_report__mutmut_4(self):
        priority_count = {"High": 0, "Medium": 1, "Low": 0}
        for task in self.tasks["tasks"]:
            if task["priority"] in priority_count:
                priority_count[task["priority"]] += 1
        return priority_count

    def xǁTaskManagerǁgenerate_priority_report__mutmut_5(self):
        priority_count = {"High": 0, "Medium": 0, "XXLowXX": 0}
        for task in self.tasks["tasks"]:
            if task["priority"] in priority_count:
                priority_count[task["priority"]] += 1
        return priority_count

    def xǁTaskManagerǁgenerate_priority_report__mutmut_6(self):
        priority_count = {"High": 0, "Medium": 0, "Low": 1}
        for task in self.tasks["tasks"]:
            if task["priority"] in priority_count:
                priority_count[task["priority"]] += 1
        return priority_count

    def xǁTaskManagerǁgenerate_priority_report__mutmut_7(self):
        priority_count = None
        for task in self.tasks["tasks"]:
            if task["priority"] in priority_count:
                priority_count[task["priority"]] += 1
        return priority_count

    def xǁTaskManagerǁgenerate_priority_report__mutmut_8(self):
        priority_count = {"High": 0, "Medium": 0, "Low": 0}
        for task in self.tasks["XXtasksXX"]:
            if task["priority"] in priority_count:
                priority_count[task["priority"]] += 1
        return priority_count

    def xǁTaskManagerǁgenerate_priority_report__mutmut_9(self):
        priority_count = {"High": 0, "Medium": 0, "Low": 0}
        for task in self.tasks[None]:
            if task["priority"] in priority_count:
                priority_count[task["priority"]] += 1
        return priority_count

    def xǁTaskManagerǁgenerate_priority_report__mutmut_10(self):
        priority_count = {"High": 0, "Medium": 0, "Low": 0}
        for task in self.tasks["tasks"]:
            if task["XXpriorityXX"] in priority_count:
                priority_count[task["priority"]] += 1
        return priority_count

    def xǁTaskManagerǁgenerate_priority_report__mutmut_11(self):
        priority_count = {"High": 0, "Medium": 0, "Low": 0}
        for task in self.tasks["tasks"]:
            if task[None] in priority_count:
                priority_count[task["priority"]] += 1
        return priority_count

    def xǁTaskManagerǁgenerate_priority_report__mutmut_12(self):
        priority_count = {"High": 0, "Medium": 0, "Low": 0}
        for task in self.tasks["tasks"]:
            if task["priority"] not in priority_count:
                priority_count[task["priority"]] += 1
        return priority_count

    def xǁTaskManagerǁgenerate_priority_report__mutmut_13(self):
        priority_count = {"High": 0, "Medium": 0, "Low": 0}
        for task in self.tasks["tasks"]:
            if task["priority"] in priority_count:
                priority_count[task["XXpriorityXX"]] += 1
        return priority_count

    def xǁTaskManagerǁgenerate_priority_report__mutmut_14(self):
        priority_count = {"High": 0, "Medium": 0, "Low": 0}
        for task in self.tasks["tasks"]:
            if task["priority"] in priority_count:
                priority_count[task[None]] += 1
        return priority_count

    def xǁTaskManagerǁgenerate_priority_report__mutmut_15(self):
        priority_count = {"High": 0, "Medium": 0, "Low": 0}
        for task in self.tasks["tasks"]:
            if task["priority"] in priority_count:
                priority_count[None] += 1
        return priority_count

    def xǁTaskManagerǁgenerate_priority_report__mutmut_16(self):
        priority_count = {"High": 0, "Medium": 0, "Low": 0}
        for task in self.tasks["tasks"]:
            if task["priority"] in priority_count:
                priority_count[task["priority"]] -= 1
        return priority_count

    def xǁTaskManagerǁgenerate_priority_report__mutmut_17(self):
        priority_count = {"High": 0, "Medium": 0, "Low": 0}
        for task in self.tasks["tasks"]:
            if task["priority"] in priority_count:
                priority_count[task["priority"]] = 1
        return priority_count

    def xǁTaskManagerǁgenerate_priority_report__mutmut_18(self):
        priority_count = {"High": 0, "Medium": 0, "Low": 0}
        for task in self.tasks["tasks"]:
            if task["priority"] in priority_count:
                priority_count[task["priority"]] += 2
        return priority_count

    xǁTaskManagerǁgenerate_priority_report__mutmut_mutants = {
    'xǁTaskManagerǁgenerate_priority_report__mutmut_1': xǁTaskManagerǁgenerate_priority_report__mutmut_1, 
        'xǁTaskManagerǁgenerate_priority_report__mutmut_2': xǁTaskManagerǁgenerate_priority_report__mutmut_2, 
        'xǁTaskManagerǁgenerate_priority_report__mutmut_3': xǁTaskManagerǁgenerate_priority_report__mutmut_3, 
        'xǁTaskManagerǁgenerate_priority_report__mutmut_4': xǁTaskManagerǁgenerate_priority_report__mutmut_4, 
        'xǁTaskManagerǁgenerate_priority_report__mutmut_5': xǁTaskManagerǁgenerate_priority_report__mutmut_5, 
        'xǁTaskManagerǁgenerate_priority_report__mutmut_6': xǁTaskManagerǁgenerate_priority_report__mutmut_6, 
        'xǁTaskManagerǁgenerate_priority_report__mutmut_7': xǁTaskManagerǁgenerate_priority_report__mutmut_7, 
        'xǁTaskManagerǁgenerate_priority_report__mutmut_8': xǁTaskManagerǁgenerate_priority_report__mutmut_8, 
        'xǁTaskManagerǁgenerate_priority_report__mutmut_9': xǁTaskManagerǁgenerate_priority_report__mutmut_9, 
        'xǁTaskManagerǁgenerate_priority_report__mutmut_10': xǁTaskManagerǁgenerate_priority_report__mutmut_10, 
        'xǁTaskManagerǁgenerate_priority_report__mutmut_11': xǁTaskManagerǁgenerate_priority_report__mutmut_11, 
        'xǁTaskManagerǁgenerate_priority_report__mutmut_12': xǁTaskManagerǁgenerate_priority_report__mutmut_12, 
        'xǁTaskManagerǁgenerate_priority_report__mutmut_13': xǁTaskManagerǁgenerate_priority_report__mutmut_13, 
        'xǁTaskManagerǁgenerate_priority_report__mutmut_14': xǁTaskManagerǁgenerate_priority_report__mutmut_14, 
        'xǁTaskManagerǁgenerate_priority_report__mutmut_15': xǁTaskManagerǁgenerate_priority_report__mutmut_15, 
        'xǁTaskManagerǁgenerate_priority_report__mutmut_16': xǁTaskManagerǁgenerate_priority_report__mutmut_16, 
        'xǁTaskManagerǁgenerate_priority_report__mutmut_17': xǁTaskManagerǁgenerate_priority_report__mutmut_17, 
        'xǁTaskManagerǁgenerate_priority_report__mutmut_18': xǁTaskManagerǁgenerate_priority_report__mutmut_18
    }

    def generate_priority_report(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskManagerǁgenerate_priority_report__mutmut_orig"), object.__getattribute__(self, "xǁTaskManagerǁgenerate_priority_report__mutmut_mutants"), *args, **kwargs)
        return result 

    generate_priority_report.__signature__ = _mutmut_signature(xǁTaskManagerǁgenerate_priority_report__mutmut_orig)
    xǁTaskManagerǁgenerate_priority_report__mutmut_orig.__name__ = 'xǁTaskManagerǁgenerate_priority_report'


