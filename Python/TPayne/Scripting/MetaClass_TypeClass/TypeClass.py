#!/usr/bin/env python2

# what is type class creation...
# Creating a different way of creating short classes
# Old way was:
#
#class MyClass(object):
#   def __init__(self):
#       print "This is my class"
#       print "This guy loves ham"
#
#x = MyClass()
#

def printHam(self):
    print 'ham'

TypeClass = type("TypeClass", (object,), {"x":5, "pH":printHam})

t = TypeClass()
print t.x
t.pH()
