from fractals import MandelbrotFractal, JuliaFractal, SierpinskiFractal
from plot import Plot

# f = MandelbrotFractal()
# f.generateFractal()
# plot = Plot("black", "white")
# plot.plotImage(f.fractal)

f = JuliaFractal()
f.generateFractal(complex(0.34, -0.05))
plot = Plot()
plot.plotImage(f.fractal)

# f = SierpinskiFractal()
# f.generateFractal()
# plot = Plot("white", "black")
# plot.plotImage(f.fractal)
