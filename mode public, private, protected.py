class Point:
    ''' _attribute - protected (warning do not use,
     __attribute - private'''
    def __init__(self, x=0, y=0):
        self.x = self.y = 0
        if self.__check_value(x) and self.__check_value(y):
            #self._x = x #attribute protected
            #self._y = x
            self.__x = x #attribute private
            self.__y = y

# privat method
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

# setter
    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('numbers only')

# getter
    def get_coord(self):
        return self.__x, self.__y


first = Point(1, 2)
first.set_coord(2, 10)
print(first.get_coord())
print(dir(first)) #show all attributs
print(first._Point__x) #we can call even privat atribut
