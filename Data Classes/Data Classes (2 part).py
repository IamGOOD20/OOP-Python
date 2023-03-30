from dataclasses import dataclass, field, InitVar


# field() often methods:
# repr - boolean whether to specify the current attribute in the __repr__ magic method (True/False)
# compare - boolean, use attribute when comparing (True/False)
# default - default value (value used in immutable data types)

# 1. add a compute attribute
# 2. how did func field works
# class Vector3D:
#     def __init__(self, x: int, y: int, k: int):
#         self.x = x
#         self.y = y
#         self.k = k
#         self.length = (x * x + y * y + k * k) ** 0.5
#
#
# @dataclass
# class VectorD:
#     x: int = field(repr=False) # do not show
#     y: int
#     k: int = field(compare=False) # do not comparing
#     length: float = field(init=False, compare=False) # do not show and comparing
#
#
#     def __post_init__(self):
#         self.length = (self.x * self.x + self.y * self.y + self.k * self.k) ** 0.5 # print(v) >>> VectorD(x=10, y=20, k=30)
#
#
# v1 = VectorD(10, 20, 30)
# v2 = VectorD(10, 25, 5)
# print(v1 == v2) # False



# use InitVar class
# class Vector3D:
#     def __init__(self, x: int, y: int, k: int, calc_len: bool = True): # calc_len: bool = True
#         self.x = x
#         self.y = y
#         self.k = k
#         self.length = (x * x + y * y + k * k) ** 0.5 if calc_len else 0 # if calc_len else 0
#
# @dataclass
# class VectorD:
#     x: int = field(repr=False) # do not show
#     y: int
#     k: int = field(compare=False) # do not comparing
#     calc_len: InitVar[bool] = True # if True ----> __post_init__
#     length: float = field(init=False, compare=False, default=0) # do not show and comparing
#
#
#     def __post_init__(self, calc_len: bool): # add calc_len; if calc == True it will work automatically
#         if calc_len:
#             self.length = (self.x * self.x + self.y * self.y + self.k * self.k) ** 0.5
#
# v1 = VectorD(1, 2, 3, False)
# v2 = VectorD(1, 2, 3)
# print(v1)

# 3 part @dataclass attributes
# the popular is init, repr, eq, order, unsafe_hash, frozen, slots


#@dataclass(init=False) # prohibition on the work of the initializer
#@dataclass(repr=False) # >>> <__main__.VectorD object at 0x00000000022FD508>
#@dataclass(eq=False) # comparison prohibition
#@dataclass(order=True) # <; >; <=; >=;
#@dataclass(frozen=True) # freezing all attributes, unable to change or add attributes
class VectorD:
    x: int = field(repr=False) # do not show
    y: int
    k: int = field(compare=False) # do not comparing
    calc_len: InitVar[bool] = True # if True ----> __post_init__
    length: float = field(init=False, compare=False, default=0) # do not show and comparing


    def __post_init__(self, calc_len: bool): # add calc_len; if calc == True it will work automatically
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.k * self.k) ** 0.5

v1 = VectorD(1, 2, 3, False)
v2 = VectorD(1, 2, 3)
print(v1==v2)
print(v1)
print(v1 <= v2) # @dataclass(order=True) !!!  eq=True + order=True == <= True
