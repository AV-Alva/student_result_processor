class InvalidMarksError(Exception):
    """Raised when marks are outside the valid range of 0 to 100."""
    pass


class MissingStudentInfoError(Exception):
    """Raised when required student information is missing."""
    pass
