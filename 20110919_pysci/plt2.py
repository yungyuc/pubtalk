import numpy as np
import pylab
x = np.arange(51,
    dtype='float64'
    )/50*2*np.pi
y = np.sin(x)
f, ax = pylab.subplots(2,
    sharex=True)
ax[0].plot(x, y)
ax[0].set_title(
    'Sharing X axis')
ax[1].scatter(x, y)
pylab.show()
