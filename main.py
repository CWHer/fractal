from mandelbrot import MandelbrotFractal
from julia import JuliaFractal
from plot import Plot

# f = MandelbrotFractal()
# f.generateFractal()
# plot = Plot("black", "white")
# plot.plotImage(f.fractal)

f = JuliaFractal()
f.generateFractal(complex(0.34, -0.05))
plot = Plot()
plot.plotImage(f.fractal)
