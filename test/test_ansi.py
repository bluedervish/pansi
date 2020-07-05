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


from pansi import ansi


def test_ansi_reset():
    assert "{reset}".format(**ansi) == "\x1b[0m"


def test_ansi_reset_alias():
    assert "{_}".format(**ansi) == "\x1b[0m"


def test_ansi_black():
    assert "{black}".format(**ansi) == "\x1b[30m"


def test_ansi_red():
    assert "{red}".format(**ansi) == "\x1b[31m"


def test_ansi_green():
    assert "{green}".format(**ansi) == "\x1b[32m"


def test_ansi_yellow():
    assert "{yellow}".format(**ansi) == "\x1b[33m"


def test_ansi_blue():
    assert "{blue}".format(**ansi) == "\x1b[34m"


def test_ansi_magenta():
    assert "{magenta}".format(**ansi) == "\x1b[35m"


def test_ansi_cyan():
    assert "{cyan}".format(**ansi) == "\x1b[36m"


def test_ansi_white():
    assert "{white}".format(**ansi) == "\x1b[37m"


def test_ansi_bright_black():
    assert "{BLACK}".format(**ansi) == "\x1b[90m"


def test_ansi_bright_red():
    assert "{RED}".format(**ansi) == "\x1b[91m"


def test_ansi_bright_green():
    assert "{GREEN}".format(**ansi) == "\x1b[92m"


def test_ansi_bright_yellow():
    assert "{YELLOW}".format(**ansi) == "\x1b[93m"


def test_ansi_bright_blue():
    assert "{BLUE}".format(**ansi) == "\x1b[94m"


def test_ansi_bright_magenta():
    assert "{MAGENTA}".format(**ansi) == "\x1b[95m"


def test_ansi_bright_cyan():
    assert "{CYAN}".format(**ansi) == "\x1b[96m"


def test_ansi_bright_white():
    assert "{WHITE}".format(**ansi) == "\x1b[97m"


def test_ansi_rgb_3():
    assert "{rgb[#F90]}".format(**ansi) == "\x1b[38;2;255;153;0m"


def test_ansi_rgb_6():
    assert "{rgb[#FF8000]}".format(**ansi) == "\x1b[38;2;255;128;0m"


def test_ansi_rgb_bad_values():
    try:
        _ = "{rgb[#XXYYZZ]}".format(**ansi)
    except ValueError:
        assert True
    else:
        assert False


def test_ansi_rgb_bad_format():
    try:
        _ = "{rgb[#31415926535]}".format(**ansi)
    except ValueError:
        assert True
    else:
        assert False
