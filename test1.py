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
    archive = [[0, 0, 1]]

    def __init__(self, version, *args):
        patch_number = '1.2.3.4.5.6.7.8.9.0.'
        if version not in patch_number:
            raise TypeError('Error occured while parsing version!')
        else:
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

    def minor(self):
        self.MINOR += 1
        self.PATCH = 0
        self.archive.append([self.MAJOR, self.MINOR, self.PATCH])

    def patch(self):
        self.PATCH += 1
        self.archive.append([self.MAJOR, self.MINOR, self.PATCH])

    def rollback(self):
        if len(self.archive) == 0:
            return 'Cannot rollback!'
        else:
            self.archive.pop()

    def release(self):
        curent_version = self.archive.pop()
        return f'{curent_version[0]}.{curent_version[1]}.{curent_version[2]}'


v1 = VersionManager('')
