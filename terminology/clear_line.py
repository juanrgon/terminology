from .asap_print import asap_print

CLEAR_LINE_SEQUENCE = "\r\033[K"


def clear_line():
    """Clear the line that the cursor is on."""
    asap_print(CLEAR_LINE_SEQUENCE, end="")
