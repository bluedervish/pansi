#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
#
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


from fcntl import ioctl
from sys import stdin, stdout
from termios import tcgetattr, tcsetattr, TCSAFLUSH, TIOCGWINSZ
from tty import setcbreak

from pansi.codes import ESC, CSI, cur, x, bold, faint, italic, rev, blink, strike, underline, BLACK, bg, RED, GREEN, \
    YELLOW, BLUE, MAGENTA, CYAN, WHITE, black, red, green, yellow, blue, magenta, cyan, white


class Screen:

    @classmethod
    def wrapper(cls, func, *args, **kwargs):
        with Screen() as screen:
            return func(screen, *args, **kwargs)

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

    def _read_ss3(self, seq):
        while True:
            ch = self.cin.read(1)
            seq += ch
            if 0x40 <= ord(ch) <= 0x7E:
                break
        return seq

    def _read_csi(self, seq):
        while True:
            ch = self.cin.read(1)
            seq += ch
            if 0x40 <= ord(ch) <= 0x7E:
                break
        return seq

    def _read_esc(self, seq):
        ch = self.cin.read(1)
        seq += ch
        if ch == "[":
            return self._read_csi(seq)
        elif ch == "O":
            return self._read_ss3(seq)
        else:
            raise OSError(f"Unknown input sequence {seq!r}")

    def read_key(self):
        seq = ""
        ch = self.cin.read(1)
        seq += ch
        if ch == ESC:
            return self._read_esc(seq)
        else:
            return seq

    def read_response(self):
        seq = self.read_key()
        if seq.startswith(f"{ESC}["):
            args = tuple(map(int, seq[2:-1].split(";")))
            function = seq[-1]
            return args, function
        else:
            raise OSError(f"Unexpected response {seq!r}")

    @property
    def size_px(self):
        self.cout.write(f"{CSI}14t")
        self.cout.flush()
        args, function = self.read_response()
        if function == "t":
            if args[0] == 4:
                return args[1:]
            else:
                raise OSError(f"Unexpected response {function!r} {args[0]!r}")
        else:
            raise OSError(f"Unexpected response {function!r}")

    @property
    def cell_size(self):
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

    @property
    def size(self):
        import struct
        import os
        try:
            # Create a buffer for the ioctl call
            buf = struct.pack('HHHH', 0, 0, 0, 0)

            # Make the ioctl call
            fd = os.open(os.ctermid(), os.O_RDONLY)
            result = ioctl(fd, TIOCGWINSZ, buf)
            os.close(fd)

            # Unpack the result
            rows, cols, _, _ = struct.unpack('HHHH', result)

            return rows, cols
        except OSError:
            # Fallback method using environment variables
            return (int(os.environ.get('LINES', 24)),
                    int(os.environ.get('COLUMNS', 80)))

    @property
    def cur_pos(self):
        self.cout.write(f"{CSI}6n")
        self.cout.flush()
        args, function = self.read_response()
        if function == "R":
            return args
        else:
            raise OSError(f"Unexpected response {function!r}")

    @cur_pos.setter
    def cur_pos(self, row_column):
        row, column = row_column
        self.cout.write(f"{CSI}{row};{column}H")

    def cursor_forward_tab(self, stops=1):
        self.cout.write(f"{CSI}{stops}I")

    def clear(self):
        self.cout.write(f"{CSI}H{CSI}2J")

    def show(self):
        self.cout.write(f"{CSI}?1049h")
        self.cout.flush()
        self.original_mode = tcgetattr(self.cout)
        setcbreak(self.cout)
        # self.keypad_on()

    def hide(self):
        # self.keypad_off()
        tcsetattr(self.cout, TCSAFLUSH, self.original_mode)
        self.cout.write(f"{CSI}?1049l")
        self.cout.flush()

    def show_cursor(self):
        self.cout.write(f"{CSI}?25h")
        self.cout.flush()

    def hide_cursor(self):
        self.cout.write(f"{CSI}?25l")
        self.cout.flush()

    # def keypad_on(self):
    #     self.cout.write(f"{CSI}?1h{ESC}=")
    #     self.cout.flush()

    # def keypad_off(self):
    #     self.cout.write(f"{CSI}?1l{ESC}>")
    #     self.cout.flush()

    def write(self, *values):
        for value in values:
            self.cout.write(str(value))

    def flush(self):
        self.cout.flush()


def test_card(screen: Screen):
    height, width = screen.size
    screen.clear()
    screen.write(f"TL{cur.hpos(width - 1)}TR")

    screen.cur_pos = 24, 1
    screen.write(f"{BLACK}{bg.black}     "
                 f"{RED}{bg.red}     ")
    screen.write(f"{GREEN}{bg.green}     ")
    screen.write(f"{YELLOW}{bg.yellow}     ")
    screen.write(f"{BLUE}{bg.blue}     ")
    screen.write(f"{MAGENTA}{bg.magenta}     ")
    screen.write(f"{CYAN}{bg.cyan}     ")
    screen.write(f"{WHITE}{bg.white}     ")
    screen.write(f"{black}{bg.BLACK}     ")
    screen.write(f"{red}{bg.RED}     ")
    screen.write(f"{green}{bg.GREEN}     ")
    screen.write(f"{yellow}{bg.YELLOW}     ")
    screen.write(f"{blue}{bg.BLUE}     ")
    screen.write(f"{magenta}{bg.MAGENTA}     ")
    screen.write(f"{cyan}{bg.CYAN}     ")
    screen.write(f"{white}{bg.WHITE}     {x}")

    if height == 24:
        screen.write(cur.pos(height, 1), f"{bg.black}BL{x}")
    else:
        screen.write(cur.pos(height, 1), f"BL")
    if height == 24 and width == 80:
        screen.write(cur.pos(height, width - 1), f"{black}{bg.WHITE}BR{x}")
    else:
        screen.write(cur.pos(height, width - 1), f"BR")

    for line in range(2, 24):
        screen.cur_pos = line, 1
        g = 11 * line - 9
        screen.write(f"{faint}{line:02}{faint.off}{cur.hpos(79)}{bg.rgb(g, g, g)}  {bg}")

    screen.write(cur.pos(2, 5), f" !\"#$%&'()*+,-./0123456789;:<=>?")
    screen.write(cur.pos(3, 5), "@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_")
    screen.write(cur.pos(4, 5), "`abcdefghijklmnopqrstuvwxyz{|}~")

    screen.write(f"{cur.pos(6, 5)}Emphasis  : {bold}bold{bold.off} {faint}faint{faint.off} {italic}italic{italic.off}")
    screen.write(f"{cur.pos(7, 5)}Underline : {underline}single{underline.off} {underline.double}double{underline.off}")
    screen.write(f"{cur.pos(8, 5)}Blink     : {blink}slow{blink.off} {blink.fast}fast{blink.off}")
    screen.write(f"{cur.pos(9, 5)}Reverse   : {rev}reverse{rev.off}")
    screen.write(cur.pos(10, 5), f"Strike    : {strike}strike{strike.off}")

    screen.flush()
    screen.cur_pos = 10, 10
    while True:
        k = screen.read_key()
        screen.write(f"{k!r} ")
        screen.flush()


if __name__ == "__main__":
    Screen.wrapper(test_card)
