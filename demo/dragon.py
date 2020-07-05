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


print("""{rgb[#040]}{bg.rgb[#0F0]} !"#$%&'()*+,-./0123456789:;<=>?{_}""".format(**ansi))
print("""{rgb[#040]}{bg.rgb[#0F0]}@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]↑←{_}""".format(**ansi))
print("""{rgb[#0F0]}{bg.rgb[#040]}@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]↑←{_}""".format(**ansi))
print("""{rgb[#0F0]}{bg.rgb[#000]} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█{_}""".format(**ansi), end="")
print("""{rgb[#FF0]}{bg.rgb[#000]} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█{_}""".format(**ansi))
print("""{rgb[#00F]}{bg.rgb[#000]} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█{_}""".format(**ansi), end="")
print("""{rgb[#F00]}{bg.rgb[#000]} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█{_}""".format(**ansi))
print("""{rgb[#FFF]}{bg.rgb[#000]} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█{_}""".format(**ansi), end="")
print("""{rgb[#0FF]}{bg.rgb[#000]} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█{_}""".format(**ansi))
print("""{rgb[#F0F]}{bg.rgb[#000]} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█{_}""".format(**ansi), end="")
print("""{rgb[#FF8000]}{bg.rgb[#000]} ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█{_}""".format(**ansi))

