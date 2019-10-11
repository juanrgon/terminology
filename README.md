# Terminology

[![Build Status](https://travis-ci.org/juanrgon/terminology.svg?branch=master)](https://travis-ci.org/juanrgon/terminology)

A simple way to color terminal text! ❤️ 💛 💚 💙 💜

## Color Text

```python
from terminology import in_red, in_yellow, in_green, in_blue, in_magenta

print(in_red("it's"), in_yellow("a"), in_green("double"), in_blue("rainbow"), in_magenta("dude..."))
```

_Output_

![alt text][coloring]

[coloring]: https://raw.githubusercontent.com/juanrgon/terminology/master/pics/coloring.png
 "Coloring"

## Color Text Background

```python
from terminology import on_green, on_yellow, on_red

print(on_green("OK"), on_yellow("WARNING"), on_red("DANGER")
```

_Output_

![alt text][background colors]

[background colors]: https://raw.githubusercontent.com/juanrgon/terminology/master/pics/background.png
 "Background Colors"

## Emphasize Text with Bold and Underlining

```python
from terminology import in_bold, underlined

print(in_bold("Chapter 1"))
print("- ", underlined("Section i"))
print("- ", underlined("Section ii"), "\n")

print(in_bold("Chapter 2"))
print("- ", underlined("Section i"), '\n')
```

_Output_

![alt text][bold and underline]

[bold and underline]: https://raw.githubusercontent.com/juanrgon/terminology/master/pics/bold_and_underline.png
 "Bold and Underline"
