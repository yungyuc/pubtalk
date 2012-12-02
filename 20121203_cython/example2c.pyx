import numpy as np
cimport numpy as cnp
cdef extern:
    void caction(double* arr0, double* arr1)
def action():
    cdef cnp.ndarray[double, ndim=2] arr0 = np.empty(
        [1000,1000], dtype='float64')
    arr0.fill(0)
    cdef cnp.ndarray[double, ndim=2] arr1 = np.empty(
        [1000,1000], dtype='float64')
    arr1.fill(1)
    caction(&arr0[0,0], &arr1[0,0])
    assert 7968032 == arr0.sum()
