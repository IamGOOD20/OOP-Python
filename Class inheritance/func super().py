# class extension ---> adding methods to child class
# overriding ---> adding an existing method / attribute in a child / parent
# super().__init__(x1, y1, x1, x2) ---> delegation, use of base class functionality
class Geom:
    name = 'Geom'

    def __init__(self, x1, x2, y1, y2):
        print(f'initialize Geom for {self.__class__}')
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

class Line(Geom):
    def draw(self):
        print('draws a _____')

class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill=None):
        super().__init__(x1, y1, x1, x2)
        print('initialize class React')
        self.fill = fill

    def draw(self):
        print('draws []')

l = Line(0, 0, 10, 20)
r = Rect(1, 2, 3, 4)


