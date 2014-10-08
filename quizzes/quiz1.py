# CS 61A Fall 2014
# Name: Kuriakose Theakanath
# Login: cs61a-ach


def two_equal(a, b, c):
    """Return whether exactly two of the arguments are equal and the
    third is not.

    >>> two_equal(1, 2, 3)
    False
    >>> two_equal(1, 2, 1)
    True
    >>> two_equal(1, 1, 1)
    False
    >>> result = two_equal(5, -1, -1) # return, don't print
    >>> result
    True

    """
    "*** YOUR CODE HERE ***"
    return (a == b and b != c) or (a == c and c != b) or (b == c and c != a) 


def same_hailstone(a, b):
    """Return whether a and b are both members of the same hailstone
    sequence.

    >>> same_hailstone(10, 16) # 10, 5, 16, 8, 4, 2, 1
    True
    >>> same_hailstone(16, 10) # order doesn't matter
    True
    >>> result = same_hailstone(3, 19) # return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    if a > b:
        a, b = b, a
    while a != 1:
        if a == b:
            return True
        else:
            if a % 2 == 0:
                a = a // 2
            else:
                a = a * 3 + 1 
    return False

def near_golden(perimeter):
    """Return the integer height of a near-golden rectangle with PERIMETER.

    >>> near_golden(42) # 8 x 13 rectangle has perimeter 42
    8
    >>> near_golden(68) # 13 x 21 rectangle has perimeter 68
    13
    >>> result = near_golden(100) # return, don't print
    >>> result
    19

    """
    "*** YOUR CODE HERE ***"
    counter, ratio, sm_height = 1, perimeter, perimeter
    while counter < perimeter/2:
        width, height, counter = (perimeter - 2*counter)/2, counter, counter +1
        if abs(height/width - (width/height-1)) < ratio:
            ratio, sm_height = abs(height/width - (width/height-1)), height
    return sm_height
