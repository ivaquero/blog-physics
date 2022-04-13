import numpy as np
import matplotlib.pyplot as plt


def complex_set(num_iter, n_points, X0, fractal="Mandelbrot"):
    X = np.linspace(X0[0], X0[1], n_points)
    Y = np.linspace(X0[2], X0[3], n_points)
    [x, y] = np.meshgrid(X, Y * 1j)
    z = x + y
    C = x + y
    Q = np.zeros([n_points, n_points])

    for j in range(num_iter):
        index = np.abs(z) < np.inf
        Q[index] = Q[index] + 1
        if fractal == "Julia":
            z = z**2 + -0.835 - 0.2321 * 1j
        elif fractal == "Mandelbrot":
            z = z**2 + C
    return X, Y, Q


num_iter = 50
n_points = 1000
X0 = [-2, 2, -2, 2]

X, Y, Q = complex_set(num_iter, n_points, X0, "Mandelbrot")

_, ax = plt.subplots(dpi=100)
ax.pcolormesh(X, Y, Q, cmap="Greys")
ax.axis('equal')
plt.show()
