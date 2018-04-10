# Brennan Huber
# Assignment 3

"""This function with test the functions that are required for assignment 3"""
def test():
    area = areaCircle(15)
    num3 = solveProblem(x = 5, n = 6)

    print 'Area of circle with radius ', 15, ' is ', area
    print 'Solution to (1+x)^n when x is ', 5, 'and n is ', 6, ' is ', num3

"""This function will find the area of a circle, with the given radius"""
def areaCircle(radius):
    return 3.1415*(radius**2)

""" This function will find the value of (1+x)^n with the respective values"""
def solveProblem(x, n):
    return (1 + x)**n

test()