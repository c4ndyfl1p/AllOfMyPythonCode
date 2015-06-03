def listWithinListPrinter(outerlist, *args, **kwargs):
	for innerlist in outerlist:
		for item in innerlist:
			print item
a = [2,3,4]
l = [1,a]
listWithinListPrinter(l)
