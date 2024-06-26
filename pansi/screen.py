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


from sys import stdin, stdout
from termios import tcgetattr, tcsetattr, TCSAFLUSH
from tty import setcbreak

from pansi.control import ESC, CSI, green, x


class Screen:

    def __init__(self, cout=stdout, cin=stdin, cbreak=True, cursor=False):
        self.cout = cout
        self.cin = cin
        self.cbreak = cbreak
        self.cursor = cursor
        self.original_mode = None

    def __enter__(self):
        if not self.cursor:
            self.hide_cursor()
        self.show()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.hide()
        self.show_cursor()

    def read_response(self):
        response = []
        while response[-2:] != [ESC, "["]:
            ch = self.cin.read(1)
            response.append(ch)
        args = []
        function = None
        digit = None
        while True:
            ch = self.cin.read(1)
            if '0' <= ch <= '9':
                if digit is None:
                    digit = int(ch)
                else:
                    digit = 10 * digit + int(ch)
            else:
                if digit is not None:
                    args.append(digit)
                    digit = None
                if ch == ';':
                    continue
                else:
                    function = ch
                    break
        return tuple(args), function

    def cell_size_px(self):
        self.cout.write(f"{CSI}16t")
        self.cout.flush()
        args, function = self.read_response()
        if function == "t":
            if args[0] == 6:
                return args[1:]
            else:
                raise OSError(f"Unexpected response {function!r} {args[0]!r}")
        else:
            raise OSError(f"Unexpected response {function!r}")

    def size(self):
        self.cout.write(f"{CSI}18t")
        self.cout.flush()
        args, function = self.read_response()
        if function == "t":
            if args[0] == 8:
                return args[1:]
            else:
                raise OSError(f"Unexpected response {function!r} {args[0]!r}")
        else:
            raise OSError(f"Unexpected response {function!r}")

    def cursor_up(self, n=1):
        self.cout.write(f"{CSI}{n}A")

    def cursor_down(self, n=1):
        self.cout.write(f"{CSI}{n}B")

    def cursor_forward(self, n=1):
        self.cout.write(f"{CSI}{n}C")

    def cursor_back(self, n=1):
        self.cout.write(f"{CSI}{n}D")

    def cursor_next_line(self, n=1):
        self.cout.write(f"{CSI}{n}E")

    def cursor_previous_line(self, n=1):
        self.cout.write(f"{CSI}{n}F")

    def cursor_horizontal_absolute(self, column=1):
        self.cout.write(f"{CSI}{column}G")

    @property
    def cursor_position(self):
        self.cout.write(f"{CSI}6n")
        self.cout.flush()
        args, function = self.read_response()
        if function == "R":
            return args
        else:
            raise OSError(f"Unexpected response {function!r}")

    @cursor_position.setter
    def cursor_position(self, row_column):
        row, column = row_column
        self.cout.write(f"{CSI}{row};{column}H")

    def cursor_forward_tab(self, stops=1):
        self.cout.write(f"{CSI}{stops}I")

    def erase_in_display(self, n=0):
        self.cout.write(f"{CSI}{n}J")

    def erase_in_line(self, n=0):
        self.cout.write(f"{CSI}{n}K")

    def scroll_up(self, n=1):
        self.cout.write(f"{CSI}{n}S")

    def scroll_down(self, n=1):
        self.cout.write(f"{CSI}{n}T")

    def horizontal_vertical_position(self, row=1, column=1):
        self.cout.write(f"{CSI}{row};{column}f")

    def show(self):
        self.cout.write(f"{CSI}?1049h")
        self.cout.flush()
        self.original_mode = tcgetattr(self.cout)
        setcbreak(self.cout)
        # TODO: keypad(1)

    def hide(self):
        # TODO: keypad(0)
        tcsetattr(self.cout, TCSAFLUSH, self.original_mode)
        self.cout.write(f"{CSI}?1049l")
        self.cout.flush()

    def show_cursor(self):
        self.cout.write(f"{CSI}?25h")
        self.cout.flush()

    def hide_cursor(self):
        self.cout.write(f"{CSI}?25l")
        self.cout.flush()


def full():
    with Screen() as screen:
        screen.cout.write(f"{green}hello{x}, the screen size is {screen.size()!r}\n")
        screen.cout.write(f"the cell size is {screen.cell_size_px()!r}\n")
        screen.cursor_position = 13, 7
        screen.cout.write(repr(screen.cursor_position))
        screen.cout.flush()
        from time import sleep
        sleep(3)
