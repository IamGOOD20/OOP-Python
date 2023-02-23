#a = '1.2.3.b'

#print(len(a))

def len_version(arg):
    if len(arg) == 1:
        arg += '.0.0'
    elif len(arg) == 3:
        arg += '.0'
    elif len(arg) > 5:
        arg = arg[:5]
    return arg

print(len_version('1'))
print(len_version('1.2'))
print(len_version('3.3.3.b.23ewwewe'))