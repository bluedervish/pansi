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


from pansi.codes import rgb, bg, x, rv, rvx


print(f"""\
{bg.rgb('#0F0')}{rgb('#040')} !"#$%&'()*+,-./0123456789:;<=>?
@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]↑←
{rv}@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]↑←{rvx}
{bg.black}{rgb('#0F0')} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█{rgb('#FF0')} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█
{rgb('#00F')} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█{rgb('#F00')} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█
{rgb('#FFF')} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█{rgb('#0FF')} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█
{rgb('#F0F')} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█{rgb('#FF8000')} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█{x}""")
