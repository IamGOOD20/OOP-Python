from dataclasses import dataclass, field
from pprint import pprint

# Example:
# class Thing:
#     def __init__(self, name, weight, price):
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     # if we want to see the insides of class:
#     def __repr__(self):
#         return f'{self.__dict__}'
# t = Thing('Harry Potter', 100, 50)
# print(t)
# print(td)


# a lot of code!!!


# we can do it simple:
# # 1
# @dataclass
# class ThingData:
#     name: str
#     weight: int
#     price: float
#
#     def __eq__(self, other):
#         return self.weight == other.weight
#
# td = ThingData('Harry Potter', 100, 50)
# # td2 = ThingData('Titanic', 80, 40)
# # td3 = ThingData('Titanic', 80, 40)
# # print(td3 == td2) # True
#
# # after add __eq__
# td2 = ThingData('Titanic', 80, 40)
# td3 = ThingData('Titanic2', 80, 45)
# print(td3 == td2)
#
# #pprint(ThingData.__dict__) # shows all attributes


@dataclass
class ThingData:
    name: str
    weight: int = 0
    price: float = 0
    dims: list = field(default_factory=list) # dims is assigned to the list function and the list
                                             # function returns an empty list
                                             # so for all of new instances it will be always empty


td = ThingData('Harry Potter', 100)
td2 = ThingData('Harry Potter', 100)
#print(td.__dict__)
#pprint(td.__dict__)

td.dims.append(10)
print(td)
print(td2)
