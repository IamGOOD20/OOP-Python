class Vector:
    MIN = 0
    MAX = 100

# used if there is a need to use only class attributes @classmethod (cls)
    @classmethod
    def validate(cls, arg):
        return cls.MIN <= arg <= cls.MAX

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        print(self.s2(self.x, self.y))
    def get_cords(self):
        return self.x, self.y

# to define an independent function, may not refer to class attributes and work completely autonomously
    @staticmethod
    def s2(x, y):
        return x*x + y*y

v = Vector(10, 20)
print(v.get_cords())
print(Vector.s2(5, 6))c

