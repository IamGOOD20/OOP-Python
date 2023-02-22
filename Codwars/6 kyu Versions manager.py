'''
DESCRIPTION:
In this kata we are going to mimic a software versioning system.

You have to implement a VersionManager class.

It should accept an optional parameter that represents the initial version.
The input will be in one of the following formats: "{MAJOR}", "{MAJOR}.{MINOR}", or "{MAJOR}.{MINOR}.{PATCH}".
More values may be provided after PATCH but they should be ignored.
If these 3 parts are not decimal values, an exception with the message "Error occured while parsing version!" should be thrown.
If the initial version is not provided or is an empty string, use "0.0.1" by default.

This class should support the following methods, all of which should be chainable (except release):

major() - increase MAJOR by 1, set MINOR and PATCH to 0
minor() - increase MINOR by 1, set PATCH to 0
patch() - increase PATCH by 1
rollback() - return the MAJOR, MINOR, and PATCH to their values before the previous major/minor/patch call,
or throw an exception with the message "Cannot rollback!" if there's no version to roll back to.
Multiple calls to rollback() should be possible and restore the version history
release() - return a string in the format "{MAJOR}.{MINOR}.{PATCH}"
May the binary force be with you!
'''

class VersionManager:

    @classmethod
    def validate(cls, number):
        if 10 > number >= 0:
            return True
        else:
            raise TypeError('"Error occured while parsing version!" should be thrown')

    def __init__(self, MAJOR=0, MINOR=0, PATCH=1, *arg):
        if self.validate(MAJOR) and self.validate(MINOR) and self.validate(PATCH):
            self.MAJOR = MAJOR
            self.MINOR = MINOR
            self.PATCH = PATCH

    def major(self):
        self.MAJOR += 1
        self.MINOR = 0
        self.PATCH = 0

    def minor(self):
        self.MINOR += 1
        self.PATCH = 0

    def patch(self):
        self.PATCH += 1

# rollback() - вернуть MAJOR, MINOR и PATCH к их значениям до
# предыдущего основного/второстепенного/патч-вызова или создать исключение
# с сообщением "Cannot rollback!" если нет версии для отката.
# Должны быть возможны множественные вызовы rollback() и восстановление истории версий.

    #def rollback(self):
        #if self.MAJOR:

        #else:
            #if self.MAJOR == 0 and self.MINOR == 0 and self.PATCH == 1:
                #return 'Cannot rollback!'

    def release(self):
       return f'{self.MAJOR}.{self.MINOR}.{self.PATCH}'

v = VersionManager(1, 0, 0, 'd')
v.major()
print(v.release())
