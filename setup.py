#!/usr/bin/env python3

"""
Author: Stylianos (Steve) Mavrianos
"""

from setuptools import setup, find_packages

setup(
    name="DEXTR",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    description="A forked version of DEXTR for SegmentME project. mainly changes with numpy version.",
    author="Stylianos Mavrianos",
    author_email="stylianosmavrianos@gmail.com"
)
