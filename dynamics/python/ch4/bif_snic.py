import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
from scipy.integrate import solve_ivp


def snic(t, z):
    x, y = z
    return [
        x * (1 - x**2 - y**2) - y * (1 + μ + x),
        y * (1 - x**2 - y**2) + x * (1 + μ + x)
    ]


μ = 1
my_images = []
t_span = [0, 200]
t = np.arange(0, 200, 0.01)
x0 = [0.5, 0]

fig, ax = plt.subplots()

for _ in np.arange(-3, 1, 0.1):
    sol = solve_ivp(snic, t_span, x0, dense_output=True)
    X = sol.sol(t).T
    img = ax.plot(X[:, 0], X[:, 1], 'r-')
    my_images.append(img)

my_anim = ArtistAnimation(fig,
                          artists=my_images,
                          interval=100,
                          blit=False,
                          repeat_delay=100)

# HTML(my_anim.to_jshtml())
plt.show()
