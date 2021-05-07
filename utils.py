import time
from functools import wraps

from settings import IMAGE_HEIGHT, IMAGE_WIDTH


def pixels2coordinates(r, c, x_range, y_range):
    x = c * x_range / IMAGE_WIDTH - x_range / 2
    y = r * y_range / IMAGE_HEIGHT - y_range / 2
    return (x, y)


# display used time
def timeLog(func):
    @wraps(func)
    def clocked(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print("{} finishes after {:.2f} s".format(func.__name__,
                                                  time.time() - start))
        return ret

    return clocked
