from sympy import re, im, sqrt, I, expand

a, b = -0.5, 0.3
k = 15
num_iterations = 2**k


def julia(X):
    x, y = X
    x1, y1 = x, y
    u = sqrt((x1 - a)**2 + (y1 - b)**2) / 2
    v = (x - a) / 2
    u1, v1 = sqrt(u + v), sqrt(u - v)
    xn, yn = u1, v1
    if y1 < b:
        yn = -yn
    if np.random.random() < 0.5:
        xn, yn = -u1, -yn
    return (xn, yn)


x1 = (re(0.5 + sqrt(0.25 - (a + b * I)))).expand(complex=True)
y1 = (im(0.5 + sqrt(0.25 - (a + b * I)))).expand(complex=True)

is_unstable = 2 * abs(x1 + y1 * I)
print(is_unstable)
# 2.78590787704913
