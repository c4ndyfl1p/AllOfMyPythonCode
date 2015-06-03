from abc import ABCMeta, abstractmethod

class Enemy(object):
	__metaclass__=ABCMeta
	@abstractmethod
	def attackPlayer(self, player):
		pass
		
class EnvAsset(object):
	__metaclass__=ABCMeta
	@abstractmethod
	def __init__(self):
		self.mobile = False
		
class Trap(Enemy, EnvAsset):
	def __init__(self):
		super(Trap, self).__init__()
		
	def attackPlayer(self, player):
		return player.health - 10
		
x = Trap()
