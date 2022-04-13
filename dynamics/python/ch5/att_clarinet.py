import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation


def clarinet(t, z, a=1):
    X, V = z
    u = V
    v = -X - (a * V**3 - V)
    return [u, v]


def arrows(x, y):
    dx, dy = [], []
    for x, y in zip(x, y):
        ver = clarinet(t=0, z=[x, y])
        dx.append(ver[0])
        dy.append(ver[1])

    m = np.hypot(dx, dy)

    for i in range(1, len(x), 50):
        ax.arrow(x[i],
                 y[i],
                 dx[i] / m[i] / 30,
                 dy[i] / m[i] / 30,
                 head_width=0.05,
                 color='black')


θs = np.linspace(0, 2 * np.pi, 5)
coordinates = []

for θ in θs:
    coordinates.append([1.5 * np.cos(θ), 1.5 * np.sin(θ)])
    coordinates.append([0.05 * np.cos(θ), 0.05 * np.sin(θ)])

a_list = np.arange(0.1, 2, 0.1)[::-1]
fig, ax = plt.subplots()
t_span = [0, 10]
t = np.linspace(t_span[0], t_span[1], 100)


def animate(i):
    ax.clear()
    ax.set(xlabel='x', ylabel='y', ylim=(-1, 1), xlim=(-2, 2))
    for coordinate in coordinates:
        x_i = coordinate[0]
        y_i = coordinate[1]
        sol = solve_ivp(lambda t, z: clarinet(t, z, a_list[i]),
                        t_span, [x_i, y_i],
                        dense_output=True)
        X = sol.sol(t).T
        x, y = X[:, 0], X[:, 1]
        ax.plot(x, y)

    ax.set(title=f'a={a_list[i]}')


def animate2(i):
    ax.clear()
    ax.set(xlabel='time', ylabel='deviation', xlim=(0, 100), ylim=(-5, 5))
    x_i = 0
    if a_list[i] != 0:
        y_i = 1 / np.sqrt(a_list[i])
    else:
        y_i = 0
    sol = solve_ivp(lambda t, z: clarinet(t, z, a_list[i]),
                    t_span, [x_i, y_i],
                    dense_output=True)
    X = sol.sol(t).T
    x, y = X[:, 0], X[:, 1]
    ax.plot(t, x)
    ax.set(title=f'a={a_list[i]}')


anim = FuncAnimation(fig, animate, frames=19, interval=100)

plt.show()
