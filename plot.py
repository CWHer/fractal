# plot pixel image
#   input: a n x m np.ndarray of single value
#   output: image

from colour import Color
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

from settings import DISPLAY_TYPE


class Plot():
    def __init__(self):
        self.gradient_num = 0
        self.start_color = Color("white")
        self.end_color = Color("orange")

    # generate a RGB list of gradient colors
    def __generateGradientColors(self) -> list:
        return np.array(
            list(map(lambda x: x.rgb,
                     list(self.start_color.
                          range_to(self.end_color, self.gradient_num)))))

    # w is a n x m np.ndarray of single value
    def plotImage(self, w: np.ndarray):

        self.gradient_num = w.max() - w.min() + 1
        colors = self.__generateGradientColors()

        image = colors[w - w.min()]

        if DISPLAY_TYPE == 0:
            cv.imshow('image', image)
            cv.waitKey(0)
            cv.destroyAllWindows()
        elif DISPLAY_TYPE == 1:
            plt.imshow(image)
            plt.show()


# # test
# plot = Plot()
# w = np.random.randint(0, 2, [600, 800])
# print(w)
# plot.plotImage(w)
