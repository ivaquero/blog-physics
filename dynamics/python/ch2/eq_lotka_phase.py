import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def lotka_volterra(t, z, coefs):
    x, y = z
    a, b, c, d = coefs
    return [a * x - b * x * y, -c * y + d * x * y]


def generate_mesh_2d(xy_range, n_points):
    X, Y = np.meshgrid(np.linspace(xy_range[0], xy_range[1], n_points),
                       np.linspace(xy_range[2], xy_range[3], n_points))
    return X, Y


def vector_field(X, Y, U, V, ax):

    M = np.hypot(U, V)  # Norm of the growth rate
    M[M == 0] = 1  # Avoid zero division errors
    U /= M  # Normalize each vector_field
    V /= M
    ax.quiver(X, Y, U, V, M, pivot='mid', cmap=plt.cm.jet)


_, ax = plt.subplots(dpi=100)

xy_range = [0, 5, 0, 10]
n_points = 20
coefs = [1, 0.7, 0.35, 1]
a, b, c, d = coefs
# create a grid
X, Y = generate_mesh_2d(xy_range, n_points)
# compute growth rate on the grid
U, V = lotka_volterra(t=0, z=[X, Y], coefs=coefs)
vector_field(X, Y, U, V, ax)

X_R = [c / d, a / b]
t_span = [0, 50]

values = np.linspace(1, 5, 5)
vcolors = plt.cm.autumn_r(values)

for v, col in zip(values, vcolors):
    z = v * np.array(X_R)
    sol = solve_ivp(lotka_volterra,
                    t_span,
                    z,
                    args=([coefs]),
                    dense_output=True)
    t = np.linspace(t_span[0], t_span[1], 1000)
    X = sol.sol(t).T
    preys, predators = X[:, 0], X[:, 1]
    ax.plot(preys, predators, color=col, label='X0=(%.f, %.f)' % (z[0], z[1]))

ax.legend()
ax.grid()
ax.set(xlabel='Number of Preys',
       ylabel='Number of Predators',
       xlim=(xy_range[0], xy_range[1]),
       ylim=(xy_range[2], xy_range[3]))

plt.show()
