from .exceptions import InvalidMarksError, MissingStudentInfoError


def get_student_details():
    """Read and validate student name and roll number."""

    name = input("Enter student name: ").strip()
    roll_number = input("Enter roll number: ").strip()

    if not name or not roll_number:
        raise MissingStudentInfoError(
            "Student name and roll number cannot be empty."
        )

    return name, roll_number


def get_marks():
    """Read and validate marks for five subjects."""

    marks = []

    for subject in range(1, 6):

        try:
            mark = float(
                input(f"Enter marks for Subject {subject}: ")
            )

        except ValueError:
            raise InvalidMarksError(
                f"Subject {subject}: Marks must be numeric."
            )

        if mark < 0 or mark > 100:
            raise InvalidMarksError(
                f"Subject {subject}: {mark} is outside the range 0-100."
            )

        marks.append(mark)

    return marks