import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - x - 1

def f_prime(x):
    return 3*x**2 - 1

def secant_method(x0, x1, tol, max_iter):
    results = []
    for _ in range(max_iter):
        if abs(f(x1)) < tol:
            break
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        results.append(x2)
        x0, x1 = x1, x2
    return x1, results

def iteration_method(x0, tol, max_iter):
    g = lambda x: (x + 1)**(1/3)
    results = []
    for _ in range(max_iter):
        x1 = g(x0)
        results.append(x1)
        if abs(x1 - x0) < tol:
            break
        x0 = x1
    return x1, results

def newton_raphson_method(x0, tol, max_iter):
    results = []
    for _ in range(max_iter):
        x1 = x0 - f(x0) / f_prime(x0)
        results.append(x1)
        if abs(x1 - x0) < tol:
            break
        x0 = x1
    return x1, results

x0 = 1.5
x1 = 1.5
x2 = 1.6
tol = 1e-3
max_iter = 100

secant_root, secant_results = secant_method(x1, x2, tol, max_iter)
iteration_root, iteration_results = iteration_method(x0, tol, max_iter)
newton_root, newton_results = newton_raphson_method(x0, tol, max_iter)

print(f"Secant method: root ≈ {secant_root}")
print(f"Iteration method: root ≈ {iteration_root}")
print(f"Newton-Raphson method: root ≈ {newton_root}")

plt.figure(figsize=(10, 6))
plt.plot(range(len(secant_results)), secant_results, label="Secant method", marker="o")
plt.plot(range(len(iteration_results)), iteration_results, label="Iteration method", marker="s")
plt.plot(range(len(newton_results)), newton_results, label="Newton-Raphson method", marker="x")
plt.axhline(y=secant_root, color='gray', linestyle='--', label=f"Root ≈ {secant_root:.3f}")
plt.xlabel("Iteration number")
plt.ylabel("Root approximation")
plt.title("Comparison of methods for finding the root")
plt.legend()
plt.grid()
plt.show()
