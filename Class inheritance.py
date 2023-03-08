class Geom:
    name = 'Geom'

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print('draws .^.')

class Line(Geom):
    name = 'Line' # override

    def draw(self):
        print('draws a ----')

class Rect(Geom):
    pass
    # def draw(self):
    #     print('draws a []')

l = Line()
r = Rect()

l.set_coords(1, 2, 3, 4)
r.set_coords(1, 2, 3, 4)
r.draw()
