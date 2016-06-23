from libc.stdint cimport uint32_t, int32_t, uint64_t, int64_t
from libc.string cimport const_char


cdef extern from "include/MurmurHash3.h" nogil:
    void MurmurHash3_x86_32(const void *key, int len, uint32_t seed, void *out)
    void MurmurHash3_x86_128(const void *key, int len, uint32_t seed, void *out)
    void MurmurHash3_x64_128(const void *key, int len, uint32_t seed, void *out)


# Unsigned 128 bits representation as a pair of 64 bits unsigned integers.
cdef struct uint64x2_t:
    uint64_t high
    uint64_t low


# Signed 128 bits representation as a pair of 64 bits signed integers.
cdef struct int64x2_t:
    int64_t high
    int64_t low


cpdef uint64x2_t mhash128(const_char *key, size_t length, uint32_t seed=*) nogil
cpdef int64x2_t mhash128s(const_char *key, size_t length, uint32_t seed=*) nogil
cpdef uint64x2_t mhash128_x64(const_char *key, size_t length, uint32_t seed=*) nogil
cpdef int64x2_t mhash128s_x64(const_char *key, size_t length, uint32_t seed=*) nogil

cpdef uint64_t mhash64(const_char *key, size_t length, uint32_t seed=*) nogil
cpdef uint64_t mhash64l(const_char *key, size_t length, uint32_t seed=*) nogil
cpdef int64_t mhash64s(const_char *key, size_t length, uint32_t seed=*) nogil
cpdef int64_t mhash64sl(const_char *key, size_t length, uint32_t seed=*) nogil
cpdef uint64_t mhash64_x64(const_char *key, size_t length, uint32_t seed=*) nogil
cpdef uint64_t mhash64l_x64(const_char *key, size_t length, uint32_t seed=*) nogil
cpdef int64_t mhash64s_x64(const_char *key, size_t length, uint32_t seed=*) nogil
cpdef int64_t mhash64sl_x64(const_char *key, size_t length, uint32_t seed=*) nogil

cpdef uint32_t mhash32(const_char *key, size_t length, uint32_t seed=*) nogil
cpdef int32_t mhash32s(const_char *key, size_t length, uint32_t seed=*) nogil
