from string import ascii_letters

class Personal:
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        #self.verify_old(old)
        #self.verify_weight(weight)
        #self.verify_ps(ps)

        self.__fio = fio.split()
        #self.__old = old
        #self.__ps = ps
        #self.__weight = weight

        self.old = old
        self.ps = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('Fio must be an str!')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('Not correct format')

        letters = ascii_letters
        for w in f:
            if len(w) < 1:
                raise TypeError('Must be minimum 1 symbol')
            if len(w.strip(letters)) != 0:
                raise TypeError('Must be only letters or hyphens')

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError('Old must have type int and old must be between 14 and 120')


    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError('Weight must have float type and cant be 20 less')

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('Ps must be a string')

        p = ps.split()
        if len(p) != 2 or len(p[0]) != 4 or len(p[1]) != 6:
            raise TypeError('Wrong ps format1')

        for _ in p:
            if not _.isdigit():
                raise TypeError('Wrong ps format2')

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def ps(self):
        return self.ps

    @ps.setter
    def ps(self, ps):
        self.verify_ps(ps)
        self.__ps = ps

ruk = Personal('Ruskhenas Eugene Leonasovitch', 33, '1234 567890', 90.00)

ruk.old = 60
ruk.weight = 80.00
ruk.ps = '0987 654321'

print(ruk.__dict__)
