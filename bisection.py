# this python code will do bisection
def f(x):
    return 3*(x**2) + 2*x - 1


def bisection(a, b, tol=0.00001):

    if f(a)*f(b) > 0:
        return f"The root of the function does not exist between the given interval [{a},{b}]"
    elif f(a) == 0:
        root = a
        return root
    elif f(b) == 0:
        root = b
        return root
    else:
        x0 = (a+b)/2
        while (f(x0) != 0 or abs(f(x0)) > tol):

            if f(a)*f(x0) < 0:
                b = x0
                x0 = (a+b)/2
            elif f(x0)*f(b) < 0:
                a = x0
                x0 = (a+b)/2
        root = x0
        return root


root = bisection(-2, 0, 0.000001)
print(root)
