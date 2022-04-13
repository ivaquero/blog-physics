import numpy as np
import matplotlib.pyplot as plt


def lotka_volterra(t, z, coefs=[0.5, 0.01, 0.2, 0.005]):
    x, y = z
    a, b, c, d = coefs
    return [a * x - b * x * y, -c * y + d * x * y]


def generate_mesh_2d(xy_range, n_points):
    X, Y = np.meshgrid(np.linspace(xy_range[0], xy_range[1], n_points),
                       np.linspace(xy_range[2], xy_range[3], n_points))
    return X, Y


def vector_field(X, Y, U, V, xy_range, ax):
    # Norm of the growth rate
    M = np.hypot(U, V)  # equivalent to np.sqrt(U**2 + V**2)
    M[M == 0] = 1  # Avoid zero division errors
    U /= M  # Normalize each vector_field
    V /= M

    ax.quiver(X, Y, U, V, M, pivot='mid', cmap=plt.cm.jet)


def euler2(xy_init, step_size, period):
    X, Y = xy_init
    x, y = [], []
    time = []
    for i in range(0, period):
        x.append(X)
        y.append(Y)
        # 每次 + 步长 * 导数（上一对 x,y）
        z = [x[-1], y[-1]]
        X += step_size * lotka_volterra(t=0, z=z)[0]
        Y += step_size * lotka_volterra(t=0, z=z)[1]
        time.append(step_size * i)
    return x, y, time


xy_range = [0, 100, 0, 100]
n_points = 15

# create a grid
X, Y = generate_mesh_2d(xy_range, n_points)
# compute growth rate on the grid
U, V = lotka_volterra(t=0, z=[X, Y])

_, axes = plt.subplots(1, 2, dpi=100)

step_sizes = [0.01, 0.1]
xy_init = [80, 60]
period = 10000

for ind, step in enumerate(step_sizes):

    x, y, time = euler2(xy_init, step, period)
    axes[ind].scatter(x, y)
    vector_field(X, Y, U, V, xy_range, axes[ind])
    axes[ind].set(xlim=(xy_range[0], xy_range[ind]),
                  ylim=(xy_range[2], xy_range[ind]),
                  title=f'δt = {step}')

plt.show()
