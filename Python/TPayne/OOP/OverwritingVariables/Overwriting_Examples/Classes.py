from Base import BaseClass
        
class InClass(BaseClass):
    def __init__(self):
		super(InClass, self).__init__()
		self.x = 17

class InTwoClass(BaseClass):
    def printHam(self):
		print "Real ham"
		
f = InClass()
a = InTwoClass()
print f.x
a.printHam()
