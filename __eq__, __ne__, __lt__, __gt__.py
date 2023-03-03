class Clock:
    __DAY = 86400 # sec in one day

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Seconds must be integer')
        self.seconds = seconds % self.__DAY


    def __eq__(self, other): # ==; !=
        if not isinstance(other, (int, Clock)):
            raise TypeError('Right operator must be int or Clock')

        sc = other if isinstance(other, int) else other.seconds
        return self.seconds == sc


    def __lt__(self, other): # < >
        if not isinstance(other, (int, Clock)):
            raise TypeError('Right operator must be int or Clock')

        sc = other if isinstance(other, int) else other.seconds
        return self.seconds < sc

c1 = Clock(1000)
c2 = Clock(2000)
print(c1 != c2)
