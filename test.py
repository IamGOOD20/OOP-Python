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
        # положить v монет в копилку


box = MoneyBox(50)
#print(box.capacity)
#print(box.can_add(60))

box.add(20)
print(box.capacity)

print(box.can_add(30))