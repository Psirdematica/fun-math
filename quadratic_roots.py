# this script will determine the nature of the roots of a quadratic equation

# ax^2 + bx + c
# using the descriminant b^2 - 4ac

def descriminant(a, b, c):
    des = (b**2) - (4*a*c)
    if des > 0:
        return "real and distinct roots"
    elif des < 0:
        return "complex roots"
    else:
        return "real repeated roots"


print(descriminant(1, -7, 10))
print(descriminant(3, 2, -1))
print(descriminant(3, 2, 1))
