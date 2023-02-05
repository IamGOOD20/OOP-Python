class Point:
      color = 'red'
      circle = 2


      def __init__(self, x, y):
            print('init')
            self.x = x
            self.y = y

      def __del__(self):
            print('Deleted' + str(self))

      def set_corts(self, x, y):
            self.x = x
            self.y = y


      def get_corts(self):
            return self.x, self.y


yo = Point(10, 20)
print(yo.__dict__)
# print(yo.__doc__)