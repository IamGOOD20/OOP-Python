'''
Implement a data structure that is an extended stack structure. It is necessary to support adding an element to the top of the stack, removing from the top of the stack, and it is necessary to support the operations of addition, subtraction, multiplication, and integer division.

The addition operation on the stack is defined as follows. The top element (top1) is removed from the stack, then the next top element (top2) is removed, and then the element equal to top1 + top2 is put on top of the stack as a result of the addition operation.

The operations of subtraction (top1 - top2), multiplication (top1 * top2), and integer division (top1 // top2) are defined similarly.

Implement this data structure as an ExtendedStack class, deriving from the standard list class.
Required class structure:

class ExtendedStack(list):
     defsum(self):
         # addition operation

     def sub(self):
         # subtraction operation

     def mul(self):
         # multiplication operation

     defdiv(self):
         # integer division operation

Note
To add an element to the stack, use the append method, and to remove it from the stack, use the pop method.
It is guaranteed that operations will be performed only when there are at least two elements on the stack.
'''


class ExtendedStack(list):
    def sum(self):
        return self.append(self.pop() + self.pop())

    def sub(self):
        return self.append(self.pop() - self.pop())

    def mul(self):
        return self.append(self.pop() * self.pop())

    def div(self):
        return self.append(self.pop() // self.pop())
