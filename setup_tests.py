#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from setuptools import setup
from setuptools.extension import Extension

from Cython.Build import cythonize

import yammh3


def get_extensions():
    kwargs = {
        'include_dirs': [yammh3.get_include()],
    }
    return cythonize([
        Extension('tests._test_cimports', ['tests/_test_cimports.pyx'], **kwargs),
    ])


setup(
    name='yammh3-tests',
    version='0.1.2',
    packages=['tests'],
    package_data={
        "tests": ['*.pyx', '*.pxd'],
    },
    ext_modules=get_extensions(),
)
