import numpy as np
import matplotlib.pyplot as plt
import os

xlist = np.linspace(-10.0, 10.0, 100)
ylist = np.linspace(-4.0, 4.0, 100)
X, Y = np.meshgrid(xlist, ylist)
Z = Y**2 / 2 - 5 * np.cos(X)


def fun(x, y):
    return y**2 / 2 - 5 * np.cos(x)


fig = plt.figure()

ax = fig.add_subplot(121)

ax.contour(X, Y, Z)
ax.set(xlabel=r'$θ$', ylabel=r'$ϕ$')

ax2 = fig.add_subplot(122, projection='3d')

zs = np.array([fun(x, y) for x, y in zip(np.flatten(X), np.flatten(Y))])
Z = zs.reshape(X.shape)

ax2.plot_surface(X, Y, Z)
ax2.set(xlabel=r'$θ$', ylabel=r'$ϕ$', zlabel=r'$H(θ, ϕ)$')

plt.show()
