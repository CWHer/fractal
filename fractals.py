import numpy as np
from utils import timeLog, pixels2coordinates

from settings import IMAGE_HEIGHT, IMAGE_WIDTH


# generate Sierpinski fractal
class SierpinskiFractal():
    def __init__(self):
        pass

    # generate fractal with size 3^depth
    @timeLog
    def generateFractal(self, depth=6):
        fractal_size = 3**depth
        self.fractal = np.zeros([fractal_size, fractal_size], dtype=np.int32)

        def drawFractal(left_up, depth):
            if depth == 0: return
            left, up = left_up
            block_size = 3**(depth - 1)
            for r in range(3):
                for c in range(3):
                    x = left + c * block_size
                    y = up + r * block_size
                    if r == 1 and c == 1:
                        for i in range(block_size):
                            for j in range(block_size):
                                self.fractal[y + i, x + j] = 1
                    else:
                        drawFractal((x, y), depth - 1)

        drawFractal((0, 0), depth)


# generate Mandelbrot fractal
# f(z) = z^2 + c
# where c is current point, and z iterates from 0
class MandelbrotFractal():
    def __init__(self):
        self.x_range = 4
        self.y_range = 4 * IMAGE_HEIGHT / IMAGE_WIDTH

    # calculate escape time
    # and generate fractal
    @timeLog
    def generateFractal(self):
        max_escape_time = 50
        # n x m np.ndarray of single value
        self.fractal = np.zeros([IMAGE_HEIGHT, IMAGE_WIDTH],
                                dtype=np.int32) + max_escape_time
        for i in range(IMAGE_HEIGHT):
            for j in range(IMAGE_WIDTH):
                x, y = pixels2coordinates(i, j, self.x_range, self.y_range)

                # calculate escape time
                z = 0 + 0j
                for T in range(max_escape_time):
                    if abs(z) > 2:
                        self.fractal[i, j] = T
                        break
                    z = z * z + complex(x, y)


# generate Julia fractal
# f(z) = z^2 + c
# where z iterates from current point, and c is a constant
class JuliaFractal():
    def __init__(self):
        self.x_range = 4
        self.y_range = 4 * IMAGE_HEIGHT / IMAGE_WIDTH

    # calculate escape time
    # and generate fractal
    @timeLog
    def generateFractal(self, c=-0.52 + 0.62j):
        max_escape_time = 50
        # n x m np.ndarray of single value
        self.fractal = np.zeros([IMAGE_HEIGHT, IMAGE_WIDTH],
                                dtype=np.int32) + max_escape_time
        for i in range(IMAGE_HEIGHT):
            for j in range(IMAGE_WIDTH):
                x, y = pixels2coordinates(i, j, self.x_range, self.y_range)

                # calculate escape time
                z = complex(x, y)
                for T in range(max_escape_time):
                    if abs(z) > 2:
                        self.fractal[i, j] = T
                        break
                    z = z * z + c
