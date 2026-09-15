from student_processor import (
    get_student_details,
    get_marks,
    calculate_result,
    InvalidMarksError,
    MissingStudentInfoError,
    setup_logger
)


logger = setup_logger()


def display_result(name, roll_number, marks, total, percentage, grade, status):
    """Display the student's result."""

    print("\n----- STUDENT RESULT -----")
    print("Name:", name)
    print("Roll Number:", roll_number)
    print("Marks:", marks)
    print("Total:", total)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
    print("Status:", status)


def main():
    """Run the fault-tolerant student result processor."""

    print("===== STUDENT RESULT PROCESSOR =====")

    try:
        number_of_students = int(
            input("Enter number of students to process: ")
        )

        if number_of_students <= 0:
            print("Number of students must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number of students.")
        return

    for student_number in range(1, number_of_students + 1):

        print(
            f"\n--- Processing Student {student_number} ---"
        )

        try:
            name, roll_number = get_student_details()

            marks = get_marks()

            total, percentage, grade, status = calculate_result(
                marks
            )

            display_result(
                name,
                roll_number,
                marks,
                total,
                percentage,
                grade,
                status
            )

            logger.info(
                f"Successfully processed student: "
                f"{name} ({roll_number})"
            )

        except MissingStudentInfoError as error:

            print("Student information error:", error)

            logger.error(
                f"Student {student_number}: {error}"
            )

        except InvalidMarksError as error:

            print("Invalid marks:", error)

            logger.error(
                f"Student {student_number}: {error}"
            )

        except ZeroDivisionError as error:

            print("Calculation error:", error)

            logger.error(
                f"Student {student_number}: {error}"
            )

        except Exception as error:

            print("Unexpected error:", error)

            logger.exception(
                f"Unexpected error while processing "
                f"student {student_number}"
            )

        finally:
            print(
                f"Finished processing Student {student_number}"
            )

    print("\n===== PROCESSING COMPLETED =====")


if __name__ == "__main__":
    main()