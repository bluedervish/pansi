#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright 2020, Nigel Small
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping


__author__ = "Nigel Small"
__copyright__ = "2020, Nigel Small"
__email__ = "pansi@nige.tech"
__license__ = "Apache License, Version 2.0"
__package__ = "pansi"
__version__ = "0.0.dev1"


class ANSI(Mapping, object):

    def __init__(self, **codes):
        self.__codes = dict(codes)

    def __getitem__(self, key):
        return self.__codes[key]

    def __len__(self):
        return len(self.__codes)

    def __iter__(self):
        return iter(self.__codes)

    def __dir__(self):
        return list(self.__codes)

    def __getattr__(self, name):
        try:
            return self.__codes[name]
        except KeyError:
            raise AttributeError(name)


_weight = ANSI(
    normal="\x1b[22m",
    bold="\x1b[1m",
    light="\x1b[2m",
)

_style = ANSI(
    normal="\x1b[23m",
    italic="\x1b[3m",
    fraktur="\x1b[20m",
)

_border = ANSI(
    none="\x1b[54m",
    frame="\x1b[51m",
    circle="\x1b[52m",
)


class RGB(object):

    def __init__(self, bg=False):
        if bg:
            self.__template = "\x1b[48;2;%s;%s;%sm"
        else:
            self.__template = "\x1b[38;2;%s;%s;%sm"

    def __getitem__(self, code):
        if len(code) == 3:
            # rgb[XXX]
            r = int(code[0], 16) * 17
            g = int(code[1], 16) * 17
            b = int(code[2], 16) * 17
        elif len(code) == 4 and code[0] == "#":
            # rgb[#XXX]
            r = int(code[1], 16) * 17
            g = int(code[2], 16) * 17
            b = int(code[3], 16) * 17
        elif len(code) == 6:
            # rgb[XXXXXX]
            r = int(code[0:2], 16)
            g = int(code[2:4], 16)
            b = int(code[4:6], 16)
        elif len(code) == 7 and code[0] == "#":
            # rgb[#XXXXXX]
            r = int(code[1:3], 16)
            g = int(code[3:5], 16)
            b = int(code[5:7], 16)
        else:
            raise ValueError("Unknown hex code %r" % code)
        return self.__template % (r, g, b)


_fg = ANSI(

    black="\x1b[30;1m",
    red="\x1b[31;1m",
    green="\x1b[32;1m",
    yellow="\x1b[33;1m",
    blue="\x1b[34;1m",
    magenta="\x1b[35;1m",
    cyan="\x1b[36;1m",
    white="\x1b[37;1m",
    rgb=RGB(),
    reset="\x1b[39;1m",

    BLACK="\x1b[90;1m",
    RED="\x1b[91;1m",
    GREEN="\x1b[92;1m",
    YELLOW="\x1b[93;1m",
    BLUE="\x1b[94;1m",
    MAGENTA="\x1b[95;1m",
    CYAN="\x1b[96;1m",
    WHITE="\x1b[97;1m",

)

_bg = ANSI(

    black="\x1b[40;1m",
    red="\x1b[41;1m",
    green="\x1b[42;1m",
    yellow="\x1b[43;1m",
    blue="\x1b[44;1m",
    magenta="\x1b[45;1m",
    cyan="\x1b[46;1m",
    white="\x1b[47;1m",
    rgb=RGB(bg=True),
    reset="\x1b[49;1m",

    BLACK="\x1b[100;1m",
    RED="\x1b[101;1m",
    GREEN="\x1b[102;1m",
    YELLOW="\x1b[103;1m",
    BLUE="\x1b[104;1m",
    MAGENTA="\x1b[105;1m",
    CYAN="\x1b[106;1m",
    WHITE="\x1b[107;1m",

)

ansi = ANSI(

    # Foreground colour
    fg=_fg,
    black=_fg.black,
    red=_fg.red,
    green=_fg.green,
    yellow=_fg.yellow,
    blue=_fg.blue,
    magenta=_fg.magenta,
    cyan=_fg.cyan,
    white=_fg.white,
    rgb=_fg.rgb,
    BLACK=_fg.BLACK,
    RED=_fg.RED,
    GREEN=_fg.GREEN,
    YELLOW=_fg.YELLOW,
    BLUE=_fg.BLUE,
    MAGENTA=_fg.MAGENTA,
    CYAN=_fg.CYAN,
    WHITE=_fg.WHITE,

    # Background colour
    bg=_bg,

    # Reversed colours
    rev="\x1b[7m",
    _rev="\x1b[27m",

    # Weight
    weight=_weight,
    _b=_weight.normal,
    b=_weight.bold,

    # Style
    style=_style,
    _i=_style.normal,
    i=_style.italic,

    # Underline
    _u="\x1b[24m",
    u="\x1b[4m",
    uu="\x1b[21m",

    # Strike through
    _s="\x1b[29m",
    s="\x1b[9m",

    # Overline
    _o="\x1b[55m",
    o="\x1b[53m",

    # Blinking
    _blink="\x1b[25m",
    blink="\x1b[5m",
    BLINK="\x1b[6m",

    # Conceal/Reveal
    hide="\x1b[8m",
    show="\x1b[28m",

    # Font
    font0="\x1b[10m",
    font1="\x1b[11m",
    font2="\x1b[12m",
    font3="\x1b[13m",
    font4="\x1b[14m",
    font5="\x1b[15m",
    font6="\x1b[16m",
    font7="\x1b[17m",
    font8="\x1b[18m",
    font9="\x1b[19m",

    # Border
    border=_border,

    # Superscript/Subscript
    sup="\x1b[73m",
    sub="\x1b[74m",

    # Reset
    reset="\x1b[0m",
    _="\x1b[0m",

)
