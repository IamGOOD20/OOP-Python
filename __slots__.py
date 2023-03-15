class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y



class Point2D:
    # __slots__collection prevents the creation of attributes other than those specified
    # no __dict__ collection
    __slots__ = ('x', 'y')

    MAX_COORD = 100
    def __init__(self, x, y):
        self.x = x # but we can change it, but can't create new
        self.y = y


# benefits of __slots__ collection:
# Point2D takes up less memory (4 times)
# Point2D more quickly
