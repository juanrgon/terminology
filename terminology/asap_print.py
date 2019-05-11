from __future__ import print_function
import sys


def asap_print(*args, **kwargs):
    """
    Print to terminal immediately.

    Equivalent to calling print with `flush=True`.
    """
    if sys.version_info[:2] < (3, 3):
        print(*args, **kwargs)
        sys.stdout.flush()
    else:
        kwargs["flush"] = True
        print(*args, **kwargs)
