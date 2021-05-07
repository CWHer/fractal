# generate Sierpinski fractal

import numpy as np
from utils import timeLog


class SierpinskiFractal():
    def __init__(self):
        pass

    # generate fractal with size 3^depth
    @timeLog
    def generateFractal(self, depth=6):
        fractal_size = 3**depth
        self.fractal = np.zeros([fractal_size, fractal_size], dtype=np.int32)

        def drawFractal(left_upper, depth):
            if depth == 0: return
            left, upper = left_upper
            block_size = 3**(depth - 1)
            for r in range(3):
                for c in range(3):
                    x = left + c * block_size
                    y = upper + r * block_size
                    if r == 1 and c == 1:
                        for i in range(block_size):
                            for j in range(block_size):
                                self.fractal[y + i, x + j] = 1
                    else:
                        drawFractal((x, y), depth - 1)

        drawFractal((0, 0), depth)


# test
# f = SierpinskiFractal()
# f.generateFractal()
# print(f.fractal)