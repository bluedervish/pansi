#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright 2011-2020, Nigel Small
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


from os.path import dirname, join as path_join
from setuptools import setup


from pansi import (
    __author__,
    __email__,
    __license__,
    __package__,
    __version__,
)

source_url = "https://github.com/technige/pansi"


with open(path_join(dirname(__file__), "README.rst")) as f:
    README = f.read().replace(".. image :: art/",
                              ".. image :: {}/raw/master/art/".format(source_url))

package_metadata = {
    "name": __package__,
    "version": __version__,
    "description": "ANSI escape code library for Python",
    "long_description": README,
    "author": __author__,
    "author_email": __email__,
    "url": source_url,
    "project_urls": {
        "Bug Tracker": "{}/issues".format(source_url),
        "Source Code": source_url,
    },
    "entry_points": {
        "console_scripts": [
        ],
    },
    "packages": [
    ],
    "py_modules": [
        "pansi",
    ],
    "install_requires": [
    ],
    "extras_require": {
    },
    "license": __license__,
    "classifiers": [
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Environment :: Console :: Curses",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Console Fonts",
        "Topic :: System :: Shells",
        "Topic :: Terminals",
        "Topic :: Terminals :: Terminal Emulators/X Terminals",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Markup",
        "Topic :: Utilities",
    ],
}

setup(**package_metadata)
