#!/usr/bin/env python

from setuptools import setup

setup(
    name="python-pushover",
    version="1.1",
    description="Comprehensive bindings and command line utility for the "
    "Pushover notification service",
    long_description=open("README.rst").read()
    + "\n"
    + open("AUTHORS.rst").read()
    + "\n"
    + open("CHANGES.rst").read(),
    url="https://github.com/almir1904/python-pushover",
    packages=["pushover"],
    entry_points={"console_scripts": ["pushover = pushover.cli:main"]},
    install_requires=["requests>=1.0"],
    license="GNU GPLv3",
)
