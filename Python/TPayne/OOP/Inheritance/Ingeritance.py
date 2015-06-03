class Character(object):
    def __init__(self, name):
        self.health = 100
        self.name = name
    def printName(self):
        print self.name
        
class BlackSmith(Character):
    def __init__(self, name, forgeName):
        super(BlackSmith, self).__init__(name)
        self.forge = Forge(forgeName)

class Forge:
    def __init__(self, forgeName):
        self.name = forgeName

bs = BlackSmith('Bob', 'Rick\'s forge')
bs.printName()
print bs.forge.name
print bs.health
