'''
    @classmethod
    def validate(cls, number):
        #if 10 > number >= 0 and isinstance(number, int): #and type(number) == 'int':
        if type(number) == int:
            return True
        else:
            raise TypeError('Error occured while parsing version!')

#if self.validate(MAJOR) and self.validate(MINOR) and self.validate(PATCH):
'''


class VersionManager:
    archive = []

    @classmethod
    def len_version(cls, arg):
        if len(arg) == 1:
            arg += '.0.0'
        elif len(arg) == 3:
            arg += '.0'
        elif len(arg) > 5:
            arg = arg[:5]
        elif arg == '':
            arg = '0.0.1'
        return arg

    def __init__(self, version='0.0.1', args='First commit'):
        version = self.len_version(version)
        for i in version:
            if i not in '1.2.3.4.5.6.7.8.9.0.':
                raise TypeError("Error occured while parsing version!")

        version = list(map(int, version.split('.')))
        self.MAJOR = version[0]
        self.MINOR = version[1]
        self.PATCH = version[2]
        self.archive.append([self.MAJOR, self.MINOR, self.PATCH])

    def major(self):
        self.MAJOR += 1
        self.MINOR = 0
        self.PATCH = 0
        self.archive.append([self.MAJOR, self.MINOR, self.PATCH])
        return self

    def minor(self):
        self.MINOR += 1
        self.PATCH = 0
        self.archive.append([self.MAJOR, self.MINOR, self.PATCH])
        return self

    def patch(self):
        self.PATCH += 1
        self.archive.append([self.MAJOR, self.MINOR, self.PATCH])
        return self

    def rollback(self):
        if len(self.archive) == 0:
            return 'Cannot rollback!'
        else:
            self.archive.pop()
            return self

    def release(self):
        curent_version = self.archive.pop()
        return f'{curent_version[0]}.{curent_version[1]}.{curent_version[2]}'


#test.assert_equals(VersionManager().major().release(), "1.0.0", "First major release")


#print(VersionManager().major().release())
v1 = VersionManager()
print(v1.major())
#print(v1.MAJOR, v1.MINOR, v1.PATCH)
#v1.major()
#print(v1.MAJOR, v1.MINOR, v1.PATCH)
print(v1.release())
