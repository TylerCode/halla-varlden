# Will run the famous "Conway's Game of Life"
# Tested under Python 2.7.9

import numpy as numpy
import matplotlib.pyplot as pyplot
import matplotlib.animation as animation

x = numpy.array([[0,0,255], [255,255,0], [0,255,0]])
pyplot.imshow(x, interpolation='nearest')
pyplot.show()