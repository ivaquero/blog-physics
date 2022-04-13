import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def SIR(t, z, coefs=(0.7, 0.2)):

    population = 10000
    β, γ = coefs
    S, I, R = z
    u = -1 * β * S * I / population
    v = β * S * I / population - γ * I
    w = γ * I

    return [u, v, w]


t_span = [0, 50]
t = np.linspace(t_span[0], t_span[1], 5000)

_, axes = plt.subplots(1, 3, constrained_layout=True)

sir_inits = [[9999, 1, 0], [9900, 100, 0], [5000, 5000, 0]]

for i, sir_init in enumerate(sir_inits):

    sol = solve_ivp(SIR, t_span, sir_init, dense_output=True)
    X = sol.sol(t).T
    S, I, R = X[:, 0], X[:, 1], X[:, 2]
    axes[i].plot(t, S, label='S')
    axes[i].plot(t, I, label='I')
    axes[i].plot(t, R, label='R')
    axes[i].set(xlabel='Time (days)',
                title=f'{sir_init[0]} susceptible and {sir_init[1]} infected')
    axes[i].legend(loc='right')

axes[0].set(ylabel='Number of People')
plt.show()
