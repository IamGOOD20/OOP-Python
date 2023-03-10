'''
One use of multiple inheritance is to extend the functionality of a class in some predetermined way. For example,
if we need to log some information when accessing class methods.

Consider the Loggable class:

import time

class Loggable:
     def log(self, msg):
         print(str(time.ctime()) + ": " + str(msg))
It has exactly one log method, which allows you to output some message to the log (in this case, to stdout),
while adding the current time.
Implement the LoggableList class by deriving it from the list and Loggable classes so that when an element is added
to the list using the append method, a message consisting of the newly added element is sent to the log.

Note
Your program must not contain the Loggable class. When checked, this class will be available to your program,
and it will contain the log method described above.
'''

class LoggableList(list, Loggable):
    def append(self, x):
        list.append(self, x)
        self.log(x)
