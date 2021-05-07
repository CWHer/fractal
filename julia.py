# generate Mandelbrot fractal

import numpy as np
from utils import pixels2coordinates, timeLog

from settings import IMAGE_HEIGHT, IMAGE_WIDTH

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


# # test
# f = JuliaFractal()
# f.generateFractal()
# print(f.fractal)