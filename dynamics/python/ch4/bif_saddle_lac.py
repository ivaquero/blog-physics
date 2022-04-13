import numpy as np
import matplotlib.pyplot as plt


def lac(X, a, r):
    return (a + X**2) / (1 + X**2) - r * X


def stablity(X_init, r):
    perturbation = 0.01
    time_interval = 0.01
    x = []
    X = X_init + perturbation
    for i in range(100):
        X += time_interval * lac(X, a, r)
    return abs(X - X_init) <= perturbation


x_range = [0.001, 10]
X = np.linspace(x_range[0], x_range[1], 2000)
a = 0.006
r = (1 / X) * (a + X**2) / (1 + X**2)

stable_x = []
stable_y = []
unstable_x = []
unstable_y = []

for ri, x in zip(r, X):
    if stablity(x, ri):
        stable_x.append(ri)
        stable_y.append(x)
    else:
        unstable_x.append(ri)
        unstable_y.append(x)

_, ax = plt.subplots()

ax.scatter(stable_x, stable_y, color='g')
ax.scatter(unstable_x, unstable_y, color='r')
ax.plot(r, X)
ax.set(xlim=(0, 1), xlabel='r', ylabel='X')


def arrows(r, X, head_width=0.02, head_length=0.5):
    ax.vlines(r, 0, 10, color='black')
    for x in X:
        points_at = lac(x, a, r)
        ax.arrow(r,
                 x,
                 0,
                 points_at,
                 head_width=head_width,
                 head_length=head_length,
                 color='black')


arrows(0.2, [2, 6])
arrows(0.4, [1, 6])
arrows(0.6, [1, 6])

plt.show()
