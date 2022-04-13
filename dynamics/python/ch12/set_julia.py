import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

# $$fc(z) = z2 + C$$
# Choose a complex C as the ‘seed’.

x_res, y_res = 200, 200
xmin, xmax = -1.5, 1.5
ymin, ymax = -1.5, 1.5

# The mathematical parameters.
z_abs_max = 10
max_iter = 1000


def julia_set(C):
    # Initialise an empty array (corresponding to pixels)
    julia = np.zeros((x_res, y_res))
    width = xmax - xmin
    height = ymax - ymin
    # Loop over each pixel
    for ix in range(x_res):
        for iy in range(y_res):
            # Map pixel position to a point in the complex plane
            z = complex(ix / x_res * width + xmin, iy / y_res * height + ymin)
            # Iterate
            iteration = 0
            while abs(z) <= z_abs_max and iteration < max_iter:
                z = z**2 + C
                iteration += 1
            iteration_ratio = iteration / max_iter
            # Set the pixel value to be equal to the iteration_ratio

            julia[ix, iy] = iteration_ratio

    return julia


julia = julia_set(complex(0.9, 0.5))

# Plot the array using matplotlib's imshow
_, ax = plt.subplots()

ax.imshow(julia, interpolation='nearest', cmap=cm.gnuplot2)
ax.axis('off')
plt.show()
