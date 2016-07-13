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

import os
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

tests_require = ["pymongo"]
if sys.version_info[:2] == (2, 6):
    tests_require.append("unittest2 >= 0.5.1")
    test_suite = "unittest2.collector"
else:
    test_suite = "test"


def run_or_exit(args):
    try:
        subprocess.check_output(args, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as err:
        exit(err.output)


def install_libbson():
    install_dir = os.path.join(os.getcwd(), "libbson", "install_dir")
    if os.path.isdir(install_dir):
        return
    try:
        os.chdir("libbson")
        if sys.platform == "win32":
            # Windows
            arch = "Win64" if sys.maxsize == (1 << 63) - 1 else "Win32"
            run_or_exit(["cmake", "-G", '"Visual Studio 10 2010 ' + arch + '"',
                         '"-DCMAKE_INSTALL_PREFIX=' + install_dir + '"'])
            run_or_exit(["msbuild.exe", "ALL_BUILD.vcxproj"])
            run_or_exit(["msbuild.exe", "INSTALL.vcxproj"])
        else:
            # Unix like
            run_or_exit(["./autogen.sh", "--enable-static",
                         "--prefix=" + install_dir])
            run_or_exit(["make"])
            run_or_exit(["make", "install"])
        print("Installed libbson in: " + install_dir)
    finally:
        os.chdir("..")

install_libbson()

if sys.platform == "win32":
    LIBBSON_STATIC = "libbson/install_dir/lib/bson-static-1.0.lib"
else:
    LIBBSON_STATIC = "libbson/install_dir/lib/libbson-1.0.a"

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
            sources=["src/bsonjs.c"],
            include_dirs=["src",
                          "libbson/install_dir/include/libbson-1.0"],
            extra_objects=[LIBBSON_STATIC]
        )
    ]
)
