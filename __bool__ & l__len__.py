class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__')
        return self.x * self.x + self.y * self.y
        # return True if != 0 and if not 0

    def __bool__(self): # higher priority for len
        print('__bool__')
        return self.x == self.y

#p1 = Point(3, 4) # return True if != 0 and if not 0


## AFTER BOOL METHOD
# p1 = Point(1, 10) # False
# p1 = Point(1, 1) # True
p1 = Point(1, 10) # True

if p1:
    print('__bool : True')
else:
    print('___bool : False')