def addSandwich(func):
	def addit(*args, **kwargs):
		return func() + ' sandwich'
	return addit
	
@addSandwich	
def returnHam(x = 'ham'):
	return x

print returnHam()
