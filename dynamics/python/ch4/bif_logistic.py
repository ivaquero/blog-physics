import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols
from sympy.solvers import solve
from matplotlib import colors


def number_track(H, A):
    matrix = []
    X = symbols('X', real=True)
    equilibria = np.zeros(len(H))
    for h in enumerate(H):
        item = np.zeros(len(A))
        for ind, a in enumerate(A):
            item[ind] = len(solve(X * (1 - X) - h * X / (a + X), X))
        matrix.append(item)
    return matrix


# colormap
# cmap = colors.ListedColormap(['red', 'orange'])
# bounds=[1,2,3]
extent = [0, 1, 0, 1]
# norm = colors.BoundaryNorm(bounds, cmap.N)
h_vals = np.linspace(0, 1, 20)
a_vals = np.linspace(0, 1, 20)
matrix = number_track(h_vals, a_vals)

_, ax = plt.subplots()

image = ax.imshow(matrix, extent=extent, aspect='auto')

plt.show()
