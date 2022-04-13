import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

a = 1.3
x = np.arange(-1, 1, 0.01)


def opinion(X, a):
    return ((1 - X) * np.exp(a * X) - (1 + X) * np.exp(-a * X))


_, ax = plt.subplots()

ax.set(xlim=(-1, 1), ylim=(-1, 1))
values = opinion(x, a)
zeros = np.zeros(len(x))
ax.grid()
ax.plot(x, values)
ax.plot(x, zeros)

null_points = np.zeros(3)
null_points[0] = brentq(
    lambda X: (1 - X) * np.exp(a * X) - (1 + X) * np.exp(-a * X), -1, -0.5)
null_points[1] = brentq(
    lambda X: (1 - X) * np.exp(a * X) - (1 + X) * np.exp(-a * X), -0.5, 0.5)
null_points[2] = brentq(
    lambda X: (1 - X) * np.exp(a * X) - (1 + X) * np.exp(-a * X), 0.5, 1)

idx = np.argwhere(np.diff(np.sign(values - 0))).flatten()

ax.plot(null_points, opinion(null_points, a), 'ro')
plt.show()
print(
    f"The null points are {null_points[0]}, {null_points[1]}, and {null_points[2]}"
)
