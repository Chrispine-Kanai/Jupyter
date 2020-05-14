from math import sqrt

maxNumber = 20

for a in range(1, maxNumber + 1):
    for b in range(a, maxNumber+1):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if (c_square - c**2) == 0:
            print(a, b, c)
