"""
Lecture 18 - October 13, 2014

Announcements

    Project is due Thursday 10/23
    Midterm 2 - Monday 10/27 - 7pm to 9pm

String Representations
    - An object value should behave like the kind of data it is meant to represetn
    - For instance, by producting a string representation of itself
    - String = important: represent language and programs
    - All objects produce two string represntations
        - str for humans
        - repr for Python interpreter
    - str and repr are often teh same but not always

The repr String for an Object
    - repr function returns a Python expression that evaluates to an equal object
    - Returns the canonical string represetnation of the object.
    - For most object types eval(repr(object)) == object
    - The result of calling repr on a value is what Python prints in an interactive session

    >>> 12e12
    120000000000.00
    >>> print(repr(12e12))
    120000000000.00
    
    - Some objects do not have a simple Python-readable string
    
    >>> repr(min)
    '<built in function min>'
    
The str string for an Object
    - Human interpretable strings are useful as well
    
    >>> import datetime
    >>> today = datetime.date(2014, 10, 13)
    >>> repr(today)
    'datetime.date(2014, 10, 13)'
    >>> str(today)
    '2014-10-13'

    - The result of calling str on the value of an expresion is what Python prints using the print function

    >>> print(today)
    2014-10-13

Polynormhic Functions
    - A function that applies to many differnt forms of data
    - str and repr are both polymorphic; they apply to any object
    - repr invoke sa zero-argument medthod __repr__ on its argument

    >>> today.__repr___()
    'datetime.date(2014, 10, 13)'

    - str invoekes a zero_argument method __str__ on its argument

    >>> today.__str__()
    '2014-10-13'

Implemetning repr and str
    - The bhavoir of repr is more complicatied than invoking __repr__ on its argument:
        - An instance attribute called __repr__ is ignored! only class attributes are found
        - How would we implement this behaviro?

    - str is also complicated:
        - Instance attribute called __str__ is also ignored
        - If no __str__ is found uses repr string
        - str is a calss, not a function
"""

class Bear:
    def __init__(self):
        self.__repr__ = lambda: 'oski' #called by oski.__repr__()
        self.__str__ = lambda: 'oski the bear' #called by oski.__str__()

    def __repr__(self): #called by 
        return 'Bear()'
    
    def __str__(self):
        return 'a bear'

def print_bear():
    oski = Beart()
    print(oski) #same with bottom one
    print(repr(oski))
    print(oski.repr())
    print(oski.str()) #no str anywhere so it finds repr. Repr is there so it calls that

def repr(x):
    return :type(x).__repr__(x)
