from operator import add

# Q3
def f1():
    """
    >>> f1()
    3
    """
    "*** YOUR CODE HERE ***"
    return 3

def f2():
    """
    >>> f2()()
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda: 3

def f3():
    """
    >>> f3()(3)
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda x: x

def f4():
    """
    >>> f4()()(3)()
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda: lambda x: lambda: x

# Q4
def lambda_curry2(func):
    """
    Returns a Curried version of a two argument function func.
    >>> x = lambda_curry2(add)
    >>> y = x(3)
    >>> y(5)
    8
    """
    "*** YOUR CODE HERE ***"
    return lambda a: lambda b: func(a, b)

# Q6
def sum(n):
    """Computes the sum of all integers between 1 and n, inclusive.
    Assume n is positive.

    >>> sum(1)
    1
    >>> sum(5)  # 1 + 2 + 3 + 4 + 5
    15
    """
    "*** YOUR CODE HERE ***"
    return 1 if n == 1 else (sum(n-1) + n)

# Q8
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    print(n)
    return 1 if n == 1 else hailstone(n*3+1 if n%2 != 0 else n//2) + 1
