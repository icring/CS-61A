# CS 61A Fall 2014
# Name: Sony Theakanath
# Login: cs61a-ach

class VendingMachine(object):
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.current_cash = 0
        self.number_items = 0

    def vend(self):
        if self.number_items == 0:
            return 'Machine is out of stock.'
        elif self.current_cash < self.price:
            return 'You must deposit $' + str(self.price - self.current_cash) + ' more.'
        else:
            temp_cash = self.current_cash - self.price
            self.current_cash = 0
            self.number_items -= 1
            if temp_cash == 0:
                return 'Here is your ' + str(self.name) + '.'
            return 'Here is your ' + str(self.name) + ' and $' + str(temp_cash) + ' change.'

    def restock(self, amount_items):
        self.number_items += amount_items
        return 'Current ' + str(self.name) + ' stock: ' + str(self.number_items)

    def deposit(self, amount_cash):
        if self.number_items > 0:
            self.current_cash += amount_cash
            return 'Current balance: $' + str(self.current_cash)
        return 'Machine is out of stock. Here is your $' + str(amount_cash) + '.'

class MissManners(object):
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    >>> fussy_three = MissManners(3)
    >>> fussy_three.ask('add', 4)
    'You must learn to say please first.'
    >>> fussy_three.ask('please add', 4)
    'Thanks for asking, but I know not how to add'
    >>> fussy_three.ask('please __add__', 4)
    7
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, obj):
        self.obj = obj

    def ask(self, *args):
        if 'please' not in args[0]:
            return 'You must learn to say please first.'
        else:
            to_repr = args[0].replace('please ', '', 1)
            if hasattr(self.obj, to_repr):
                return getattr(self.obj, to_repr)(*args[1:])
            return 'Thanks for asking, but I know not how to ' + to_repr


