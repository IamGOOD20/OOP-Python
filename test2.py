class VersionManager:
    archive = []

    @classmethod
    def correct(cls, version='0.0.1', arg2='bla bla bla'):
        if version == '':
            version = '0.0.1'
        version = version.split('.') + ['0', '0']
        version = version[:3]
        for i in version:
            for j in i:
                if j not in '1234567890.':
                    raise TypeError("Error occured while parsing version!")
        return list(map(int, version))

    def __init__(self, version='0.0.1', args='First commit'):
        version = self.correct(version)
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
            raise ValueError('Cannot rollback!')
        else:
            self.archive.pop()
            return self

    def release(self):
        curent_version = self.archive.pop()
        return f'{curent_version[0]}.{curent_version[1]}.{curent_version[2]}'

#'12' -> patch -> minor -> rollback: '0.0.1' should equal '12.0.1'
print(VersionManager('12').patch().minor().rollback().release())
#print(v1.archive)
#v1.rollback()
#print(v1.archive)
#print(v1.rollback())

#print(VersionManager().rollback())#.rollback())

# test.assert_equals(VersionManager().major().rollback().release(), "0.0.1", "Rollback of major release")
# test.assert_equals(VersionManager().major().patch().rollback().major().rollback().release(), "1.0.0", "major -> patch -> rollback -> major -> rollback")
# test.assert_equals(VersionManager().major().patch().rollback().rollback().release(), "0.0.1", "Multiple rollbacks right after another: major -> patch -> rollback -> rollback")