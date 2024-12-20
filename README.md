

# Python Testing with Hypothesis, Coverage, and MutMut

This project demonstrates the use of Python testing tools such as `unittest`, `hypothesis`, `coverage`, and `mutmut` for creating robust and reliable applications. Follow the steps below to set up and execute tests.

---

## Prerequisites

- Python 3.x installed on your machine.
- Familiarity with Python testing frameworks.

---

## Setup

### Create a Virtual Environment

clone the repo 

```
git clone https://github.com/venkataramanagovindu/CS567_the_project.git
```

and move the cloned directory

A virtual environment helps isolate dependencies.

```
python3 -m venv venv
```
Activate the Virtual Environment
Activate the environment to start working.

On Linux/Mac:

```
source venv/bin/activate
```

On Windows:

```
venv\Scripts\activate
```

Install required dependencies:


In the root directory check the total code line count using

```
cloc task_manager/task_manager.py
```

```
pip install -r requirements.txt
```
Running Tests
Running Unit Tests
Discover and run all tests in the project using unittest.


```
python3 -m unittest discover
```
Measuring Test Coverage
Run tests with coverage to measure code coverage.


```
coverage run -m unittest discover
```
Generate an HTML report:


```
coverage html
```
Open htmlcov/index.html in a browser to view the coverage report.

Mutation Testing with MutMut
MutMut tests the quality of your unit tests by introducing small code changes (mutations) and checking if the tests catch them.

Running MutMut
Start the mutation testing process:


```
mutmut run
```
Viewing Results
View a summary of the results:


```
mutmut results
```
Check detailed results for a specific file:


```
mutmut show <result_file_name>
```
View all mutation results:


```
mutmut results --all true
```
Project Structure

```
project/
├── venv/               # Virtual environment
├── src/                # Source code
├── tests/              # Test files
├── htmlcov/            # Coverage report
├── README.md           # Documentation
└── requirements.txt    # Dependencies


```
 python3 -m venv venv
 source venv/bin/activate
 pip install hypothesis
 python3 -m unittest discover
 coverage run -m unittest discover  
 coverage html            
 mutmut run
 mutmut results
 mutmut show <result_file_name>
 mutmut results --all true 
```
