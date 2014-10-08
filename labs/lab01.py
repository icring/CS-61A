def my_email():
    """Return your email address as a string.

    >>> my_email() != 'oski@berkeley.edu'
    True
    """
    return 'stheakanath@berkeley.edu'

from operator import add, mul

def twenty_fourteen():
    """Come up with the most creative expression that evaluates to 2014, 
    using only numbers and the functions add(. . .) and mul(. . .).

    >>> twenty_fourteen()
    2014
    """
    "*** YOUR CODE HERE ***"
    return add(mul(20, mul(10,10)), add(mul(5,2), 4))