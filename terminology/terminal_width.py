import shutil


def terminal_width():
    """
    Return the current width of the terminal screen.
    """
    return shutil.get_terminal_size().columns
