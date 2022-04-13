import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols
from sympy.solvers import solve
from matplotlib import colors


def number_track(rs, ks, n_points):
    X = symbols('X', real=True)
    item = np.zeros(n_points)
    equilibria = np.zeros(n_points)
    for r in range(n_points):
        for k in range(n_points):
            r_i, k_i = rs[r], k_i[k]
            item[k] = len(solve(rs[r] * (1 - X / k_i) - X / (1 + X**2), X)) + 1
        matrix.append(item)
        item = np.zeros(n_points)
    return matrix


n_points = 20
r_range = [0, 0.6]
k_range = [0, 40]
rs = np.linspace(r_range[0], r_range[1], n_points)
ks = np.linspace(k_range[0], k_range[1], n_points)

matrix = []

cmap = colors.ListedColormap(['red', 'orange'])
bounds = [1, 2, 3]
extent = [0, 40, 0, 0.6]
norm = colors.BoundaryNorm(bounds, cmap.N)

matrix = number_track(rs, ks, n_points)

_, ax = plt.subplots()

image = ax.imshow(matrix,
                  interpolation='nearest',
                  origin='lower',
                  cmap=cmap,
                  norm=norm,
                  extent=extent,
                  aspect='auto')

plt.colorbar(image, boundaries=bounds, ticks=[1, 2, 3])
plt.show()
