
def f(x):
    return x**3 - x - 1

def f_prime(x):
    return 3*x**2 - 1

def secant_method(x0, x1, max_iter):
    results = [x0, x1]
    for _ in range(max_iter - 2):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        results.append(x2)
        x0, x1 = x1, x2
    return results[:max_iter]

def iteration_method(x0, max_iter):
    g = lambda x: (x + 1)**(1/3)
    results = [x0]
    for _ in range(max_iter - 1):
        x1 = g(x0)
        results.append(x1)
        x0 = x1
    return results[:max_iter]

def newton_raphson_method(x0, max_iter):
    results = [x0]
    for _ in range(max_iter - 1):
        x1 = x0 - f(x0) / f_prime(x0)
        results.append(x1)
        x0 = x1
    return results[:max_iter]

x0 = 1.5
x1 = 1.6
max_iter = 7

secant_results = secant_method(x0, x1, max_iter)
iteration_results = iteration_method(x0, max_iter)
newton_results = newton_raphson_method(x0, max_iter)

print(f"{'Iter':<5}{'Secant Method':<20}{'Iteration Method':<20}{'Newton-Raphson Method':<20}")
for i in range(max_iter):
    print(f"{i:<5}{secant_results[i]:<20.10f}{iteration_results[i]:<20.10f}{newton_results[i]:<20.10f}")
