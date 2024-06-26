#!/usr/bin/env python3
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


from collections.abc import Mapping


# C0 control codes
BEL = "\x07"
BS = "\x08"
HT = "\x09"
LF = "\x0A"
FF = "\x0C"
CR = "\x0D"
ESC = "\x1B"

# C1 control codes
SS2 = f"{ESC}N"
SS3 = f"{ESC}O"
DCS = f"{ESC}P"
CSI = f"{ESC}["
ST = f"{ESC}\\"
OSC = f"{ESC}]"
SOS = f"{ESC}X"
PM = f"{ESC}^"
APC = f"{ESC}_"


class CodeSet(Mapping, object):

    def __init__(self, **codes):
        self.__codes = dict(codes)

    def __getitem__(self, key):
        return self.__codes[key]

    def __len__(self):
        return len(self.__codes)    # pragma: no cover

    def __iter__(self):
        return iter(self.__codes)   # pragma: no cover

    def __dir__(self):
        return list(self.__codes)   # pragma: no cover

    def __getattr__(self, name):
        try:
            return self.__codes[name]
        except KeyError:
            raise AttributeError(name)


# SGR


def sgr(*args):
    return f"{CSI}{';'.join(map(str, args))}m"


class RGB(object):

    def __init__(self, ground):
        self.ground = ground

    def __call__(self, *args):
        n_args = len(args)
        if n_args == 1:
            code = str(args[0])
            if code.startswith("#"):
                code_len = len(code)
                if code_len == 4:
                    # '#XXX'
                    r = int(code[1], 16) * 17
                    g = int(code[2], 16) * 17
                    b = int(code[3], 16) * 17
                elif code_len == 7:
                    # '#XXXXXX'
                    r = int(code[1:3], 16)
                    g = int(code[3:5], 16)
                    b = int(code[5:7], 16)
                else:
                    raise ValueError(f"Unparseable hex code {code!r}")
                return sgr(self.ground, 2, r, g, b)
            else:
                raise ValueError(f"Unparseable color code {args[0]!r}")
        elif n_args == 3:
            return sgr(self.ground, 2, *args)
        else:
            raise TypeError("Unusable color arguments")


# Foreground
fg = CodeSet(
    black=sgr(30),
    red=sgr(31),
    green=sgr(32),
    yellow=sgr(33),
    blue=sgr(34),
    magenta=sgr(35),
    cyan=sgr(36),
    white=sgr(37),
    rgb=RGB(38),
    default=sgr(39),
    BLACK=sgr(90),
    RED=sgr(91),
    GREEN=sgr(92),
    YELLOW=sgr(93),
    BLUE=sgr(94),
    MAGENTA=sgr(95),
    CYAN=sgr(96),
    WHITE=sgr(97),
)
black = sgr(30)
red = sgr(31)
green = sgr(32)
yellow = sgr(33)
blue = sgr(34)
magenta = sgr(35)
cyan = sgr(36)
white = sgr(37)
rgb = RGB(38)
BLACK = sgr(90)
RED = sgr(91)
GREEN = sgr(92)
YELLOW = sgr(93)
BLUE = sgr(94)
MAGENTA = sgr(95)
CYAN = sgr(96)
WHITE = sgr(97)

# Background
bg = CodeSet(
    black=sgr(40),
    red=sgr(41),
    green=sgr(42),
    yellow=sgr(43),
    blue=sgr(44),
    magenta=sgr(45),
    cyan=sgr(46),
    white=sgr(47),
    rgb=RGB(48),
    default=sgr(49),
    BLACK=sgr(100),
    RED=sgr(101),
    GREEN=sgr(102),
    YELLOW=sgr(103),
    BLUE=sgr(104),
    MAGENTA=sgr(105),
    CYAN=sgr(106),
    WHITE=sgr(107),
)

# Reversed colours
reverse = CodeSet(
    on=sgr(7),
    off=sgr(27),
)
r = sgr(7)
rx = sgr(27)

# Weight
weight = CodeSet(
    bold=sgr(1),
    light=sgr(2),
    normal=sgr(22),
)
b = sgr(1)
bx = sgr(22)

# Style
style = CodeSet(
    italic=sgr(3),
    normal=sgr(23),
)
i = sgr(3)
ix = sgr(23)

# Underline
underline = CodeSet(
    single=sgr(4),
    double=sgr(21),
    none=sgr(24),
    color=RGB(58),
)
u = sgr(4)
uu = sgr(21)
ux = sgr(24)

# Strike through
strike = CodeSet(
    on=sgr(9),
    off=sgr(29),
)
s = sgr(9)
sx = sgr(29)

# Reset
x = sgr(0)
