class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)


    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndentationError('Wrong index')

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError('Index must be int type')

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)
        self.marks[key] = value
        # s1[2] = 5
        # print(s1[2])

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('The key must be int type')

        del self.marks[key]

s1 = Student('Eugene', [1, 2, 3, 4, 5])
# print(s1.marks[2]) # 3
#
# print(s1[20]) # ----> def __getitem__ # 3

# if we want to change values: --->  __setitem__

# __setitem__
# s1[10] = 5
# print(s1[2])
# print(s1.marks)


# delitem
# del s1[0]
# print(s1.marks)