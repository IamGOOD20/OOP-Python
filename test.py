# rollback() - вернуть MAJOR, MINOR и PATCH к их значениям до
# предыдущего основного/второстепенного/патч-вызова или создать исключение
# с сообщением "Cannot rollback!" если нет версии для отката.
# Должны быть возможны множественные вызовы rollback() и восстановление истории версий.
# 2.1.1 --

'''
@classmethod
    def validate(cls, number):
        if 10 > number >= 0:
            return True
        else:
            raise TypeError('"Error occured while parsing version!" should be thrown')
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

'''
print(patch1.archive)
patch1.patch()
print(patch1.archive)
patch1.minor()
print(patch1.archive)
patch1.major()
print(patch1.archive)
patch1.rollback()
patch1.rollback()
print(patch1.release())
'''
