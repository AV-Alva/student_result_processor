# Fault-Tolerant Student Result Processor

## Project Overview

The **Fault-Tolerant Student Result Processor** is a Python application that processes student details and marks for five subjects.

The application calculates:

* Total marks
* Percentage
* Grade
* Pass/Fail status

The main objective of this project is to demonstrate the practical use of:

* Python functions
* Modules
* Packages
* Imports
* Exception handling
* Custom exceptions
* Logging
* Input validation
* Fault-tolerant programming

The application is designed so that an error while processing one student does **not stop the entire program**. The error is logged, and the program continues processing the remaining students.

---

## Problem Statement

Create a Python program that reads student details and marks for 5 subjects and calculates total, percentage, grade, and pass/fail status.

The program must handle:

* Incorrect marks
* Non-numeric marks
* Marks outside the range 0–100
* Missing student information
* Division/calculation errors
* Unexpected runtime errors

At least one custom exception must be implemented.

Example:

```python
class InvalidMarksError(Exception):
    pass
```

Errors should be recorded in a log file instead of causing the complete application to terminate.

---

## Project Structure

```text
student_result_processor/
│
├── main.py
├── README.md
├── student_processor.log
│
└── student_processor/
    ├── __init__.py
    ├── student_operations.py
    ├── result_calculator.py
    ├── exceptions.py
    └── logger_config.py
```

---

## Module Description

### `main.py`

This is the entry point of the application.

It:

* Accepts the number of students
* Processes students one by one
* Calls functions from the `student_processor` package
* Handles exceptions
* Displays student results
* Logs successful and failed operations
* Continues with the next student when an error occurs

---

### `student_operations.py`

This module handles student-related input operations.

It is responsible for:

* Reading student name
* Reading roll number
* Checking for missing student information
* Accepting marks for five subjects
* Converting marks into numeric values
* Validating that marks are between 0 and 100

Example validation:

```python
if mark < 0 or mark > 100:
    raise InvalidMarksError(
        "Marks must be between 0 and 100."
    )
```

---

### `result_calculator.py`

This module contains the result calculation logic.

It provides functions to:

* Calculate total marks
* Calculate percentage
* Determine grade
* Determine pass/fail status
* Return the complete student result

Keeping calculation logic in a separate module makes the program easier to understand, test, maintain, and reuse.

---

### `exceptions.py`

This module defines application-specific custom exceptions.

Example:

```python
class InvalidMarksError(Exception):
    """Raised when marks are outside the valid range."""
    pass


class MissingStudentInfoError(Exception):
    """Raised when required student information is missing."""
    pass
```

Custom exceptions make errors easier to identify and handle.

For example, entering `150` as marks is not simply a Python `ValueError`. It is specifically an invalid mark according to the rules of this application.

---

### `logger_config.py`

This module contains the logging configuration.

The application records successful operations and errors inside:

```text
student_processor.log
```

Example log entries:

```text
2026-09-15 19:20:10 - INFO - Successfully processed student: Rahul
2026-09-15 19:21:03 - ERROR - Student 2: Marks must be between 0 and 100
2026-09-15 19:22:15 - ERROR - Student 3: Marks must be numeric
```

Logging helps us understand what happened during program execution even after the application has finished running.

---

### `__init__.py`

The `__init__.py` file tells Python that `student_processor` should be treated as a package.

It also exposes important functions and exceptions so they can be imported directly from the package.

Example:

```python
from .student_operations import get_student_details, get_marks
from .result_calculator import calculate_result
from .exceptions import InvalidMarksError, MissingStudentInfoError
from .logger_config import setup_logger
```

This allows `main.py` to use clean package imports:

```python
from student_processor import (
    get_student_details,
    get_marks,
    calculate_result,
    InvalidMarksError,
    MissingStudentInfoError,
    setup_logger
)
```

---

## Grade Calculation

The following grading system is used:

| Percentage | Grade |
| ---------- | ----- |
| 90–100     | A+    |
| 80–89      | A     |
| 70–79      | B     |
| 60–69      | C     |
| 50–59      | D     |
| Below 50   | F     |

---

## Pass/Fail Rule

A student must score at least **35 marks in every subject** to pass.

For example:

```text
Marks: 85, 75, 90, 65, 70
Status: PASS
```

But:

```text
Marks: 85, 75, 90, 65, 20
Status: FAIL
```

