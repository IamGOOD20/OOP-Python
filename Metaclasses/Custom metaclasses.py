# Make own Metaclasses

# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0

# simple metaclass using func:
# def create_class_point(name, base, attrs):
#     attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0}) # add attributes
#     return type(name, base, attrs)
#
#
# # use our metaclass:
# class Point(metaclass=create_class_point):
#     def get_coords(self):
#         return (0, 0)

# pt = Point()
# print(pt.MAX_COORD)
# print(pt.get_coords())

# using class ---> metaclass


class Meta(type): # it's metaclass, so it must be inherited from type
    def __new__(cls, name, base, attrs):
        attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
        return type.__new__(cls, name, base, attrs)


    # def __init__(cls, name, base, attrs): # use cls not self, we make class!
    #     super().__init__(name, base, attrs)
    #     cls.MAX_COORD = 100
    #     cls.MIN_COORD = 0


class Point(metaclass=Meta):
    def get_coords(self):
        return (0, 0)


pt = Point()
print(pt.MAX_COORD)
print(pt.MIN_COORD)
print(pt.get_coords())