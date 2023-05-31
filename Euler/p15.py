# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20grid?

from math import factorial as fac

def compute_routes(w, h):
    return fac(w + h) // (fac(w) * fac(h))

print(compute_routes(20, 20))