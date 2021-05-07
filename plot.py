# plot pixel image
#   input: a n x m np.ndarray of single value
#   output: image

from colour import Color
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from utils import timeLog

from settings import DISPLAY_TYPE


class Plot():
    def __init__(self, start_col="white", end_col="darkorange"):
        self.start_color = Color(start_col)
        self.end_color = Color(end_col)

    # generate a RGB list of gradient colors
    def __generateGradientColors(self, gradient_num) -> list:
        return np.array(
            list(map(lambda x: x.rgb,
                     list(self.start_color.
                          range_to(self.end_color, gradient_num)))))

    # fractal is a n x m np.ndarray of single value
    @timeLog
    def plotImage(self, fractal: np.ndarray):

        colors = self.__generateGradientColors(
            fractal.max() - fractal.min() + 1)

        image = colors[fractal - fractal.min()]

        if DISPLAY_TYPE == 0:
            # cv2 uses BGR
            image = np.array(list(
                map(lambda x: np.array([x[:, 2], x[:, 1], x[:, 0]]).T,
                    image)))
            cv.namedWindow("image", cv.WINDOW_NORMAL)
            cv.imshow("image", image)
            cv.waitKey(0)
            cv.destroyAllWindows()
        elif DISPLAY_TYPE == 1:
            # matplotlib uses RGB
            plt.imshow(image)
            plt.show()


# # test
# plot = Plot()
# w = np.random.randint(0, 3, [10, 10])
# plot.plotImage(w)
