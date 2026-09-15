import logging


def setup_logger():
    """Create and configure the application logger."""

    logging.basicConfig(
        filename="student_processor.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger(__name__)
