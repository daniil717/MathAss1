import math

def f(x):
    return math.exp(x) - x ** 2

# с = (a + b) / 2
def bisection_method(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        return None

    for i in range(1, max_iter + 1):
        c = (a + b) / 2

        if abs(f(c)) < tol:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        print(f"Step {i}: a = {a}, b = {b}, c = {c}, f(c) = {f(c)}")

    return (a + b) / 2

a = -2
b = 0
tolerance = 0.000001
max_iter = 7

root = bisection_method(a, b, tolerance, max_iter)
print(root)
