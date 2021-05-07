from mandelbrot import MandelbrotFractal
from plot import Plot

f = MandelbrotFractal()
f.generateFractal()
plot = Plot("black", "white")
plot.plotImage(f.fractal)
