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


version = "0.0.dev0"  # TODO import from module


with open(path_join(dirname(__file__), "README.rst")) as f:
    README = f.read()

package_metadata = {
    "name": "pansi",
    "version": version,
    "description": "ANSI escape code library for Python",
    "long_description": README,
    "author": "Nigel Small",
    "author_email": "technige@nige.tech",
    "url": "https://nige.tech/pansi",
    "project_urls": {
        "Bug Tracker": "https://github.com/technige/pansi/issues",
        "Source Code": "https://github.com/technige/pansi",
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
    "license": "",  # TODO
    "classifiers": [
        "Development Status :: 6 - Mature",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
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
        "Topic :: Database",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
    ],
}

setup(**package_metadata)
