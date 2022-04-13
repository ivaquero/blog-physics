import numpy as np
from numpy.linalg import *
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def derivatives(t, z):
    x, y = z
    return [-y - x * np.sqrt(x**2 + y**2), x - y * np.sqrt(x**2 + y**2)]


t_span = [0, 16 * np.pi]
z = [1, 0]
sol = solve_ivp(derivatives, t_span, z, dense_output=True)

t = np.linspace(t_span[0], t_span[1], 10000)
X = sol.sol(t).T

_, ax = plt.subplots()

ax.plot(X[:, 0], X[:, 1], 'r-')
ax.set(xlabel='x', ylabel='y', xlim=(-.5, 1.5), ylim=(-.5, .5))

plt.show()
