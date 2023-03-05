'''
You are given a sequence of integers and you need to process it and display
the sum of the first five numbers from this sequence,
then the sum of the second five, and so on.

But the sequence is not given to you all at once. In the course of time,
successive parts of it come to you. For example, first the first three elements,
then the next six, then the next two, and so on.

Implement a Buffer class that will accumulate the elements of a sequence and
display the sum of fives of consecutive elements as they accumulate.

One of the requirements for the class is that it should not store more elements than it really needs,
i.e. it should not store elements that are already included in the five for which the sum was deduced.

The class should look like this

class Buffer:
     def __init__(self):
         # constructor with no arguments

     def add(self, *a):
         # add the next part of the sequence

     def get_current_part(self):
         # return the currently stored elements of the sequence in the order they were
         # added

An example of working with a class

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # return [1, 2, 3]
buf.add(4, 5, 6) # print(15) - print the sum of the first five elements
buf.get_current_part() # return [6]
buf.add(7, 8, 9, 10) # print(40) - print the sum of the second five elements
buf.get_current_part() # return []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) - print the sums of the third and fourth five
buf.get_current_part() # return [1]

Note that during the execution of the add method,
it may be necessary to print the sum of fives several times until there are fewer than five elements in the buffer.
'''

class Buffer:
    avalibility_buffer = []

    def __init__(self):
        pass

    def add(self, *a):
        self.avalibility_buffer += list(a)
        while len(self.avalibility_buffer) >= 5:
            first_five = self.avalibility_buffer[:5]
            del self.avalibility_buffer[:5]
            print(sum(first_five))

    def get_current_part(self):
        return self.avalibility_buffer



buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part()) # return [1, 2, 3]
print(buf.add(4, 5, 6)) # print(15) - print the sum of the first five elements
print(buf.get_current_part()) # return [6]
print(buf.add(7, 8, 9, 10)) # print(40) - print the sum of the second five elements
print(buf.get_current_part()) # return []
print(buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)) # print(5), print(5) - print the sums of the third and fourth five
print(buf.get_current_part()) # return [1]
