import numpy as np
from numpy.linalg import matrix_power

L = np.array([[0, 3, 1], [0.3, 0, 0], [0, 0.5, 0]])
X0 = np.array([[1000], [2000], [3000]])
X_50 = np.dot(matrix_power(L, 50), X0)
X_50 = X_50.round()
print(f'X(50) = {X_50}')
# X(50) = [[15696.] [ 4604.] [ 2249.]]
