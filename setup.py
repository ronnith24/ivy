# lint as: python3
# Copyright 2021 The Ivy Authors. All Rights Reserved.
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
# limitations under the License..
# ==============================================================================
import setuptools
from pathlib import Path
from distutils.core import setup


def _strip(line):
    return line.split(" ")[0].split("#")[0].split(",")[0]


def _replace_logos_html(txt):

    # html-containing chunks
    chunks = txt.split(".. raw:: html")

    # backend logos
    backends_chunk = chunks[2]
    bc = backends_chunk.split("\n\n")
    img_str = (
        ".. image:: https://github.com/unifyai/unifyai.github.io/blob/master/img/externally_linked/logos/supported/frameworks.png?raw=true\n"  # noqa
        "   :width: 100%"
    )
    backends_chunk = "\n\n".join(bc[0:1] + [img_str] + bc[2:])

    # re-join
    return "".join(
        [
            ".. raw:: html".join(chunks[0:2]),
            backends_chunk,
            ".. raw:: html".join(chunks[2:]),
        ]
    )


def _is_html(line):
    line_squashed = line.replace(" ", "")
    if not line_squashed:
        return False
    if line_squashed[0] == "<" and line_squashed[-1] == ">":
        return True
    return False


def _is_raw_block(line):
    line_squashed = line.replace(" ", "")
    if len(line_squashed) < 11:
        return False
    if line_squashed[-11:] == "..raw::html":
        return True
    return False


def read_description(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


this_directory = Path(__file__).parent
text = read_description("README.rst")
lines = _replace_logos_html(text).split("\n")
lines = [line for line in lines if not (_is_html(line) or _is_raw_block(line))]
long_description = "\n".join(lines)


setup(
    name="ivy-core",
    version="1.1.9",
    author="Ivy Team",
    author_email="ivydl.team@gmail.com",
    description=(
        "The unified machine learning framework, enabling framework-agnostic "
        "functions, layers and libraries."
    ),
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://lets-unify.ai/ivy",
    project_urls={
        "Docs": "https://lets-unify.ai/ivy/",
        "Source": "https://github.com/unifyai/ivy",
    },
    packages=setuptools.find_packages(),
    install_requires=[
        _strip(line)
        for line in open("requirements/requirements.txt", "r", encoding="utf-8")
    ],
    classifiers=["License :: OSI Approved :: Apache Software License"],
    license="Apache 2.0",
)
