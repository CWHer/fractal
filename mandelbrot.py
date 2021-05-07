# generate Mandelbrot fractal

import numpy as np
from utils import pixels2coordinates, timeLog

from settings import IMAGE_HEIGHT, IMAGE_WIDTH

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


# test
# f = MandelbrotFractal()
# f.generateFractal()
# print(f.fractal)