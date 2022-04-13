import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

α, β, ω, γ = 1, -1, 1.25, 0.5
k = 0.3


def duffing(t, z):
    x, y = z
    return [y, -k * y - β * x - α * x**3 + γ * np.cos(ω * t)]


def plot_phase(func, t_span, z, ax):

    sol = solve_ivp(func, t_span, z, dense_output=True)
    t = np.linspace(t_span[0], t_span[1], t_span[1] * 10)
    X1 = sol.sol(t).T

    ax.plot(X1[:, 0], X1[:, 1], 'r-', lw=0.2)
    ax.set(xlabel='x', ylabel='y', title='Phase portrait')


def plot_poincare(func, t_span, z, n_period, ax):

    sol = solve_ivp(func, t_span, z, dense_output=True)
    t = np.linspace(t_span[0], t_span[1] * n_period, t_span[1]**2)
    X2 = sol.sol(t).T

    x = [X2[t_span[1] * i, 0] for i in range(t_span[1])]
    y = [X2[t_span[1] * i, 1] for i in range(t_span[1])]

    ax.plot(x, y, 'b.', ms=2)
    ax.set(xlabel='x', ylabel='y', title='Poincaré section')


z = [1, 0]
t_span = [0, 1000]
n_period = (2 * np.pi) / ω

_, axes = plt.subplots(1, 2, constrained_layout=True)

plot_phase(func=duffing, t_span=t_span, z=z, ax=axes[0])
plot_poincare(func=duffing, t_span=t_span, z=z, n_period=n_period, ax=axes[1])
plt.show()
