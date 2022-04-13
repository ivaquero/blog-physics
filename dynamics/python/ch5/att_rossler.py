import numpy as np
import matplotlib.pyplot as plt


def rossler(x, y, z, a=0.2, b=0.2, c=6.3):
    x_dot = -y - z
    y_dot = x + a * y
    z_dot = b + x * z - c * z
    return (x_dot, y_dot, z_dot)


dt = 0.01
step_count = 50000

xs = np.empty([step_count + 1])
ys = np.empty([step_count + 1])
zs = np.empty([step_count + 1])

# The initial conditions
xs[0], ys[0], zs[0] = (1.0, 1.0, 1.0)

# Iterate.
for i in range(step_count):
    x_dot, y_dot, z_dot = rossler(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot(xs, ys, zs, lw=0.5)
ax.set(xlabel='x', ylabel='y', zlabel='z', title='Rossler Attractor')
plt.show()
