'''
class Counter:
    def __init__(self):
        self.__counter = 0


    def __call__(self, step=1, *args, **kwargs):
        print('__Call__')
        self.__counter += step
        return self.__counter

c = Counter()
c2 = Counter()
c()
c()
c2()
res = c()
res2 = c2()
print(res) #3
print(res2) #2
'''


'''
class StripChars:
     #Delete signs
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars


    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Must be a str')

        return args[0].strip(self.__chars)

a = StripChars('!?:;" ')
a2 = StripChars(' ')

res = a2('Hello world!?')
res2 = a(' Eugene! ')

print(res)
print(res2)
'''

