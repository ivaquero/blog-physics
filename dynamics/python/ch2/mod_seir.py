import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def SEIR(t, z, ρ):

    # constantes
    α = 0.2
    β = 0.266
    γ = 1 / 14
    population = 1000000
    S, E, I, R = z
    # Differential equations
    u = -ρ * β * S * I / population
    v = ρ * β * S * I / population - α * E
    w = α * E - γ * I
    l = γ * I

    return [u, v, w, l]


ρs = [1, 0.6, 0.4]
seir_inits = [[999999, 0, 1, 0], [999999, 0, 1, 0], [999999, 0, 1, 0]]
t_span = [0, 800]
t = np.linspace(t_span[0], t_span[1], 5000)

_, ax = plt.subplots()

for seir_init, ρ in zip(seir_inits, ρs):
    sol = solve_ivp(lambda t, z: SEIR(t, z, ρ),
                    t_span,
                    seir_init,
                    dense_output=True)
    X = sol.sol(t).T
    S, I, E, R = X[:, 0], X[:, 1], X[:, 2], X[:, 3]

    ax.plot(t, I, label=f'ϱ = {ρ}')

ax.legend()
ax.set(xlabel='Time (days)',
       ylabel='Number',
       title='Number of Infection by Function of Time')

plt.show()
