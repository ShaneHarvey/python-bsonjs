# Copyright 2016 MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import subprocess
import sys

try:
    from setuptools import setup, Extension
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, Extension

with open("README.rst") as f:
    try:
        description = f.read()
    except Exception:
        description = ""

tests_require = ['pymongo']
if sys.version_info[:2] == (2, 6):
    tests_require.append("unittest2 >= 0.5.1")
    test_suite = "unittest2.collector"
else:
    test_suite = "test"


def pkgconfig(lib, flags):
    try:
        proc = subprocess.Popen(['pkg-config'] + flags + [lib],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                universal_newlines=True)
    except OSError as exc:
        exit('pkg-config failed: {0},'
             'is pkg-config installed?'.format(exc.strerror))

    out, err = proc.communicate()
    if proc.returncode != 0:
        exit('Failed to determine compile flags for libbson: {0}'.format(err))

    return out.strip().split()


def compile_args(lib):
    return pkgconfig(lib, ['--cflags'])


def link_args(lib):
    return pkgconfig(lib, ['--libs'])


setup(
    name="python-bsonjs",
    version="0.1.0.dev0",
    description="A library for converting between BSON and JSON.",
    long_description=description,
    author="Shane Harvey",
    author_email="shane.harvey@mongodb.com",
    url="https://github.com/mongodb-labs/python-bsonjs",
    keywords=["BSON", "JSON", "PyMongo"],
    test_suite=test_suite,
    tests_require=tests_require,
    license="Apache License, Version 2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython"],
    ext_modules=[
        Extension(
            "bsonjs",
            extra_compile_args=compile_args('libbson-1.0'),
            extra_link_args=link_args('libbson-1.0'),
            sources=["src/bsonjs.c"]
        )
    ]
)