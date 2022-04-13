import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import os


def duffing(t, x):
    return [x[1], ϵ * x[0]**3 - x[0]]


ϵ = 0.01
x0 = [1, 0]
t_span = [0, 100]

sol = solve_ivp(duffing, t_span, x0, dense_output=True)

t = np.linspace(t_span[0], t_span[1], 2000)
X = sol.sol(t).T[:, 0]

_, ax = plt.subplots()

x_perturb = np.cos(t)
ax.plot(t, X - x_perturb)
ax.set(xlabel='t', ylabel='$x_N-x_0$')
plt.show()
