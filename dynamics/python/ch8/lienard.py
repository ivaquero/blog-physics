import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
from scipy.integrate import solve_ivp


def lienard(t, z, μ):
    x, y = z
    return [μ * y - μ * (-x + x**3), -x / μ]


t_span = [0, 20]
t = np.arange(t_span[0], t_span[1], 0.1)
x0 = [1, 0]

fig, ax = plt.subplots(dpi=100)

my_images = []
μs = np.arange(0, 5, 0.1)

for μ in μs:
    sol = solve_ivp(lambda t, z: lienard(t, z, μ), t_span, x0)
    X = sol.y
    img = ax.plot(X[0, :], X[1, :], 'r-')
    my_images.append(img)

my_anim = ArtistAnimation(fig,
                          my_images,
                          interval=100,
                          blit=False,
                          repeat_delay=100)

ax.set(xlim=(-1.5, 1.5), ylim=(-5, 5), title='Liénard System')
plt.show()
