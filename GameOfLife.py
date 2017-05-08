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


def update(frameNumber, img, grid, N):
    # Get a copy of the grid for neighbor calculation
    # Then the process of running through line-by-line
    newGrid = grid.copy()
    
    for i in range(N):
        for j in range(N):
            # Neighbor Sum calculation
            #x and y wrapping
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] + grid[(i-1)%N, j] + grid[(i+1)%N, j] + grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)

            # Now we apply conway's rules
            if grid[i, j] == ON:
                if(total < 2) or (total > 3):
                    newGrid[i,j] = OFF
            else:
                if total == 3:
                    newGrid[i,j] = ON

            img.set_data(newGrid)
            grid[:] = newGrid[:]
            return img,

# Where bananas happens
def main():
    # command line arguments
    # argv[0] can be ignored
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    
    # Adding args
    parser.add_argument('--grid-size', dest = 'N', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    args = parser.parse_args()

    N=100
    if args.N and int(args.N) > 8:
        N = int(args.N)

    updateInterval = 50
    if args.interval:
        updateInterval = args.interval

    grid = numpy.array([])
    if args.glider:
        grid = numpy.zeros(N*N).reshape(N,N)
        addGlider()
    else:
        grid = randomStart(N)

    fig, ax = pyplot.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ), frames=10, interval=updateInterval, save_count=50)

    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])

    pyplot.show()

if __name__ == '__main__':
    main()
