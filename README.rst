================================
Yet Another Murmurhash3 Bindings
================================

.. image:: https://img.shields.io/pypi/v/yammh3.svg
        :target: https://pypi.python.org/pypi/yammh3

.. image:: https://img.shields.io/travis/rolando/yammh3.svg
        :target: https://travis-ci.org/rolando/yammh3

.. image:: https://readthedocs.org/projects/yammh3/badge/?version=latest
        :target: https://readthedocs.org/projects/yammh3/?badge=latest
        :alt: Documentation Status


CPython/Cython Murmurhash3 bindings.

* Free software: MIT license
* Documentation: https://yammh3.readthedocs.org.

Features
--------

* Provides a high-level Python API.
* Provides a low-level Cython bindings.
* Python 2 and 3 support.

Example
-------

Here is an example in Python:

.. code:: python

  from yammh3 import hash64

  key = b"yammh3!"

  # hash* functions return a signed integer by default.
  print("signed 64 bits hash is %s" % hash64(key))  # -> -1339990020854215562
  print("unsigned 64 bits hash is %s" % hash64(key, signed=False))  # -> 17106754052855336054L


In Cython, first we need to write a ``.pyx`` file with our code:

.. code:: cython

    # file: yammh3_example.pyx
    # mhash* functions are only available via cimport.
    from yammh3._yammh3 cimport mhash64, mhash64s
    from yammh3._yammh3 cimport int64_t, uint64_t, uint32_t

    def print_hashes(bytes key):
        cdef uint64_t h1
        cdef int64_t h2
        cdef uint32_t n = len(key)
        cdef char *c_key = <char *>key

        with nogil:  # releasing the GIL!
            h1 = mhash64(c_key, n)
            h2 = mhash64s(c_key, n)

        print("unsigned 64 bits hash is %d" % h1)
        print("signed 64 bits hash is %d" % h2)


We need to compile it as a module, usually by using a setup script:

.. code:: python

    # file: setup.py
    from setuptools import setup
    from setuptools.extension import Extension
    from Cython.Build import cythonize

    import yammh3  # already installed

    setup(
        name='yammh3-example',
        version='0.1.0',
        ext_modules=cythonize([
            Extension('*', ['*.pyx'], include_dirs=[yammh3.get_include()]),
        ])
    )


Then we build the modules in-place:

.. code::

    $ python setup.py build_ext --inplace
    Running build_ext
    building 'yammh3_example' extension
    ... [snip] ...
    copying build/lib.macosx-10.5-x86_64-2.7/yammh3_example.so ->


Now we are ready to run our code:

.. code::

    $ python -c 'import yammh3_example; yammh3_example.print_hashes(b"yammh3!")'
    unsigned 64 bits hash is 17106754052855336054
    signed 64 bits hash is -1339990020854215562


Credits
---------

Murmurhash3 was originally created by `Austin Appleby`_.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`Austin Appleby`: https://github.com/aappleby/smhasher
