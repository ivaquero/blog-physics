import numpy as np
import matplotlib.pyplot as plt

V = np.arange(-2, 2.05, 0.01)
W = V * (1 - V) * (V - 0.1)
w_ = 2 * V

_, ax = plt.subplots()

ax.plot(V, W)
ax.plot(V, w_)
ax.set(xlim=(-2, 2.05))

plt.show()
