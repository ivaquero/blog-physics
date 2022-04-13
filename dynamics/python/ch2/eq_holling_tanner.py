import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def Holling_Tanner(t, z):
    x, y = z
    u = x * (1 - x / 7) - 6 / 7 * x * y / (1 + x)
    v = 0.2 * y * (1 - 0.5 * y / x)
    return [u, v]


t_span = [0, 200]
z = [7, 0.1]
sol = solve_ivp(Holling_Tanner, t_span, z, dense_output=True)

t = np.linspace(t_span[0], t_span[1], 1000)
X = sol.sol(t).T

_, axes = plt.subplots(1, 2, constrained_layout=True)

axes[0].plot(t, X[:, 0], 'r-', label='prey')
axes[0].plot(t, X[:, 1], 'b-', label='predator')
axes[0].set(xlabel="Time", title="Time Series")
axes[0].grid()
axes[0].legend()

axes[1].plot(X[:, 0], X[:, 1], color="blue")
axes[1].set(xlabel='x', ylabel='y', title='Phase Portrait')
axes[1].grid()

plt.show()
