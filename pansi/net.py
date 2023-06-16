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


from io import BytesIO

from urllib3 import PoolManager as HTTP


def download(uri, method="GET", expected_status=200):
    http = HTTP()
    rs = http.request(method, str(uri))
    if rs.status == expected_status:
        return BytesIO(rs.data)
    else:
        raise RuntimeError(f"{method} {uri} -> {rs.status}")


class URI:

    @classmethod
    def parse(cls, s):
        scheme, colon, ssp = s.partition(":")
        if not colon:
            scheme, ssp = None, scheme
        apq, hash_sign, fragment = ssp.partition("#")
        if not hash_sign:
            fragment = None
        hierarchical_part, question_mark, query = apq.partition("?")
        if not question_mark:
            query = None
        if hierarchical_part.startswith("//"):
            hierarchical_part = hierarchical_part[2:]
            slash = hierarchical_part.find("/")
            if slash:
                authority = hierarchical_part[:slash]
                path = hierarchical_part[slash:]
            else:
                authority = hierarchical_part
                path = ""
        else:
            authority = None
            path = hierarchical_part
        return cls(scheme, authority, path, query, fragment)

    def __init__(self, scheme=None, authority=None, path="", query=None, fragment=None):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __str__(self):
        if self.authority is None:
            s = [self.path]
        else:
            s = ["//", self.authority, self.path]
        if self.query is not None:
            s.extend(["?", self.query])
        if self.fragment is not None:
            s.extend(["#", self.fragment])
        if self.scheme is not None:
            s = [self.scheme, ":"] + s
        return "".join(s)
