# An abstract method is, in object-oriented programming, a class method for which there is no implementation.
# A class containing abstract methods is also called abstract. Abstract methods are often confused with virtual methods.

# 4.1
# class Geom:
#     def get_pr(self):
#         return -1

# 4.2
class Geom:
    def get_pr(self):
        raise NotImplemented('In the child class, the get_pr_method must be overridden')

class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    # def get_rect_pr(self):
    # 3. solution
    def get_pr(self):
        return 2*(self.w+self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    # def get_rect_pr(self):
    # 3. solution
    def get_pr(self):
        return 4*self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # def get_rect_pr(self):
    # 3. solution
    #def get_pr(self):
     #   return self.a + self.b + self.c


# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# s1 = Square(10)
# s2 = Square(20)
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)

# 1. error Square does't have get_sq_pr
# geom = [r1, r2, s1, s2]
# for g in geom:
#     print(g.get_rect_pr())

# 2. solutions
#for g in geom:
    # if isinstance(g, Rectangle):
    #     print(g.get_rect_pr())
    # else:
    #     print(g.get_sq_pr())

# 3. add 3-nd class Triangle:
# geom = [r1, r2, s1, s2, t1, t2]
# for g in geom:
#     print(g.get_pr())
# each object uses its own method, that's why it works

# code update
geom = [
    Rectangle(1, 2), Rectangle(3, 4),
    Square(10), Square(20),
    Triangle(1, 2, 3), Triangle(4, 5, 6)
]

for i in geom:
    print(i.get_pr())

# 4. if we forget to declare a method in a class
    # 1. we can use Parent class and make func in it and then all classe inheritan from it
    # 2. best solution is:
    #     class Geom:
    #         def get_pr(self):
    #             raise NotImplemented('In the child class, the get_pr_method must be overridden')