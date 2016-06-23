#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import os

from pkgutil import walk_packages
from setuptools import setup
from setuptools.extension import Extension
from setuptools.command.build_ext import build_ext as _build_ext


class build_ext(_build_ext):

    def finalize_options(self):
        from Cython.Build import cythonize
        self.distribution.ext_modules[:] = cythonize(
            self.distribution.ext_modules,
            compiler_directives={'embedsignature': True},
        )
        _build_ext.finalize_options(self)


def find_extensions(dir, pattern, **kwargs):
    for pkgname in find_packages(dir):
        pkgdir = os.path.join(dir, pkgname.replace('.', '/'))
        for path in glob.glob(os.path.join(pkgdir, pattern)):
            modname, _ = os.path.splitext(os.path.basename(path))
            extname = '%s.%s' % (pkgname, modname)
            yield Extension(extname, [path], **kwargs)


def find_packages(path):
    # This method returns packages and subpackages as well.
    for _, name, is_pkg in walk_packages([path]):
        if is_pkg:
            yield name


def read_file(filename):
    with open(filename) as fp:
        return fp.read()


setup(
    name='yammh3',
    version='0.1.1',
    description="CPython/Cython Murmurhash3 bindings.",
    long_description=read_file('README.rst') + '\n\n' + read_file('HISTORY.rst'),
    author="Rolando Espinoza",
    author_email='rolando at rmax.io',
    url='https://github.com/rolando/yammh3',
    packages=list(find_packages('src')),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'six>=1.5.2',
    ],
    license="MIT",
    zip_safe=False,
    keywords='yammh3',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    ext_modules=list(find_extensions('src', '*.pyx', **dict(
        include_dirs=['src/yammh3/'],
    ))),
    cmdclass={'build_ext': build_ext},
    setup_requires=[
        'cython>=0.24',
    ],
)
