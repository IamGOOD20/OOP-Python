# type metaclass


class Point:
    MAX_COORD = 100
    MIN_COORD = 0


# same:
# Python console
# >>> A = type('Point', (), {'MAX_COORD': 100, 'MIN_COORD':0})
# pt = A()
# >>> class B1: pass
# >>> class B1: pass
# A = type('Point', (B1, B2), {'MAX_COORD': 100, 'MIN_COORD':0})
# A.__mro__
# (<class '__main__.Point'>, <class '__main__.B1'>, <class '__main__.B2'>, <class 'object'>)
#
# we can add methods:
# def method1(self):
#     print(sels.__dict__)
# A = type('Point', (B1, B2), {'MAX_COORD': 100, 'method1': method1})
# pt = A()
# pt.method1()
# {}
#
# add methods 2: Lambda:
# A = type('Point', (B1, B2), {'MAX_COORD': 100, 'method1': lambda self: self.MAX_COORD})

