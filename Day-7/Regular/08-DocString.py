def area(radius):
    """Calculates the area of a circle given its radius."""
    import math
    return math.pi * radius ** 2
print(area(5))
print(area.__doc__)