import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def lotka_volterra(t, X):
    u = 0.05 * X * (1 - X / 100)
    return u


x_inits = [1, 50, 200]
t_span = [0, 200]
t = np.linspace(t_span[0], t_span[1], 1000)

_, ax = plt.subplots()

for x_init in x_inits:
    sol = solve_ivp(lotka_volterra, t_span, [x_init], dense_output=True)
    X = sol.sol(t).T
    ax.plot(t, X, label=f'X = {x_init}')

ax.legend()
ax.set(xlabel='Time', ylabel='X', title='The Logistics Equation')

plt.show()
