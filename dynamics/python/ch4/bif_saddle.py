import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

xmin, xmax = -4, 4
μ_min, μ_max = -3, 3

fig, ax = plt.subplots()

line, = ax.plot([], [], lw=2)

ax.plot([xmin, xmax], [0, 0], 'm')
ax.plot([0, 0], [xmin, xmax], 'm')


def init():
    line.set_data([], [])
    return line,


# Animate μ-x^**2, where -3<μ<3.
def animate(μ):
    x = np.linspace(xmin, xmax, 100)
    y = μ - x**2
    line.set_data(x, y)
    return line,


saddle = FuncAnimation(fig,
                       func=animate,
                       frames=np.linspace(μ_min, μ_max, 1000),
                       init_func=init,
                       interval=10,
                       blit=True)

ax.set(xlabel='x', ylabel='y', xlim=(xmin, xmax), ylim=(μ_min, μ_max))
# HTML(saddle.to_jshtml())
plt.show()
