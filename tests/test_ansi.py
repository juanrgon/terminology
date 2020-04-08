from mock import patch

import pytest

from terminology import (
    disable,
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


def test_disable():
    with disable():
        assert underlined("Hello World") == "Hello World"
    assert underlined("Hello World") != "Hello World"


def test_in_black():
    assert in_black("Hello World") == "\x1b[30mHello World\x1b[0m"
    assert in_black("Hello World").in_black() == "\x1b[30mHello World\x1b[0m"


def test_in_blue():
    assert in_blue("Hello World") == "\x1b[34mHello World\x1b[0m"
    assert in_blue("Hello World").in_blue() == "\x1b[34mHello World\x1b[0m"


def test_in_bold():
    assert in_bold("Hello World") == "\x1b[1mHello World\x1b[0m"
    assert in_bold("Hello World").in_bold() == "\x1b[1mHello World\x1b[0m"


def test_in_cyan():
    assert in_cyan("Hello World") == "\x1b[36mHello World\x1b[0m"
    assert in_cyan("Hello World").in_cyan() == "\x1b[36mHello World\x1b[0m"


def test_in_green():
    assert in_green("Hello World") == "\x1b[32mHello World\x1b[0m"
    assert in_green("Hello World").in_green() == "\x1b[32mHello World\x1b[0m"


def test_in_magenta():
    assert in_magenta("Hello World") == "\x1b[35mHello World\x1b[0m"
    assert in_magenta("Hello World").in_magenta() == "\x1b[35mHello World\x1b[0m"


def test_in_red():
    assert in_red("Hello World") == "\x1b[31mHello World\x1b[0m"
    assert in_red("Hello World").in_red() == "\x1b[31mHello World\x1b[0m"


def test_in_white():
    assert in_white("Hello World") == "\x1b[37mHello World\x1b[0m"
    assert in_white("Hello World").in_white() == "\x1b[37mHello World\x1b[0m"


def test_in_yellow():
    assert in_yellow("Hello World") == "\x1b[33mHello World\x1b[0m"
    assert in_yellow("Hello World").in_yellow() == "\x1b[33mHello World\x1b[0m"


def test_on_black():
    assert on_black("Hello World") == "\x1b[40mHello World\x1b[0m"
    assert on_black("Hello World").on_black() == "\x1b[40mHello World\x1b[0m"


def test_on_blue():
    assert on_blue("Hello World") == "\x1b[44mHello World\x1b[0m"
    assert on_blue("Hello World").on_blue() == "\x1b[44mHello World\x1b[0m"


def test_on_cyan():
    assert on_cyan("Hello World") == "\x1b[46mHello World\x1b[0m"
    assert on_cyan("Hello World").on_cyan() == "\x1b[46mHello World\x1b[0m"


def test_on_green():
    assert on_green("Hello World") == "\x1b[42mHello World\x1b[0m"
    assert on_green("Hello World").on_green() == "\x1b[42mHello World\x1b[0m"


def test_on_magenta():
    assert on_magenta("Hello World") == "\x1b[45mHello World\x1b[0m"
    assert on_magenta("Hello World").on_magenta() == "\x1b[45mHello World\x1b[0m"


def test_on_red():
    assert on_red("Hello World") == "\x1b[41mHello World\x1b[0m"
    assert on_red("Hello World").on_red() == "\x1b[41mHello World\x1b[0m"


def test_on_white():
    assert on_white("Hello World") == "\x1b[47mHello World\x1b[0m"
    assert on_white("Hello World").on_white() == "\x1b[47mHello World\x1b[0m"


def test_on_yellow():
    assert on_yellow("Hello World") == "\x1b[43mHello World\x1b[0m"
    assert on_yellow("Hello World").on_yellow() == "\x1b[43mHello World\x1b[0m"


def test_underlined():
    assert underlined("Hello World") == "\x1b[4mHello World\x1b[0m"
    assert underlined("Hello World").underlined() == "\x1b[4mHello World\x1b[0m"


def test_visual_len():
    assert visual_len(underlined("Hello World")) == len("Hello World")


class TestMixing:
    def test_in_white_on_red_in_bold_underlined(self, ):
        text = "In white, on red, in bold, and underlined"
        value = in_white(text).on_red().in_bold().underlined()
        assert value == "\x1b[4m\x1b[1m\x1b[41m\x1b[37m{}\x1b[0m".format(text)

    def test_non_strings(self, ):
        assert in_red(1) == "\x1b[31m1\x1b[0m"
