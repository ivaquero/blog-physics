import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def lorenz(t, X, σ, β, ρ):
    x, y, z = X
    dx = -σ * (x - y)
    dy = ρ * x - y - x * z
    dz = -β * z + x * y
    return (dx, dy, dz)


σ, β, ρ = 10, 2.667, 28
xyz_init = 0, 1, 1.05
t_span = [0, 100]

# Integrate the lorenz equations on the time grid t.
sol = solve_ivp(lorenz, t_span, xyz_init, args=(σ, β, ρ), dense_output=True)

t = np.linspace(t_span[0], t_span[1], 10000)
x, y, z = sol.sol(t)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot(x, y, z, 'b-', lw=0.5)
ax.set(xlabel='x', ylabel='y', zlabel='z', title='Lorenz Attractor')
plt.show()
