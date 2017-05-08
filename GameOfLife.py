# Will run the famous "Conway's Game of Life"
# Tested under Python 2.7.9

import sys, argparse
import numpy as numpy
import matplotlib.pyplot as pyplot
import matplotlib.animation as animation

ON = 255
OFF = 0
values = [ON, OFF]

def randomStart(N):
    return numpy.random.choice(values, N*N, p=[0.3, 0.7]).reshape(N,N)

def addGlider(i,j,grid):
    # Adds glider to top left cell
    glider = numpy.array([[0,0,255], [255,0,255], [0,255,255]])
    grid[i:i+3, j:j+3] = glider


def oldCode();
    x = numpy.random.choice([0,255], 5*5, p=[0.3,0.7]).reshape(5,5)
    pyplot.imshow(x, interpolation='nearest')
    pyplot.show()



grid = np.zeros(N*N).reshape(N,N)
addGlider(1,1, grid)