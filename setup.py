"""
Copyright (c) 2008-2023 synodriver <diguohuangjiajinweijun@gmail.com>
"""
# -*- coding: utf-8 -*-
import os
import re

from setuptools import find_packages, setup


def get_version() -> str:
    path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "memtrace", "__init__.py"
    )
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    result = re.findall(r"(?<=__version__ = \")\S+(?=\")", data)
    return result[0]


def get_dis():
    with open("README.markdown", "r", encoding="utf-8") as f:
        return f.read()


packages = find_packages(exclude=("test", "tests.*", "test*"))


def main():
    version: str = get_version()

    dis = get_dis()
    setup(
        name="memtrace",
        version=version,
        url="https://github.com/synodriver/memtrace",
        packages=packages,
        keywords=["debug", "memory"],
        description="Detect memory leaks at log files",
        long_description_content_type="text/markdown",
        long_description=dis,
        author="synodriver",
        author_email="diguohuangjiajinweijun@gmail.com",
        python_requires=">=3.7",
        # install_requires=["aiohttp", "aiofiles", "typing-extensions"],
        license="GPLv3",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Operating System :: OS Independent",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: Implementation :: CPython",
            "Programming Language :: Python :: Implementation :: PyPy",
        ],
        include_package_data=True,
    )


if __name__ == "__main__":
    main()
