import re
from contextlib import contextmanager


NO_COLOR = False


@contextmanager
def disable():
    global NO_COLOR
    original = NO_COLOR
    NO_COLOR = True
    try:
        yield
    finally:
        NO_COLOR = original


def in_black(text: str) -> "StyledStr":
    return _change_text_color(text, AnsiCode.BLACK_TEXT)


def in_blue(text: str) -> "StyledStr":
    return _change_text_color(text, AnsiCode.BLUE_TEXT)


def in_bold(text: str) -> "StyledStr":
    non_bold = _remove_bold(text)
    return _apply_ansi_code(AnsiCode.BOLD, non_bold)


def in_cyan(text: str) -> "StyledStr":
    return _change_text_color(text, AnsiCode.CYAN_TEXT)


def in_green(text: str) -> "StyledStr":
    return _change_text_color(text, AnsiCode.GREEN_TEXT)


def in_magenta(text: str) -> "StyledStr":
    return _change_text_color(text, AnsiCode.MAGENTA_TEXT)


def in_red(text: str) -> "StyledStr":
    return _change_text_color(text, AnsiCode.RED_TEXT)


def in_white(text: str) -> "StyledStr":
    return _change_text_color(text, AnsiCode.WHITE_TEXT)


def in_yellow(text: str) -> "StyledStr":
    return _change_text_color(text, AnsiCode.YELLOW_TEXT)


def on_black(text: str) -> "StyledStr":
    return _change_background_color(text, AnsiCode.BLACK_BACKGROUND)


def on_blue(text: str) -> "StyledStr":
    return _change_background_color(text, AnsiCode.BLUE_BACKGROUND)


def on_cyan(text: str) -> "StyledStr":
    return _change_background_color(text, AnsiCode.CYAN_BACKGROUND)


def on_green(text: str) -> "StyledStr":
    return _change_background_color(text, AnsiCode.GREEN_BACKGROUND)


def on_magenta(text: str) -> "StyledStr":
    return _change_background_color(text, AnsiCode.MAGENTA_BACKGROUND)


def on_red(text: str) -> "StyledStr":
    return _change_background_color(text, AnsiCode.RED_BACKGROUND)


def on_white(text: str) -> "StyledStr":
    return _change_background_color(text, AnsiCode.WHITE_BACKGROUND)


def on_yellow(text: str) -> "StyledStr":
    return _change_background_color(text, AnsiCode.YELLOW_BACKGROUND)


def underlined(text) -> "StyledStr":
    non_underlined = _remove_underline(text)
    return _apply_ansi_code(AnsiCode.UNDERLINE, non_underlined)


def visual_len(text) -> int:
    """The apparent visual length of this string in a terminal."""
    return len(text) if NO_COLOR else len(_remove_regex("\033\\[[0-9]*m", text))


class StyledStr(str):
    def in_black(self) -> "StyledStr":
        return in_black(self)

    def in_blue(self) -> "StyledStr":
        return in_blue(self)

    def in_bold(self) -> "StyledStr":
        return in_bold(self)

    def in_cyan(self) -> "StyledStr":
        return in_cyan(self)

    def in_green(self) -> "StyledStr":
        return in_green(self)

    def in_magenta(self) -> "StyledStr":
        return in_magenta(self)

    def in_red(self) -> "StyledStr":
        return in_red(self)

    def in_white(self) -> "StyledStr":
        return in_white(self)

    def in_yellow(self) -> "StyledStr":
        return in_yellow(self)

    def on_black(self) -> "StyledStr":
        return on_black(self)

    def on_blue(self) -> "StyledStr":
        return on_blue(self)

    def on_cyan(self) -> "StyledStr":
        return on_cyan(self)

    def on_green(self) -> "StyledStr":
        return on_green(self)

    def on_magenta(self) -> "StyledStr":
        return on_magenta(self)

    def on_red(self) -> "StyledStr":
        return on_red(self)

    def on_white(self) -> "StyledStr":
        return on_white(self)

    def on_yellow(self) -> "StyledStr":
        return on_yellow(self)

    def underlined(self) -> "StyledStr":
        return underlined(self)

    def visual_len(self) -> int:
        """The apparent visual length of this string in a terminal."""
        return visual_len(self)


def _apply_ansi_code(ansi_code, text) -> StyledStr:
    if NO_COLOR:
        return StyledStr(text)

    start = ESCAPE_BEGIN + ansi_code + ESCAPE_END
    end = STYLE_RESET
    text = _remove_regex("\033\\[0m$", text)
    text = (STYLE_RESET + start).join(text.split(STYLE_RESET))
    return StyledStr(start + text + end)


def _change_text_color(text, color_code) -> StyledStr:
    """Change the color of text to the given color code."""
    uncolored_fg = _remove_text_colors(text)
    return _apply_ansi_code(color_code, uncolored_fg)


def _change_background_color(text, color_code) -> StyledStr:
    """Change the background color of text to the given color code."""
    uncolored_bg = _remove_background_colors(text)
    return _apply_ansi_code(color_code, uncolored_bg)


def _remove_background_colors(text) -> StyledStr:
    """Remove all background coloring from the given text."""
    return _remove_regex(BACKGROUND_COLORS_REGEX, text)


def _remove_bold(text) -> StyledStr:
    """Remove all text modifications from the given text."""
    return _remove_regex(BOLD_REGEX, text)


def _remove_text_colors(text) -> StyledStr:
    """Remove all foreground coloring from the given text."""
    return _remove_regex(FOREGROUND_COLORS_REGEX, text)


def _remove_regex(regex, text) -> StyledStr:
    """Remove the given regex from the text."""
    text = str(text)
    if NO_COLOR:
        return StyledStr(text)
    return StyledStr(re.sub(regex, "", text))


def _remove_underline(text) -> StyledStr:
    """Remove underlining from the given text."""
    return _remove_regex(UNDERLINED_REGEX, text)


ESCAPE_BEGIN = "\033["
ESCAPE_END = "m"
STYLE_RESET = "\033[0m"
FOREGROUND_COLORS_REGEX = "\033\\[3[0-9]m"
BACKGROUND_COLORS_REGEX = "\033\\[4[0-9]m"
BOLD_REGEX = "\033\\[1m"
UNDERLINED_REGEX = "\033\\[4m"
INVERTED_REGEX = "\033\\[7m"


class AnsiCode:
    BLACK_BACKGROUND = "40"
    BLACK_TEXT = "30"
    BLUE_BACKGROUND = "44"
    BLUE_TEXT = "34"
    CYAN_BACKGROUND = "46"
    CYAN_TEXT = "36"
    BOLD = "1"
    GREEN_BACKGROUND = "42"
    GREEN_TEXT = "32"
    MAGENTA_BACKGROUND = "45"
    MAGENTA_TEXT = "35"
    RED_BACKGROUND = "41"
    RED_TEXT = "31"
    WHITE_BACKGROUND = "47"
    WHITE_TEXT = "37"
    YELLOW_BACKGROUND = "43"
    YELLOW_TEXT = "33"
    NORMAL = "0"
    UNDERLINE = "4"
