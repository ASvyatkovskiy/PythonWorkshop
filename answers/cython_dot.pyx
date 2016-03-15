cimport cython
#import numpy as np
#cimport numpy as np

#DTYPE = np.float64
#ctypedef np.float64_t DTYPE_t

@cython.boundscheck(False) # Will not check indexing, so ensure indices are valid and non-negative
@cython.wraparound(False) # Will not allow negative indexing
@cython.cdivision(True) # Will not check for division by zero
#def _extract(np.ndarray[DTYPE2_t, ndim=2] ft, np.ndarray[DTYPE_t, ndim=3] ii,
#                   np.ndarray[DTYPE_t, ndim=2] features, int pad, int fraction):
#    cdef unsigned int row, col, t, pixel_counter
#    cdef unsigned int ncols, row0, col0

def dot_product(vec1,vec2):
    cdef float result = 0.0
    cdef unsigned int i
    cdef unsigned int n = len(vec1)

    for i in range(n):
        result += vec1[i]*vec2[i]

    return result
