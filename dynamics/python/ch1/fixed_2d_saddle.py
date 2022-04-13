import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eig
from scipy.integrate import solve_ivp


def generate_mesh_2d(xy_range, n_points):
    X, Y = np.meshgrid(np.linspace(xy_range[0], xy_range[1], n_points),
                       np.linspace(xy_range[2], xy_range[3], n_points))
    return X, Y


def derivatives(t, z):
    X, Y = z
    u = 9 / 7 * X - 4 / 7 * Y
    v = 8 / 7 * X - 9 / 7 * Y
    return [u, v]


def vector_field(X, Y, U, V, ax):

    M = np.hypot(U, V)  # Norm of the growth rate
    M[M == 0] = 1  # Avoid zero division errors
    U /= M  # Normalize each vector_field
    V /= M
    ax.quiver(X, Y, U, V, M, pivot='mid', cmap=plt.cm.jet)


# Here comes the code to generate the arrows showing how the trajectory goes:
def pillar(X, Y, vec):
    x, y = [], []
    t = []
    for i in range(100):
        x.append(X[i * vec])
        y.append(Y[i * vec])
        t.append(i * vec)
    return x, y, t


xy_range = [0, 100, 0, 100]
n_points = 15
A, B = generate_mesh_2d(xy_range, n_points)
u, v = derivatives(t=0, z=[A, B])

_, axes = plt.subplots(1, 2, constrained_layout=True)

xy_inits = [[2, 1], [20, 80]]
vecs = [1, 10]
colors = ['b', 'r']

M = np.array([[9 / 7, -4 / 7], [8 / 7, -9 / 7]])
eigen_values, eigen_vectors = eig(M)
X, Y = eigen_vectors
origin = [0, 0]

t_spans = [[0, 10], [0, 100]]
ts = [
    np.linspace(t_spans[0][0], t_spans[0][1], 5000),
    np.linspace(t_spans[1][0], t_spans[1][1], 5000)
]

for i, (t_span, xy_init, vec,
        color) in enumerate(zip(t_spans, xy_inits, vecs, colors)):
    sol = solve_ivp(derivatives, t_span, xy_init, dense_output=True)
    Z = sol.sol(ts[i]).T
    x, y = Z[:, 0], Z[:, 1]

    x_arrows, y_arrows, time = pillar(x, y, vec)
    direction_x = np.array(x_arrows[1:]) - np.array(x_arrows[:-1])
    direction_y = np.array(y_arrows[1:]) - np.array(y_arrows[:-1])
    axes[i].quiver(x_arrows[:-1],
                   y_arrows[:-1],
                   direction_x,
                   direction_y,
                   scale=1000,
                   lws=time[:-1],
                   color=colors[i])

    vector_field(A, B, u, v, ax=axes[i])
    axes[i].quiver(origin,
                   origin,
                   X,
                   Y,
                   scale=0.01,
                   scale_units='xy',
                   angles='xy',
                   color=['b', 'g'])

    axes[i].plot(x, y, color=colors[i])
    axes[i].set(xlim=(0, 100), ylim=(0, 100))
plt.show()
