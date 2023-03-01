
import heapq

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def all_money(self):
        return self.fives + self.tens + self.twenties

phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 1)
geoff = Student("Geoff", 0, 3, 0)


def most_money(students):
    money = dict()
    for i in students:
        all_money = i.fives * 5 + i.tens * 10 + i.twenties * 20
        money[i.name] = all_money
    max_value = max(money.values())
    finish = [key for key, value in money.items() if value == max_value]
    if len(finish) > 1:
        return 'all'
    else:
        return ', '.join(finish)
print(most_money([cam, phil]))


'''
def most_money(students):
    money = dict()
    for i in students:
        all_money = i.fives * 5 + i.tens * 10 + i.twenties * 20
        money[i.name] = all_money
    print(money)
'''