Even if the overall percentage is high enough, scoring below the passing mark in any individual subject results in a `FAIL` status.

---

## Exception Handling

The project demonstrates multiple types of exception handling.

### Non-Numeric Marks

If the user enters:

```text
Enter marks: abc
```

Python cannot convert `abc` into a number.

The resulting error is handled and converted into an `InvalidMarksError`.

---

### Marks Outside 0–100

Examples of invalid marks:

```text
-10
120
150
```

These values raise:

```text
InvalidMarksError
```

---

### Missing Student Information

If the student name or roll number is empty, the program raises:

```text
MissingStudentInfoError
```

---

### Division Errors

The percentage calculation contains protection against division by zero.

```python
if number_of_subjects == 0:
    raise ZeroDivisionError(
        "Cannot calculate percentage with zero subjects."
    )
```

---

### Unexpected Errors

Unexpected errors are handled using:

```python
except Exception as error:
```

This acts as a final safety mechanism so that an unexpected problem with one student does not terminate processing for all remaining students.

---

## Fault-Tolerant Design

The most important feature of this application is its fault-tolerant behavior.

Suppose five students need to be processed:

```text
Student 1 → Valid data
Student 2 → Valid data
Student 3 → Invalid marks
Student 4 → Valid data
Student 5 → Valid data
```

Instead of terminating at Student 3, the application behaves like this:

```text
Student 1 → Processed successfully
Student 2 → Processed successfully
Student 3 → Error detected and logged
Student 4 → Processed successfully
Student 5 → Processed successfully
```

The `try-except` block is placed inside the student-processing loop so that an error affects only the current student.

---

## Example Output

```text
===== STUDENT RESULT PROCESSOR =====

Enter number of students to process: 2

--- Processing Student 1 ---

Enter student name: Rahul
Enter roll number: 101

Enter marks for Subject 1: 85
Enter marks for Subject 2: 90
Enter marks for Subject 3: 75
Enter marks for Subject 4: 80
Enter marks for Subject 5: 70

----- STUDENT RESULT -----

Name: Rahul
Roll Number: 101
Marks: [85.0, 90.0, 75.0, 80.0, 70.0]
Total: 400.0
Percentage: 80.0 %
Grade: A
Status: PASS

Finished processing Student 1
```

Example with invalid input:

```text
--- Processing Student 2 ---

Enter student name: Priya
Enter roll number: 102

Enter marks for Subject 1: 80
Enter marks for Subject 2: 120

Invalid marks: Subject 2: 120.0 is outside the range 0-100.

Finished processing Student 2

===== PROCESSING COMPLETED =====
```

---

## How to Run the Project

### Step 1: Open the project in VS Code

Open the root folder:

```text
student_result_processor
```

### Step 2: Open the terminal

Make sure the terminal is pointing to the project root.

Example:

```text
D:\Projects\student_result_processor>
```

### Step 3: Run the application

Execute:

```bash
python main.py
```

Do not run `main.py` from inside the `student_processor` package directory.

---

## Concepts Demonstrated

### Function

A function is a reusable block of code designed to perform a particular operation.

Example:

```python
def calculate_total(marks):
    return sum(marks)
```

### Module

A module is a Python file containing related functions, classes, or variables.

Examples:

```text
student_operations.py
result_calculator.py
exceptions.py
logger_config.py
```

### Package

A package is a directory containing multiple related Python modules.

In this project:

```text
student_processor/
```

is the Python package.

### Import

Imports allow functionality from one module or package to be reused elsewhere.

Example:

```python
from student_processor import calculate_result
```

### Exception

An exception represents an error or unexpected situation during program execution.

Examples:

```text
ValueError
ZeroDivisionError
```

### Custom Exception

A custom exception represents an application-specific error.

Example:

```python
class InvalidMarksError(Exception):
    pass
```

### Logging

Logging records important application events into a file for debugging, monitoring, and troubleshooting.

---

## Key Learning

This project demonstrates that exception handling is not only about preventing a Python program from crashing.

A well-designed application should:

1. Detect invalid data
2. Raise meaningful exceptions
3. Handle expected errors
4. Record errors using logging
5. Protect the rest of the application
6. Continue processing whenever possible

This creates a more reliable and fault-tolerant application.

---

## Technologies Used

* Python 3
* Python Packages and Modules
* Exception Handling
* Custom Exceptions
* Python `logging` module
* VS Code


Keep Learning. Keep Building. Keep Evolving.
