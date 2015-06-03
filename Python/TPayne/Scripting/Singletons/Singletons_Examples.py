## Answer one: Created a class which returns a number +1 every time it's called

class addOne(object):
    _instance = None
    def __new__(self):
        if not self._instance:
            self._instance = super(addOne, self).__new__(self)
            self.value = 0
        self.value += 1
        return self.value

if __name__ == "__main__":
    print addOne()
    print addOne()
    print addOne()
    

##  Answer two:created a singleton which acts like a phone book. It has a function that you
## Can pass in a name and number to store, and another function to retrieve a Number
## given a name

def Singleton(myClass):
	instances = {}
	def GetInstance(*args, **kwargs):
		if myClass not in instances:
			instances[myClass] = myClass(*args, **kwargs)
		return instances[myClass]
	return GetInstance
'''
@singleton
class PhoneBook(object):
    book = {}
    def __init__(self):
        self.ask()
    def ask(self):
        print "what would you like to do ?"
        print "a = add a name and number"
        print "b = retrive  a  name and number"
        self.choice = raw_input("Please enter your choice: ")
        if self.choice == 'a':
            self.add()
        elif self.choice == 'b':
            self.retrive()
        else:
            print "Invalid Choice"
    def add(self):
        self.name = raw_input("Please enter the name: ")
        self.num = raw_input("Please enter the number: ")
        self.book[str(self.name)] = int(self.num)
    def retrive(self):
        namer = raw_input("Please enter the name: ")
        try:
            book[namer]
        except:
            print "Name Not Found"

a = PhoneBook()
'''

@Singleton
class PhoneBook(object):
	def __init__(self):
		self.myDict = {}
	def addEntery(self, name, number, *args, **kwargs):
		self.myDict[name] = number
	def getEntery(self, name, *args, **kwargs):
		if name in self.myDict.keys():
			return self.myDict[name]
		return '000-000-0000'


if __name__ == "__main__":
	pm = PhoneBook()
	pm.addEntery("me", "555-555-5555")
	pm2 = PhoneBook()
	print (pm2.getEntery('me'))
    
        
