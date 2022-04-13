import numpy as np
from scipy.linalg import eig
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from itertools import product

a, b, c, d = 2, 1, 1, 2
# 矩阵
m = np.array([[a, b], [c, d]])
# 特性值数组
eigen = eig(m)[0]


def derivatives(t, z):
    x, y = z
    u = a * x + b * y
    v = c * x + d * y
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


xlabel, ylabel = ['x', 'u'], ['y', 'v']
ic = np.linspace(-1, 1, 5)

t_span1 = [0, 4]
t_span2 = [-4, 0]
t1 = np.linspace(t_span1[0], t_span1[1], 1000)
t2 = np.linspace(t_span2[0], t_span2[1], 1000)

xy_range = [-1, 1, -1, 1]
n_points = 10

_, ax = plt.subplots(1, 2, constrained_layout=True)

for i in range(2):
    if i == 1:
        a, b, c, d = eigen[1], 0, 0, eigen[0]

    for init in product(ic, ic):
        sol1 = solve_ivp(derivatives, t_span1, init, dense_output=True)
        X1 = sol1.sol(t1).T
        x1, y1 = X1[:, 0], X1[:, 1]
        ax[i].plot(x1, y1, 'r-')
        sol2 = solve_ivp(derivatives, t_span2, init, dense_output=True)
        X2 = sol1.sol(t1).T
        x2, y2 = X1[:, 0], X1[:, 1]
        ax[i].plot(x2, y2, 'r-')

    ax[i].set(xlim=(-1, 1), ylim=(-1, 1), xlabel=xlabel[i], ylabel=ylabel[i])

    major_locator = plt.MultipleLocator(0.5)
    ax[i].xaxis.set_major_locator(major_locator)
    ax[i].yaxis.set_major_locator(major_locator)

    # 箭头位置
    X, Y = generate_mesh_2d(xy_range, n_points)
    # X, Y = np.mgrid[-1:1:10j, -1:1:10j]
    # 箭头方向，通常为二维度组
    u, v = derivatives(t=0, z=[X, Y])
    ax[i].quiver(X, Y, u, v, color='b')

plt.show()
