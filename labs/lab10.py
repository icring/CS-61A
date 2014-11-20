#############
# Iterators #
#############

class IteratorRestart(object):
    """
    >>> i = IteratorRestart(2, 7)
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        "*** YOUR CODE HERE ***"
        self.beg = (start - 1)
        self.current = (start - 1)
        self.end = end

    def __next__(self):
        "*** YOUR CODE HERE ***"
        if self.current == self.end:
            self.current = self.beg
            raise StopIteration
        self.current += 1
        return self.current

    def __iter__(self):
        "*** YOUR CODE HERE ***"
        return self

##############
# Generators #
##############

def countdown(n):
    """
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    i = n
    while i >= 0:
        yield i
        i -= 1

class Countdown(object):
    """
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, num):
        self.start = num

    def __iter__(self):
        while self.start >= 0:
            yield self.start
            self.start -= 1

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    i = n
    yield n
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        elif n % 2 == 1:
            n = n * 3 + 1
        yield n


###########
# Streams #
###########

class Stream(object):
    class empty(object):
        def __repr__(self):
            return 'Stream.empty'

    empty = empty()

    def __init__(self, first, compute_rest=lambda: Stream.empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest

    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest

    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

def make_integer_stream(first=1):
    def compute_rest():
        return make_integer_stream(first+1)
    return Stream(first, compute_rest)

def add_streams(s1, s2):
    "*** YOUR CODE HERE ***"
    def rest():
        return add_streams(s1.rest, s2.rest)
    return Stream(s1.first + s2.first, rest)


