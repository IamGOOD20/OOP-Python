## __slot__ disables (closes) only local class properties
## and does not impose restrictions on class attributes
# 1. We can safely access the class methods and change the value of self.__length through the setter, for example

# class Point2D:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.__length = (x * x + y * y) ** 0.5
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value

# 2.__slots__ in class inheritance

class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D(Point2D):
    # pass
    #__slots__ = () # thus we open access to the class to the collection of slots
    __slots__ = 'k', # !it's a tuple ','

    def __init__(self, x, y, k): #
        self.x = x
        self.y = y
        self.k = k

# pt3 = Point3D(10, 20)
# pt3.k = 30
# pt3.__dict__
# {'k': 30} # тоесть то что скрыто в __slots__ мы не получаем
# pt3.x
# 10
# del pt3.x  # даже если удалить
# pt3.__dict__
# {'k': 30}
