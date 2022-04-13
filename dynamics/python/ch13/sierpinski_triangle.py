from random import *
import numpy as np
import matplotlib.pyplot as plt
import numba


@numba.jit
def midpoint(P, Q):
    return (0.5 * (P[0] + Q[0]), 0.5 * (P[1] + Q[1]))


# The three vertices.
vertices = [(0, 0), (2, 2 * np.sqrt(3)), (4, 0)]

iterates = 50000
x, y = [0] * iterates, [0] * iterates
x[0], y[0] = random(), random()

for i in range(1, iterates):
    k = randint(0, 2)
    x[i], y[i] = midpoint(vertices[k], (x[i - 1], y[i - 1]))

_, ax = plt.subplots(dpi=100)

ax.plot(x, y, 'r.', ms=1)
ax.axis('off')
plt.show()
