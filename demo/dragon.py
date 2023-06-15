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


print(f"""\
{ansi.rgb['#040':'#0F0']} !"#$%&'()*+,-./0123456789:;<=>?
{ansi.rgb['#040':'#0F0']}@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]↑←
{ansi.bg.rgb['#040':'#0F0']}@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]↑←
{ansi.rgb['#0F0':'#000']} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█{ansi.rgb['#FF0']} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█
{ansi.rgb['#00F']} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█{ansi.rgb['#F00']} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█
{ansi.rgb['#FFF']} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█{ansi.rgb['#0FF']} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█
{ansi.rgb['#F0F']} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█{ansi.rgb['#FF8000']} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█{ansi.reset}""")
