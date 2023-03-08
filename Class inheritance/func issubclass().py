#
# # issubclass(_, _) --> class only | class
# # isinstance(_, _) --> instance of class | class
# class Geom:
#     pass
#
# class Line(Geom):
#     pass
#
#
# #print(Geom.__name__) # name of current class
# l = Line()
# g = Geom()
# print(issubclass(Line, Geom)) # check inheritance; working with classes only
# print(isinstance(g, object)) # True # check instance for ownership
#
#
# print(isinstance(g, Geom)) # True


class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))

v = Vector([1, 2, 3])
print(v)
print(type(v)) # <class '__main__.Vector'>