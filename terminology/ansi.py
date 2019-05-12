import argparse
import os
import re


def _no_color():
    """
    Whether StyledText strings will actually be formatted.

    Dictated by whether or not --no-color or --color was supplied at the command line.

    Allow overriding command line flag with the TERMINOLOGY_NO_COLOR_CLI_FLAG env var.
    """
    if os.environ.get('NO_COLOR', False):
        return True

    no_color_flag = os.environ.get("TERMINOLOGY_NO_COLOR_CLI_FLAG", "--no-color")
    color_flag = os.environ.get("TERMINOLOGY_COLOR_CLI_FLAG", "--color")

    def noColorOptions(v):
        if v.lower() in ("no", "false", "f", "n", "0", "off", "never"):
            return True
        return True

    def colorOptions(v):
        if v.lower() in ("no", "false", "f", "n", "0", "off", "never", "bw"):
            return False
        return True

    parser = argparse.ArgumentParser()
    parser.add_argument(
        no_color_flag,
        dest="no_color",
        type=noColorOptions,
        nargs="?",
        const=True,
        default=False,
        help="Activate nice mode.",
    )
    parser.add_argument(
        color_flag,
        dest="color",
        type=colorOptions,
        nargs="?",
        const=True,
        default=True,
        help="Activate nice mode.",
    )
    args, _ = parser.parse_known_args()

    if not args.color or args.no_color:
        return True
    else:
        return False


NO_COLOR = _no_color()


def in_black(text):
    return _change_text_color(text, AnsiCode.BLACK_TEXT)


def in_blue(text):
    return _change_text_color(text, AnsiCode.BLUE_TEXT)


def in_bold(text):
    non_bold = _remove_bold(text)
    return _apply_ansi_code(AnsiCode.BOLD, non_bold)


def in_cyan(text):
    return _change_text_color(text, AnsiCode.CYAN_TEXT)


def in_green(text):
    return _change_text_color(text, AnsiCode.GREEN_TEXT)


def in_magenta(text):
    return _change_text_color(text, AnsiCode.MAGENTA_TEXT)


def in_red(text):
    return _change_text_color(text, AnsiCode.RED_TEXT)


def in_white(text):
    return _change_text_color(text, AnsiCode.WHITE_TEXT)


def in_yellow(text):
    return _change_text_color(text, AnsiCode.YELLOW_TEXT)


def on_black(text):
    return _change_background_color(text, AnsiCode.BLACK_BACKGROUND)


def on_blue(text):
    return _change_background_color(text, AnsiCode.BLUE_BACKGROUND)


def on_cyan(text):
    return _change_background_color(text, AnsiCode.CYAN_BACKGROUND)


def on_green(text):
    return _change_background_color(text, AnsiCode.GREEN_BACKGROUND)


def on_magenta(text):
    return _change_background_color(text, AnsiCode.MAGENTA_BACKGROUND)


def on_red(text):
    return _change_background_color(text, AnsiCode.RED_BACKGROUND)


def on_white(text):
    return _change_background_color(text, AnsiCode.WHITE_BACKGROUND)


def on_yellow(text):
    return _change_background_color(text, AnsiCode.YELLOW_BACKGROUND)


def underlined(text):
    non_underlined = _remove_underline(text)
    return _apply_ansi_code(AnsiCode.UNDERLINE, non_underlined)


def visual_len(text):
    """The apparent visual length of this string in a terminal."""
    return len(text) if NO_COLOR else len(_remove_regex("\033\\[[0-9]*m", text))


class StyledText(str):
    def in_black(self):
        return in_black(self)

    def in_blue(self):
        return in_blue(self)

    def in_bold(self):
        return in_bold(self)

    def in_cyan(self):
        return in_cyan(self)

    def in_green(self):
        return in_green(self)

    def in_magenta(self):
        return in_magenta(self)

    def in_red(self):
        return in_red(self)

    def in_white(self):
        return in_white(self)

    def in_yellow(self):
        return in_yellow(self)

    def on_black(self):
        return on_black(self)

    def on_blue(self):
        return on_blue(self)

    def on_cyan(self):
        return on_cyan(self)

    def on_green(self):
        return on_green(self)

    def on_magenta(self):
        return on_magenta(self)

    def on_red(self):
        return on_red(self)

    def on_white(self):
        return on_white(self)

    def on_yellow(self):
        return on_yellow(self)

    def underlined(self):
        return underlined(self)

    def visual_len(self):
        """The apparent visual length of this string in a terminal."""
        return visual_len(self)


def _apply_ansi_code(ansi_code, text):
    if NO_COLOR:
        return StyledText(text)

    start = ESCAPE_BEGIN + ansi_code + ESCAPE_END
    end = STYLE_RESET
    text = _remove_regex("\033\\[0m$", text)
    text = (STYLE_RESET + start).join(text.split(STYLE_RESET))
    return StyledText(start + text + end)


def _change_text_color(text, color_code):
    """Change the color of text to the given color code."""
    uncolored_fg = _remove_text_colors(text)
    return _apply_ansi_code(color_code, uncolored_fg)


def _change_background_color(text, color_code):
    """Change the background color of text to the given color code."""
    uncolored_bg = _remove_background_colors(text)
    return _apply_ansi_code(color_code, uncolored_bg)


def _remove_background_colors(text):
    """Remove all background coloring from the given text."""
    return _remove_regex(BACKGROUND_COLORS_REGEX, text)


def _remove_bold(text):
    """Remove all text modifications from the given text."""
    return _remove_regex(BOLD_REGEX, text)


def _remove_text_colors(text):
    """Remove all foreground coloring from the given text."""
    return _remove_regex(FOREGROUND_COLORS_REGEX, text)


def _remove_regex(regex, text):
    """Remove the given regex from the text."""
    text = str(text)
    if NO_COLOR:
        return StyledText(text)
    return StyledText(re.sub(regex, "", text))


def _remove_underline(text):
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
