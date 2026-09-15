def calculate_total(marks):
    """Calculate and return the total marks."""

    return sum(marks)


def calculate_percentage(total, number_of_subjects):
    """Calculate percentage."""

    if number_of_subjects == 0:
        raise ZeroDivisionError(
            "Cannot calculate percentage with zero subjects."
        )

    return total / number_of_subjects


def determine_grade(percentage):
    """Determine grade based on percentage."""

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "F"


def determine_status(marks):
    """Determine whether the student passed or failed."""

    passing_mark = 35

    for mark in marks:
        if mark < passing_mark:
            return "FAIL"

    return "PASS"


def calculate_result(marks):
    """Calculate the complete student result."""

    total = calculate_total(marks)

    percentage = calculate_percentage(
        total,
        len(marks)
    )

    grade = determine_grade(percentage)
    status = determine_status(marks)

    return total, percentage, grade, status
