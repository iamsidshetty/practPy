__author__ = 'sid'

# Simple class

# class SimpleClass:
#     pass
#
# p = SimpleClass()
# print p

class Greeting:
    def __init__(self, name):
        self.name = name
    def SayHi(self):
        print "My name is " + self.name
        print "Hello ji, How are you?"



s = Greeting('Sudarshan')
s.SayHi()