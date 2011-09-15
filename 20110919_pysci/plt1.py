import numpy as np
import pylab
arr = np.arange(101,
    dtype='float64')
val = np.random_sample(
    arr.shape)
pylab.plot(arr, val)
pylab.xlabel('time (sec)')
pylab.ylabel('value')
pylab.show()
