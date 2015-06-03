def Func(*args):
	for arg in args:
		print arg
l = [1,2,3,4,"ham"]		
Func(l)
Func(*l)
