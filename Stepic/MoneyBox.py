'''
Implement the MoneyBox class to work with a virtual piggy bank.

Each piggy bank has a limited capacity, which is expressed as an integer - the number of coins that can be put into the piggy bank. The class should maintain information about the number of coins in the piggy bank, provide the ability to add coins to the piggy bank, and find out if it is possible to add some more coins to the piggy bank without exceeding its capacity.

The class should look like this

class MoneyBox:
     def __init__(self, capacity):
# constructor with argument - piggy bank capacity

     def can_add(self, v):
         # True if v coins can be added, False otherwise

     def add(self, v):
         # put v coins into the piggy bank
When creating a piggy bank, the number of coins in it is 0.
Note:
It is guaranteed that the add(self, v) method will only be called if can_add(self, v) is True﻿.
'''


class MoneyBox:
    def __init__(self, capacity):
        self.balance = 0
        self.capacity = capacity

    def can_add(self, v):
        return self.balance + v <= self.capacity
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        if self.can_add(v):
            self.balance = self.balance + v
            return self.balance
box = MoneyBox(50)
box.add(20)
print(box.capacity)
print(box.can_add(30))
