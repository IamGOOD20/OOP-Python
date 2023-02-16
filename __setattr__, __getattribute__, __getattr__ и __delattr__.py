class Point:
    MIN = 0
    MAX = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_cord(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        #print('__getattribute__')
        # example
        if item == 'y':
            raise ValueError ('not available')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'j':
            raise ValueError ('not available')
        else:
            object.__setattr__(self, key, value)


    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        print('__delattr__:' + item)
        object.__delattr__(self, item)



v1 = Point(2, 20)
v2 = Point(5, 50)
