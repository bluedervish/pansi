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


__author__ = "Nigel Small"
__copyright__ = "2020, Nigel Small"
__email__ = "technige@nige.tech"
__license__ = "Apache License, Version 2.0"
__package__ = "pansi"
__version__ = "2023.6.0"


CSI = f"\x1B["


class ANSI(Mapping, object):

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


_weight = ANSI(
    normal=f"{CSI}22m",
    bold=f"{CSI}1m",
    light=f"{CSI}2m",
)

_style = ANSI(
    normal=f"{CSI}23m",
    italic=f"{CSI}3m",
    fraktur=f"{CSI}20m",
)

_border = ANSI(
    none=f"{CSI}54m",
    frame=f"{CSI}51m",
    circle=f"{CSI}52m",
)


class RGB(object):

    def __init__(self, bg=False):
        self.bg = bg
        self._fg_template = f"{CSI}38;2;%s;%s;%sm"
        self._bg_template = f"{CSI}48;2;%s;%s;%sm"

    def __getitem__(self, code):
        if isinstance(code, slice):
            r0, g0, b0 = self.parse_hex_code(code.start)
            r1, g1, b1 = self.parse_hex_code(code.stop)
            if self.bg:
                return (self._fg_template % (r1, g1, b1)) + (self._bg_template % (r0, g0, b0))
            else:
                return (self._fg_template % (r0, g0, b0)) + (self._bg_template % (r1, g1, b1))
        else:
            r, g, b = self.parse_hex_code(code)
            return (self._bg_template if self.bg else self._fg_template) % (r, g, b)

    @classmethod
    def parse_hex_code(cls, code):
        if len(code) == 4 and code[0] == "#":
            # rgb[#XXX]
            r = int(code[1], 16) * 17
            g = int(code[2], 16) * 17
            b = int(code[3], 16) * 17
        elif len(code) == 7 and code[0] == "#":
            # rgb[#XXXXXX]
            r = int(code[1:3], 16)
            g = int(code[3:5], 16)
            b = int(code[5:7], 16)
        else:
            raise ValueError("Unknown hex code %r" % code)
        return r, g, b


_fg = ANSI(

    black=f"{CSI}30m",
    red=f"{CSI}31m",
    green=f"{CSI}32m",
    yellow=f"{CSI}33m",
    blue=f"{CSI}34m",
    magenta=f"{CSI}35m",
    cyan=f"{CSI}36m",
    white=f"{CSI}37m",
    rgb=RGB(),
    reset=f"{CSI}39m",

    BLACK=f"{CSI}90m",
    RED=f"{CSI}91m",
    GREEN=f"{CSI}92m",
    YELLOW=f"{CSI}93m",
    BLUE=f"{CSI}94m",
    MAGENTA=f"{CSI}95m",
    CYAN=f"{CSI}96m",
    WHITE=f"{CSI}97m",

)

_bg = ANSI(

    black=f"{CSI}40m",
    red=f"{CSI}41m",
    green=f"{CSI}42m",
    yellow=f"{CSI}43m",
    blue=f"{CSI}44m",
    magenta=f"{CSI}45m",
    cyan=f"{CSI}46m",
    white=f"{CSI}47m",
    rgb=RGB(bg=True),
    reset=f"{CSI}49m",

    BLACK=f"{CSI}100m",
    RED=f"{CSI}101m",
    GREEN=f"{CSI}102m",
    YELLOW=f"{CSI}103m",
    BLUE=f"{CSI}104m",
    MAGENTA=f"{CSI}105m",
    CYAN=f"{CSI}106m",
    WHITE=f"{CSI}107m",

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
    rev=f"{CSI}7m",
    _rev=f"{CSI}27m",

    # Weight
    weight=_weight,
    _b=_weight.normal,
    b=_weight.bold,

    # Style
    style=_style,
    _i=_style.normal,
    i=_style.italic,

    # Underline
    _u=f"{CSI}24m",
    u=f"{CSI}4m",
    uu=f"{CSI}21m",

    # Strike through
    _s=f"{CSI}29m",
    s=f"{CSI}9m",

    # Overline
    _o=f"{CSI}55m",
    o=f"{CSI}53m",

    # Blinking
    _blink=f"{CSI}25m",
    blink=f"{CSI}5m",
    BLINK=f"{CSI}6m",

    # Conceal/Reveal
    hide=f"{CSI}8m",
    show=f"{CSI}28m",

    # Font
    font0=f"{CSI}10m",
    font1=f"{CSI}11m",
    font2=f"{CSI}12m",
    font3=f"{CSI}13m",
    font4=f"{CSI}14m",
    font5=f"{CSI}15m",
    font6=f"{CSI}16m",
    font7=f"{CSI}17m",
    font8=f"{CSI}18m",
    font9=f"{CSI}19m",

    # Border
    border=_border,

    # Superscript/Subscript
    sup=f"{CSI}73m",
    sub=f"{CSI}74m",

    # Reset
    reset=f"{CSI}0m",
    _=f"{CSI}0m",

)
