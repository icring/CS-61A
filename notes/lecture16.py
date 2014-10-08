"""
October 8, 2014
Lecture 16 - CS 61A
Sony Theakanath

Object Oriented Programming
    - A method for organizing programs
        - Data Abstraction
        - Bundling together information

Classes
    - A class serves as a template for its instances
    - Attributes are needed (what describes that certain class?)
    
    Accessing a class:
        a = Account('Jim')
        a.holder

        Calling a class gives an instance
        calling holder gets the attribute of the Account class of instance Jim

        Pretty self explanatory stuff. Same as Java.

    Better Idea:
        All bank accounts share a withdraw method and a deposit method

Class Statement
    class <name>:
        <suite>

    A class statement creates a new class and binds that class to the <name> in the first frame of the enviroment

    Assignment and def statements in <suite> create attributes of the class.

    When the class statement in executed the suite is executed.
"""

class Clown:
    nose = 'big and red'
    def dance():
        return 'No thanks'

"""
    >>>Clown.nose gives 'big and red'
    You're accessing the nose attribute of the class.
    
    Clown.dance() calls the dance() method and gives 'No thanks'
"""

"""
Object Constrution
    Idea: All bank accounts have a balance and an account holder. The account class should add those attributes to each of its instances.

    >>> a = Account('Jim')

    When a class is called:
        1. A new instance of that class is created.
        2. the __init__ method of the class is called with the new object as its first argument (named self), allong with any additional argument provided in the call expression. 

"""

class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

"""
    When creating Account object, init is called. Basically the constructor.
    Here it sets the balance to 0. And calls the holder 'Jim'
    
    Object Identity

        Every Object that is an instance of a user defined class has a unique identity
        
        >>> a = Account('Jim')
        >>> b = Account('Jack')
        >>> a is a 
        True
        >>> a is not b
        True
        >>> c = a
        >>> c is a
        True
"""

"""
Methods
    Methods are functions defined in the suite of the class statement

"""

    def deposit(self, amount):
        self.balance = self.balance + amount
        return balance

"""
    Invoking methods
        Account.deposit(100)

    Dot expeessions
        <expression> , <name>

        The expression can be a valid Python expression

        The <name> must be a simple name.

        Evalates to the value of the attrivute looked up by <name> in the object that is the value of the <expression>

        tom_account.deposit is a <dot expression>with the (10) is a call expression.

    Attributes
        getatter, we can look up an attribute using a string
        >>> getattr(tom_account, 'balance')
        10
        >>> hasattr(tom_account, 'balance')
        True
"""
"""
    Difference between Methods and Functions
        Functions: we have been creating since the beginning of the course
        Bound methods: which couple together a function and the object on which that will be invoked
        

        Object + Function = Bound Method
        >>> type(Account.deposit)
        <class  'function'>
        >>> type(tom_account.deposit)
        <class method>

        SO A METHOD IS ONE BOUND TO A CREATED OBJECT. FUNCTION IS JUST TO THE CLASS.
        >>> Account.deposit(tom_account, 1001)
        1011
        >>> tom_account.deposit(1003)
        2014

        BOTH ARE THE SAME THING!

"""

