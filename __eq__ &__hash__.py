class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        '''make the tuple the same'''
        return hash((self.x, self.y))

# 1
#p1 = Point(1, 2) #hash -9223372036852153656
#p2 = Point(1, 2) #hash -9223372036852153652

# 2 def __eq__ and def __hash__
p2 = Point(1, 2) #hash 3713081631934410656
p1 = Point(1, 2) #hash 3713081631934410656

#print(hash(p1), hash(p2), sep='\n')

#print(p1 == p2)

d = {}
d[p1] = 1
d[p2] = 2
print(d) # {<__main__.Point object at 0x0000000001E82F88>: 2}  we have 1 ket and 2 values

### !!!!!! THIS CODE ALLOWS YOU TO GET 1 KEY FOR OBJECTS WITH THE SAME VALUES
