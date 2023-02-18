class Personal:
    def __init__(self, old, name):
        self.__old = old
        self.__name = name

# property helps to work with private attributes
#! important! use before getter
    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

ivan = Personal(35, 'Ivan')
ivan.old = 5
print(ivan.old)
del ivan.old
print(ivan.__dict__)
