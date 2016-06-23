=====
Usage
=====

In Python
---------

To use the high-level functions in Python::

    from yammh3 import hash32, hash64, hash128

In Cython
---------

To use the low-level functions in Cython::

    from yammh3._yammh3 cimport mhash64, ...

Use ``yammh3.get_include`` to get the includes directory.

.. note:: Functions with ``s`` suffix return a signed integer.
