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


from io import StringIO

from pansi import ansi
from pansi.console import Console


def test_console_write():
    captured = StringIO()
    con = Console(__name__, out=captured)
    con.write("hello, world")
    assert captured.getvalue() == "hello, world\n"


def test_console_debug_output():
    captured = StringIO()
    con = Console(__name__, out=captured, verbosity=1)
    con.debug("hello, world")
    assert captured.getvalue() == "{cyan}hello, world{_}\n".format(**ansi)


def test_console_info_output():
    captured = StringIO()
    con = Console(__name__, out=captured)
    con.info("hello, world")
    assert captured.getvalue() == "hello, world\n"


def test_console_warning_output():
    captured = StringIO()
    con = Console(__name__, out=captured, verbosity=1)
    con.warning("hello, world")
    assert captured.getvalue() == "{yellow}hello, world{_}\n".format(**ansi)


def test_console_error_output():
    captured = StringIO()
    con = Console(__name__, out=captured, verbosity=1)
    con.error("hello, world")
    assert captured.getvalue() == "{red}hello, world{_}\n".format(**ansi)


def test_console_critical_output():
    captured = StringIO()
    con = Console(__name__, out=captured, verbosity=1)
    con.critical("hello, world")
    assert captured.getvalue() == "{RED}hello, world{_}\n".format(**ansi)
