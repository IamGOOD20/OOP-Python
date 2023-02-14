'''Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"'''

from random import choice

class Ghost:
      def __init__(self):
            colors = ['white', 'yellow', 'purple', 'red']
            self.color = choice(colors)

      def color(self):
            return self.color

Casper = Ghost()
#print(Casper.color)
print(Casper.__dict__)