# CS 61A Fall 2014
# Name: Sony Theakanath
# Login: cs61a-ach

def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def interval(a, b):
    """Construct an interval from a to b."""
    "*** YOUR CODE HERE ***"
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[1]

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """
    "*** YOUR CODE HERE ***"
    assert lower_bound(y) != 0 or upper_bound(y) != 0, 'y interval cannot contain 0!'
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    "*** YOUR CODE HERE ***"
    return interval(lower_bound(x) - upper_bound(y), upper_bound(x) - lower_bound(y))


def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

def question4test():
    a = interval(-2, 4)
    b = interval(5, 2)
    return par1(a, b) != par2(a, b)

def multiple_references_explanation():
    return """No she is not right because 'one' is an uncertain number
    in par2. This can change whereas in par1 there are no variables being
    assigned to each other in par1. This way the 'unknown' numbers will
    not be repeated, therefore it would provide a tighter error bound. """

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    def f(t):
        return a*t*t + b*t + c
    extreme, lower, upper = f(lower_bound(x)), f(lower_bound(x)), f(upper_bound(x))
    if -b/(2*a) >= lower_bound(x) and -b/(2*a) <= upper_bound(x):
        extreme = f(-b/(2*a))
    return interval(min(extreme, lower, upper), max(extreme, lower, upper))


# def polynomial(x, c):
#     """Return the interval that is the range of the polynomial defined by
#     coefficients c, for domain interval x.

#     >>> str_interval(polynomial(interval(0, 2), (-1, 3, -2)))
#     '-3 to 0.125'
#     >>> str_interval(polynomial(interval(1, 3), (1, -3, 2)))
#     '0 to 10'
#     >>> str_interval(polynomial(interval(0.5, 2.25), (10, 24, -6, -8, 3)))
#     '18.0 to 23.0'
#     """
#     "*** YOUR CODE HERE ***"
#     def repeat(numtimes, t):
#         if numtimes == 1:
#             return t
#         else:
#             return repeat(numtimes-1)*t

#     def calc(c, t):
#         total, count, othercount = 0, len(c)-1, 0 
#         while count > 0:
#             total += othercount*repeat(count, t)
#             count -= 1




