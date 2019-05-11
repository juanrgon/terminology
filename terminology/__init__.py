"""Module for styling terminal text."""
from .ansi import (
    in_black,
    in_blue,
    in_bold,
    in_cyan,
    in_green,
    in_magenta,
    in_red,
    in_white,
    in_yellow,
    on_black,
    on_blue,
    on_cyan,
    on_green,
    on_magenta,
    on_red,
    on_white,
    on_yellow,
    underlined,
    visual_len,
)
from .asap_print import asap_print
from .clear_line import clear_line
from .overwrite_line import overwrite_line
from .terminal_width import terminal_width

__all__ = [
    "asap_print",
    "clear_line",
    "in_black",
    "in_blue",
    "in_bold",
    "in_cyan",
    "in_green",
    "in_magenta",
    "in_red",
    "in_white",
    "in_yellow",
    "on_black",
    "on_blue",
    "on_cyan",
    "on_green",
    "on_magenta",
    "on_red",
    "on_white",
    "on_yellow",
    "overwrite_line",
    "terminal_width",
    "underlined",
    "visual_len",
]

__version__ = "0.1.0"
