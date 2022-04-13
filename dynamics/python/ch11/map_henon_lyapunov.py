import numpy as np

a, b = 1.2, 0.4
x, y = 0.0, 0.0
vec1 = [1, 0]
vec2 = [0, 1]

for i in range(490):

    x = 1 - a * x**2 + y
    y = b * x
    J = np.array([[-2 * a * x, 1], [b, 0]])
    vec1 = J.dot(vec1)
    vec2 = J.dot(vec2)
    dotprod1 = np.dot(vec1, vec1)
    dotprod2 = np.dot(vec1, vec2)
    vec2 = vec2 - np.multiply((dotprod2 / dotprod1), vec1)
    lengthv1 = np.sqrt(dotprod1)
    area = np.multiply(vec1[0], vec2[1]) - np.multiply(vec1[1], vec2[0])
    h1 = np.log(lengthv1) / i
    h2 = np.log(area) / i - h1

print(f'h_1 = {h1}')  # h_1 = 0.3391568093091681
print(f'h_2 = {h2}')  # h_2 = -1.2565387259040743
