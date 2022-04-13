import numpy as np
from numpy.linalg import *
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def lotka_volterra(t, z, coefs):
    x, y = z
    a, b, c, d = coefs
    return [a * x - b * x * y, -c * y + d * x * y]


coefs = [1, 0.7, 0.35, 1]
a, b, c, d = coefs
t_span = [0, 200]
X0 = [10, 5]
sol = solve_ivp(lotka_volterra, t_span, X0, args=([coefs]), dense_output=True)

t = np.linspace(t_span[0], t_span[1], 1000)
z = sol.sol(t)

_, ax = plt.subplots()

ax.plot(t, z.T)
ax.set(xlabel='Time', ylabel='Population', xlim=(t_span[0], t_span[1]))
ax.grid()
ax.legend(['Preys', 'Predators'])

plt.show()
