from abc import ABCMeta, abstractmethod

class BaseClass(object):
	__metaclass__=ABCMeta
	#Now for the abstract functions
	@abstractmethod
	def printHam(self):
		pass
		
class InClass(BaseClass):
	def printHam(self):
		print "Ham"
		
x = InClass()
x.printHam()
