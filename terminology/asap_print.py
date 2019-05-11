def asap_print(*args, **kwargs):
    """
    Print to terminal immediately.

    Equivalent to calling print with `flush=True`.
    """
    kwargs["flush"] = True
    print(*args, **kwargs)
