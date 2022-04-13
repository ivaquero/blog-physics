import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

α, β, ω, γ = 1, -1, 1.25, 0.5
k = 0.3


def duffing(t, z):
    x, y = z
    return [y, -k * y - β * x - α * x**3 + γ * np.cos(ω * t)]


n_period = (4 * np.pi) / ω
t_span = [0, n_period]
z = [1, 0]
t = np.linspace(t_span[0], t_span[1], 200)

rs_up, rs_down = [], []
n_steps, step = 4002, 0.0001
γ_max = n_steps * step
ns = np.linspace(0, n_steps, n_steps)

# Ramp the amplitude of vibration, γ, up.
for n in ns:
    γ = step * n
    sol = solve_ivp(duffing, t_span, z, dense_output=True)
    X1 = sol.sol(t).T

    for i in range(2):
        z[0] = X1[100, 0]
        z[1] = X1[100, 1]
        r = np.sqrt(z[0]**2 + z[1]**2)
        rs_up.append([n, r])

# Ramp the amplitude of vibration, γ, down.
for n in ns:
    γ = γ_max - step * n
    sol = solve_ivp(duffing, t_span, z, dense_output=True)
    X2 = sol.sol(t).T

    for i in range(2):
        z[0] = X2[100, 0]
        z[1] = X2[100, 1]
        r = np.sqrt(z[0]**2 + z[1]**2)
        rs_down.append([n_steps - n, r])

rs_up = np.array(rs_up)
rs_down = np.array(rs_down)

_, ax = plt.subplots(dpi=100)

ax.plot(rs_up[:, 0], rs_up[:, 1], 'r.', ms=2, label='ramp up')
ax.plot(rs_down[:, 0], rs_down[:, 1], 'b.', ms=2, label='ramp down')

xtick_labels = np.linspace(0, γ_max, 5)
ax.set(xlabel=r'$γ$',
       ylabel='r',
       xticks=[x / γ_max * n_steps for x in xtick_labels],
       xticklabels=[f'{xtick}' for xtick in xtick_labels])

ax.legend()
plt.show()
