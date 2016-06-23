#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_yammh3
----------------------------------

Tests for `yammh3` module.
"""
import functools
import glob
import os
import pytest

from hypothesis import given, strategies as st
from yammh3 import get_include, hash128, hash64, hash32


def partial(func, **default_kwargs):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        kwargs = dict(default_kwargs, **kwargs)
        return func(*args, **kwargs)
    wrapper.default_kwargs = default_kwargs
    return wrapper


st_custom_seed = functools.partial(st.integers, 1, 2**32-1)

booleans = [False, True]

hash_funcs_defaults = [
    hash32, hash64, hash128,
]

hash_funcs_signed = [
    partial(hash32, signed=True),
] + [
    partial(hash64, signed=True, low=low, x64=x64)
    for low in booleans for x64 in booleans
] + [
    partial(hash128, signed=True, x64=True),
    partial(hash128, signed=True, x64=False),
]

hash_funcs_unsigned = [
    partial(hash32, signed=False),
] + [
    partial(hash64, signed=False, low=low, x64=x64)
    for low in booleans for x64 in booleans
] + [
    partial(hash128, signed=False, x64=True),
    partial(hash128, signed=False, x64=False),
]


hash_funcs_all = hash_funcs_signed + hash_funcs_unsigned


def is_hash128_out(out):
    return isinstance(out, tuple) and len(out) == 2


def assert_uint32(n):
    assert 0 <= n < 2**32


def assert_int32(n):
    assert -2**31 <= n < 2**31


def assert_uint64(n):
    assert 0 <= n < 2**64


def assert_int64(n):
    assert -2**63 <= n < 2**63


def assert_uint128(n):
    assert is_hash128_out(n)
    a, b = n
    assert_uint64(a)
    assert_uint64(b)


def assert_int128(n):
    assert is_hash128_out(n)
    a, b = n
    assert_int64(a)
    assert_int64(b)


def test_get_include():
    path = get_include()
    headers = glob.glob(os.path.join(path, '*.pxd'))
    assert len(headers) > 0


@pytest.mark.parametrize('hash_func', hash_funcs_defaults)
@given(value=st.text(), seed=st_custom_seed())
def test_hash_default_signed(hash_func, value, seed):
    out = hash_func(value, seed=seed)
    out_signed = hash_func(value, signed=True, seed=seed)
    assert out == out_signed


@pytest.mark.parametrize('hash_func', hash_funcs_all)
@given(value=st.text(), seed=st_custom_seed())
def test_hash_bytes(hash_func, value, seed):
    out_default = hash_func(value.encode('utf8'))
    out = hash_func(value, seed=seed)
    assert out != out_default


@pytest.mark.parametrize('hash_func', hash_funcs_all)
@given(value=st.text(), seed=st_custom_seed())
def test_hash_custom_seed(hash_func, value, seed):
    out_default = hash_func(value)
    out = hash_func(value, seed=seed)
    assert out != out_default


@pytest.mark.parametrize('hash_func', hash_funcs_unsigned)
@given(value=st.text(), seed=st_custom_seed())
def test_hash_unsigned(hash_func, value, seed):
    out = hash_func(value, seed=seed)
    if is_hash128_out(out):
        assert out[0] >= 0 and out[1] >= 0
    else:
        assert out >= 0


@pytest.mark.parametrize('hash_func', hash_funcs_signed)
def test_hash_signed(hash_func):
    # As we test random values, we stop once we find one negative.
    @given(value=st.text(min_size=1), seed=st_custom_seed())
    def find_negative(value, seed):
        out = hash_func(value, seed=seed)
        if is_hash128_out(out):
            out = min(*out)
        if out < 0:
            raise FoundNegative

    try:
        find_negative()
    except FoundNegative:
        pass
    else:
        assert False, "Unable to find negative hash"


@pytest.mark.parametrize('hash_assert', [
    (hash32, [assert_uint32, assert_int32]),
    (hash64, [assert_uint64, assert_int64]),
    (hash128, [assert_uint128, assert_int128]),
])
@given(value=st.text(), seed=st_custom_seed())
def test_hash_int_ranges(hash_assert, value, seed):
    hash_func, (assert_u, assert_s) = hash_assert
    assert_s(hash_func(value, seed=seed))  # default signed
    assert_u(hash_func(value, seed=seed, signed=False))


@pytest.mark.parametrize('x64', booleans)
@given(value=st.text(), seed=st_custom_seed())
def test_hash64_is_hash128(x64, value, seed):
    high = hash64(value, seed=seed, x64=x64)  # default low=False
    low = hash64(value, seed=seed, low=True, x64=x64)
    out = hash128(value, seed=seed, x64=x64)
    assert (high, low) == out


class FoundNegative(Exception):
    pass
