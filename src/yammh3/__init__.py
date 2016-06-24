# -*- coding: utf-8 -*-
import six

from ._yammh3 import (
    mhash128, mhash128s,
    mhash128_x64, mhash128s_x64,
    mhash64, mhash64s, mhash64l, mhash64sl,
    mhash64_x64, mhash64s_x64, mhash64l_x64, mhash64sl_x64,
    mhash32, mhash32s,
)


__author__ = 'Rolando Espinoza'
__email__ = 'rolando at rmax.io'
__version__ = '0.1.2'

__all__ = ['get_include', 'hash128', 'hash64', 'hash32']


def get_include():
    """Returns the includes directory.

    Returns
    -------
    out : str
        Directory that contains header files.

    """
    import os
    return os.path.abspath(os.path.dirname(__file__))


def hash128(value, seed=0, signed=True, x64=False):
    """Returns a 128 bits hash for the given value.

    Parameters
    ----------
    value : unicode or str
        Value to be hashed.
    seed : int, optional
        Seed for the hash algorithm. Default is 0.
    signed : bool, optional
        If True, returns a signed integer, otherwise returns an unsigned
        integer. Default is True.
    x64 : bool, optional
        Whether to use x64 optimized hash functions. Default is False.

    Returns
    -------
    out : tuple
        A tuple of 64 bits integers (high, low).

    """
    value = _tobytes(value)
    if x64:
        choices = (mhash128_x64, mhash128s_x64)
    else:
        choices = (mhash128, mhash128s)
    out = choices[signed](value, len(value), seed)
    return out['high'], out['low']


def hash64(value, seed=0, signed=True, low=False, x64=False):
    """Returns a 64 bits hash for the given value.

    This function uses the 128 bits hash function internally and the ``low``
    parameter controls which part of bits are returned.

    Parameters
    ----------
    value : unicode or str
        Value to be hashed.
    seed : int, optional
        Seed for the hash algorithm. Default is 0.
    signed : bool, optional
        If True, returns a signed integer, otherwise returns an unsigned
        integer. Default is True.
    low : bool, optional
        Whether to returns low bits rather than high bits. Default is False.
    x64 : bool, optional
        Whether to use x64 optimized hash functions. Default is False.

    Returns
    -------
    out : int
        A 64 bits integer.

    """
    value = _tobytes(value)
    if low:
        choices = (
            (mhash64l, mhash64sl),
            (mhash64l_x64, mhash64sl_x64),
        )[x64]
    else:
        choices = (
            (mhash64, mhash64s),
            (mhash64_x64, mhash64s_x64),
        )[x64]
    return choices[signed](value, len(value), seed)


def hash32(value, seed=0, signed=True):
    """Returns a 32 bits hash for the given value.

    Parameters
    ----------
    value : unicode or str
        Value to be hashed.
    seed : int, optional
        Seed for the hash algorithm. Default is 0.
    signed : bool, optional
        If True, returns a signed integer, otherwise returns an unsigned
        integer. Default is True.

    Returns
    -------
    out : int
        A 32 bits integer.

    """
    value = _tobytes(value)
    func = (mhash32, mhash32s)[signed]
    return func(value, len(value), seed)


def _tobytes(s, encoding='utf-8'):
    if isinstance(s, six.binary_type):
        return s
    if isinstance(s, six.text_type):
        return s.encode(encoding)
    raise ValueError("Unsupported type '%s'" % type(s))
