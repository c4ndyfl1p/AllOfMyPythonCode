def Func(*args, **kwargs):
	for arg in args:
		print arg
	for item in kwargs.items():
		print item
			
Func(x = 456, y = 3)
