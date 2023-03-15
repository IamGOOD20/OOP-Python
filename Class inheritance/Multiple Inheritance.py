class Goods:
    def __init__(self, name, weight, price):
        # 1.1:
        super().__init__() # used init of MixinLog class
        print('init Gods')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class MixinLog:
    ID = 0

    def __init__(self):
        super().__init__()
        print('Init MixinLog')
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f'{self.id}: solded at 00:00')


class MixinLog2:
    def __init__(self):
        print('Init MixinLog2')

class NoteBook(Goods, MixinLog, MixinLog2):
    pass

n = NoteBook('Aser', 1.5, 30000)
n.print_info()
n.save_sell_log()

# 1 - error AttributeError: 'NoteBook' object has no attribute 'id'
    # solutions: super().__init__() 1.1

print(NoteBook.__mro__) # shows the chain of inheritance
# Init MixinLog2
# Init MixinLog
# init Gods
# Aser, 1.5, 30000
# 1: solded at 00:00
# (<class '__main__.NoteBook'>, <class '__main__.Goods'>, <class '__main__.MixinLog'>, <class '__main__.MixinLog2'>, <class 'object'>)
