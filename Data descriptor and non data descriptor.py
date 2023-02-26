class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Wrong type coord')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)


class Point3D:
    x = Integer()
    y = Integer()
    k = Integer()


    def __init__(self, x, y, k):
        self.x = x
        self.y = y
        self.k = k


    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Wrong type coord')

d = Point3D(1, 2, 3)
print(d.__dict__, d.x)

# replacement; used class Integer
'''
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        self._x = coord

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, coord):
        self.verify_coord(coord)
        self._y = coord

    @property
    def k(self):
        return self._k

    @k.setter
    def k(self, coord):
        self.verify_coord(coord)
        self._k = coord
'''


d = Point3D(1, 2, 3)
print(d.__dict__, d.x)
