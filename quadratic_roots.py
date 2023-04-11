# this script will determine the nature of the roots of a quadratic equation
# ax^2 + bx + c
# using the descriminant b^2 - 4ac

import math as m
import cmath


def descriminant(a, b, c):
    des = (b**2) - (4*a*c)
    if des > 0:
        return "real and distinct roots"
    elif des < 0:
        return "complex roots"
    else:
        return "real repeated roots"


def quadratic_solve(a, b, c):
    # check the nature of the roots before solving
    nature_of_root = descriminant(a, b, c)
    # using the nature of roots to determine the function to use
    if (nature_of_root == "real and distinct roots"):
        print(nature_of_root)
        soln1 = (-b + m.sqrt(((b**2) - 4*a*c)))/(2*a)
        soln2 = (-b - m.sqrt(((b**2) - 4*a*c)))/(2*a)
        return soln1, soln2
    elif (nature_of_root == "real repeated roots"):
        print(nature_of_root)
        soln1 = soln2 = (-b/2*a)
        return soln1, soln2
    else:
        print(nature_of_root)
        soln1 = complex((-b/2*a), (m.sqrt(abs((b**2) - 4*a*c))/(2*a)))
        soln2 = complex((-b/2*a), - (m.sqrt(abs((b**2) - 4*a*c))/(2*a)))
        return soln1, soln2


# print(descriminant(1, -7, 10))
# print(descriminant(3, 2, -1))
# print(descriminant(3, 2, 1))

print(quadratic_solve(1, -7, 10))  # x^2 -7x + 10 = 0
print(quadratic_solve(3, 2, -1))  # 3x^2 + 2x - 1 = 0
print(quadratic_solve(3, 2, 1))  # 3x^2 + 2x + 1 = 0
