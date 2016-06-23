from yammh3._yammh3 cimport (
    mhash128, mhash128s,
    mhash128_x64, mhash128s_x64,
    mhash64, mhash64s, mhash64l, mhash64sl,
    mhash64_x64, mhash64s_x64, mhash64l_x64, mhash64sl_x64,
    mhash32, mhash32s,
)


def test_cimports(bytes s, int n):
    mhash128(s, n)
    mhash128(s, n)
    mhash128s(s, n)
    mhash128_x64(s, n)
    mhash128s_x64(s, n)
    mhash64(s, n)
    mhash64s(s, n)
    mhash64l(s, n)
    mhash64sl(s, n)
    mhash64_x64(s, n)
    mhash64s_x64(s, n)
    mhash64l_x64(s, n)
    mhash64sl_x64(s, n)
    mhash32(s, n)
    mhash32s(s, n)
