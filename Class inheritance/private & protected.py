class Geom:
    name = 'Geom'

    def __init__(self, x1, x2, y1, y2):
        print(f'initialize Geom for {self.__class__}')
        # self.__x1 = x1
        # self.__x2 = x2
        # self.__y1 = y1
        # self.__y2 = y2
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

    # def get_coords(self):
    #     return (self.__x1, self.__y1)


    # protected method
    # can't be used in children classes
    # only protected _verify_cords
    def __verify_cords(self, coord):
        return 0 <= coord < 100


class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill='red'):
        super().__init__(x1, y1, x1, x2)
        self.__fill = fill

    # error; if protected atributs ---> only Father class!
    #def get_coords(self):
    #    return (self.__x1, self.__y1)

    def get_coords(self):
        return (self._x1, self._y1)

#     return (self.__x1, self.__y1)
r = Rect(0, 0, 10, 20)
r.get_coords()
#print(r.__dict__)