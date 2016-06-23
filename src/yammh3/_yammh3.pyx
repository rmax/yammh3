# distutils: language = c++
# distutils: sources = src/yammh3/include/MurmurHash3.cpp


#
# 128 bits hash functions.
#
cpdef inline uint64x2_t mhash128(const_char *key, size_t length, uint32_t seed=0) nogil:
    """A MurmurHash3_x86_128 wrapper.
    """
    cdef uint64x2_t out
    MurmurHash3_x86_128(key, length, seed, &out)
    return out


cpdef inline int64x2_t mhash128s(const_char *key, size_t length, uint32_t seed=0) nogil:
    """A MurmurHash3_x86_128 signed wrapper."""
    cdef int64x2_t out
    MurmurHash3_x86_128(key, length, seed, &out)
    return out


#
# 128 bits x64 optimized hash functions.
#
cpdef inline uint64x2_t mhash128_x64(const_char *key, size_t length, uint32_t seed=0) nogil:
    """A MurmurHash3_x64_128 wrapper."""
    cdef uint64x2_t out
    MurmurHash3_x64_128(key, length, seed, &out)
    return out


cpdef inline int64x2_t mhash128s_x64(const_char *key, size_t length, uint32_t seed=0) nogil:
    """A MurmurHash3_x64_128 signed wrapper."""
    cdef int64x2_t out
    MurmurHash3_x64_128(key, length, seed, &out)
    return out


#
# 64 bits hash functions.
#
cpdef inline uint64_t mhash64(const_char *key, size_t length, uint32_t seed=0) nogil:
    """A MurmurHash3_x86_128 wrapper. Returns high 64 bits."""
    cdef uint64x2_t out
    MurmurHash3_x86_128(key, length, seed, &out)
    return out.high


cpdef inline uint64_t mhash64l(const_char *key, size_t length, uint32_t seed=0) nogil:
    """A MurmurHash3_x86_128 wrapper. Returns low 64 bits."""
    cdef uint64x2_t out
    MurmurHash3_x86_128(key, length, seed, &out)
    return out.low


cpdef inline int64_t mhash64s(const_char *key, size_t length, uint32_t seed=0) nogil:
    """A MurmurHash3_x86_128 signed wrapper. Returns high 64 bits."""
    cdef int64x2_t out
    MurmurHash3_x86_128(key, length, seed, &out)
    return out.high


cpdef inline int64_t mhash64sl(const_char *key, size_t length, uint32_t seed=0) nogil:
    """A MurmurHash3_x86_128 signed wrapper. Returns low 64 bits."""
    cdef int64x2_t out
    MurmurHash3_x86_128(key, length, seed, &out)
    return out.low


#
# 64 bits x64 optimized hash functions.
#
cpdef inline uint64_t mhash64_x64(const_char *key, size_t length, uint32_t seed=0) nogil:
    """A MurmurHash3_x64_128 wrapper. Returns high 64 bits."""
    cdef uint64x2_t out
    MurmurHash3_x64_128(key, length, seed, &out)
    return out.high


cpdef inline uint64_t mhash64l_x64(const_char *key, size_t length, uint32_t seed=0) nogil:
    """A MurmurHash3_x64_128 wrapper. Returns low 64 bits."""
    cdef uint64x2_t out
    MurmurHash3_x64_128(key, length, seed, &out)
    return out.low


cpdef inline int64_t mhash64s_x64(const_char *key, size_t length, uint32_t seed=0) nogil:
    """A MurmurHash3_x64_128 wrapper. Returns high 64 bits."""
    cdef int64x2_t out
    MurmurHash3_x64_128(key, length, seed, &out)
    return out.high


cpdef inline int64_t mhash64sl_x64(const_char *key, size_t length, uint32_t seed=0) nogil:
    """A MurmurHash3_x64_128 wrapper. Returns low 64 bits."""
    cdef int64x2_t out
    MurmurHash3_x64_128(key, length, seed, &out)
    return out.low


#
# 32 bit hash functions.
#
cpdef inline uint32_t mhash32(const_char *key, size_t length, uint32_t seed=0) nogil:
    """A MurmurHash3_x86_32 wrapper."""
    cdef uint32_t out
    MurmurHash3_x86_32(key, length, seed, &out)
    return out


cpdef inline int32_t mhash32s(const_char *key, size_t length, uint32_t seed=0) nogil:
    """A MurmurHash3_x86_32 signed wrapper."""
    cdef int32_t out
    MurmurHash3_x86_32(key, length, seed, &out)
    return out
