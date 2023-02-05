'''Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.

If no arguments are given, ball objects should instantiate with a "ball type" of "regular."'''

# 1
class Ball(object):
    def __init__(self, *args):
        self.ball_type = 'regular'
        if args:
            self.ball_type = args[0]

ball1 = Ball()
print(ball1.ball_type)
print(ball1.__dict__)
ball2 = Ball(input())
print(ball2.ball_type)

# 2
class Ball:
      def __init__(self, ball_type=None):
            self.ball_type = 'regular'

ball3 = Ball()
print(ball3.ball_type)
print(ball3.__dict__)

ball4 = Ball('Large')
print(ball4.__dict__)

ball5 = Ball('super')
print(ball5)
print(ball5.__dict__)
