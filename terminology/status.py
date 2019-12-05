from .asap_print import asap_print
from .clear_line import clear_line


def status(text=""):
    """
    Provide a status line.

    Usage:
       import time

       for seconds in range(10, 0, -1):
           status(f"Liftoff in {seconds}")
           time.sleep(1)
    """
    clear_line()
    asap_print(text, end="")
