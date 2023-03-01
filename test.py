
a = dict()



class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def all_money(self):
        return self.fives + self.tens + self.twenties

phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)

def most_money(students):
    finish = dict()
    money = dict()
    for i in students:
        all_money = i.fives * 5 + i.tens * 10 + i.twenties * 20
        money[i.name] = all_money
    money = sorted(money.values(), reverse=True)

    x = 0
    y = 1
    while money[x] == money[y]:
        finish[]



    print(money)
    #for i in money.values():
     #   if i > 0:
      #      a = i

    #return print(sorted(money.values()))

print(most_money([phil, cam, geoff]))




