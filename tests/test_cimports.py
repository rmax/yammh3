from hypothesis import given, strategies as st

from ._test_cimports import test_cimports as _test_cimports


@given(st.text())
def test_cimports(value):
    b_value = value.encode('utf-8')
    _test_cimports(b_value, len(b_value))
