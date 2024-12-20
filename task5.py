import math

def f(x):
    return x**3 - x - 1

def f_prime(x):
    return 3*x**2 - 1

def secant_method(x0, x1, tol, max_iter):
    results = [x0, x1]
    for _ in range(max_iter - 2):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        results.append(x2)
        E_a = abs(x2 - x1)
        E_r = abs(E_a / x2) if x2 != 0 else float('inf')
        if E_a < tol or E_r < tol:
            break
        x0, x1 = x1, x2
    return results

def newton_raphson_method(x0, tol, max_iter):
    results = [x0]
    for _ in range(max_iter - 1):
        x1 = x0 - f(x0) / f_prime(x0)
        results.append(x1)
        E_a = abs(x1 - x0)
        E_r = abs(E_a / x1) if x1 != 0 else float('inf')
        if E_a < tol or E_r < tol:
            break
        x0 = x1
    return results

def iteration_method(x0, tol, max_iter):
    g = lambda x: (x + 1)**(1/3)
    results = [x0]
    for _ in range(max_iter - 1):
        x1 = g(x0)
        results.append(x1)
        E_a = abs(x1 - x0)
        E_r = abs(E_a / x1) if x1 != 0 else float('inf')
        if E_a < tol or E_r < tol:
            break
        x0 = x1
    return results

x0 = 1.5
x1 = 1.6
tol = 1e-3
max_iter = 10

secant_results = secant_method(x0, x1, tol, max_iter)
newton_results = newton_raphson_method(x0, tol, max_iter)
iteration_results = iteration_method(x0, tol, max_iter)

print("Secant Method Results:", secant_results)
print("Newton-Raphson Results:", newton_results)
print("Iteration Method Results:", iteration_results)
