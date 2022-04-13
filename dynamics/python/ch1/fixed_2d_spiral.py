import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eig


def derivatives(X, V):

    u = V
    v = -X - (V**3 - V)
    return [u, v]


def euler2(xy_init, step_size, period):
    X, Y = xy_init
    x, y = [], []
    time = []
    for i in range(0, period):
        x.append(X)
        y.append(Y)
        # 每次 + 步长 * 导数（上一对 x,y）
        X += step_size * derivatives(x[-1], y[-1])[0]
        Y += step_size * derivatives(x[-1], y[-1])[1]
        time.append(step_size * i)
    return x, y, time


xy_inits = [[0, 0.1], [1.2, 1.2]]
step_sizes = [0.1, 0.1]
periods = [150, 80]

_, ax = plt.subplots()

for xy_init, step_size, period in zip(xy_inits, step_sizes, periods):

    x, y, t = euler2(
        xy_init,
        step_size,
        period,
    )

    ax.plot(x, y)
    ax.set(xlim=(-2, 2))

plt.show()
