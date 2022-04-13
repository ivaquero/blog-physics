import numpy as np
from numpy.linalg import eig

L = np.array([[0, 3, 1], [0.3, 0, 0], [0, 0.5, 0]])

dL, VL = eig(L)

print(f'Eigenvalues = {dL}')
print(f'Eigenvectors = {VL}')
# Eigenvalues = [ 1.02304502 -0.85068938 -0.17235564]
# Eigenvectors = [[ 0.95064458 -0.92555739  0.18403341] [ 0.27876913  0.32640259 -0.32032617] [ 0.1362448  -0.19184593  0.9292593 ]]
