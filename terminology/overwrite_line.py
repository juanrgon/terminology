from .asap_print import asap_print
from .clear_line import clear_line


def overwrite_line(text: str = ""):
    """
    Overwrite the current line in terminal with text.

    Meant to be used to create a dynamic status line.

    Usage:
       import time

       for seconds in range(10, 0, -1):
           overwrite_line(f"Liftoff in {seconds}")
           time.sleep(1)
    """
    clear_line()
    asap_print(text, end="")
