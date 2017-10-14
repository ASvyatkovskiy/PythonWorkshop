cimport cython
import numpy as np
cimport numpy as np

DTYPE = np.float
ctypedef np.float_t DTYPE_t

@cython.boundscheck(False) # Will not check indexing, so ensure indices are valid and non-negative
@cython.wraparound(False) # Will not allow negative indexing
@cython.cdivision(True) # Will not check for division by zero
def dot_product(np.ndarray[DTYPE_t, ndim=1] vec1, np.ndarray[DTYPE_t, ndim=1] vec2):
    cdef float result = 0.0
    cdef unsigned int i
    cdef unsigned int n = vec1.shape[0]

    for i in range(n):
        result += vec1[i]*vec2[i]

    return result
