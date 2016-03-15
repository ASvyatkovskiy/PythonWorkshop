cimport cython

@cython.boundscheck(False) # Will not check indexing, so ensure indices are valid and non-negative
@cython.wraparound(False) # Will not allow negative indexing
@cython.cdivision(True) # Will not check for division by zero
def dot_product(vec1,vec2):
    cdef float result = 0.0
    cdef unsigned int i
    cdef unsigned int n = len(vec1)

    for i in range(n):
        result += vec1[i]*vec2[i]

    return result
