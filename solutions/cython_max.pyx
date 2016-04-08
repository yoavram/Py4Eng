def cmax(double[:] arr, int size):
    cdef int i
    cdef double m
    m = 0
    for i in range(size):
        if arr[i] > m:
            m = arr[i]
    return m