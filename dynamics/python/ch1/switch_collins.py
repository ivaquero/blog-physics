import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eig
from scipy.integrate import solve_ivp


def collins(t, z):
    A, B = z
    u = 5 / (1 + B**4) - A
    v = 5 / (1 + A**4) - B
    return [u, v]


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


xy_range = [0, 5, 0, 5]
n_points = 10
A, B = generate_mesh_2d(xy_range, n_points)
u, v = collins(t=0, z=[A, B])

_, ax = plt.subplots()

vector_field(A, B, u, v, ax=ax)

row, col = np.arange(0, 5, 0.1), np.arange(0, 5, 0.1)
null_row, null_col = 5 / (1 + col**4), 5 / (1 + row**4)

ax.plot(row, null_col)
ax.plot(null_row, col)
plt.show()
