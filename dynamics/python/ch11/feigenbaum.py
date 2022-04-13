import numpy as np
import matplotlib.pyplot as plt


def f(x, r):
    return r * x * (1 - x)


ys = []
rs = np.linspace(0, 4, 2000)
# rs = np.linspace(3.5, 4, 2000) # For Figure 14.16.
for r in rs:
    x = 0.1
    for _ in range(500):
        x = f(x, r)
    for _ in range(50):
        x = f(x, r)
        ys.append([r, x])

ys = np.array(ys)

_, ax = plt.subplots(dpi=100)

ax.plot(ys[:, 0], ys[:, 1], 'r.', markersize=.8)
ax.set(xlabel='$μ$', ylabel='x')
plt.show()
