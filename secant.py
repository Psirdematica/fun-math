# the secant method

def f(x):
    return 3*(x**2) + 2*x - 1


def secant(x0, x1, tol):
    if f(x1) - f(x0) == 0:
        return f"improper guesses {x0} and {x1}"
    elif f(x0) == 0 or abs(f(x0)) < tol:
        root = x0
        return root
    elif f(x1) == 0 or abs(f(x1)) < tol:
        root = x1
        return root
    else:
        x = (x0*f(x1) - x1*f(x0)) / (f(x1) - f(x0))
        while (f(x) != 0 or abs(f(x)) > tol):
            x0 = x1
            x1 = x
            x = (x0*f(x1) - x1*f(x0)) / (f(x1) - f(x0))
        root = x
        return root


ans = secant(-2, 0, 0.000001)
print(ans)
