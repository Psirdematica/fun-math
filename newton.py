# this code will find the root of any non linear function using the newton-raphsons method

def f(x):
    return 3*(x**2) + 2*x - 1


def Df(x):
    return 6*(x) + 2


def newton(x0, tol=0.000001):
    if Df(x0) == 0:
        return f"Improper initial root guess {x0}"
    elif f(x0) == 0:
        root = x0
        return root
    else:
        while (f(x0) != 0 or abs(f(x0)) > tol):
            x0 = x0 - (f(x0)/Df(x0))
        root = x0
        return x0


ans = newton(0)
print(ans)
