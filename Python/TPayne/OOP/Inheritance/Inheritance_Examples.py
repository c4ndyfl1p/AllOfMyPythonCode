class Base(object):
    def __init__(self):
        print self.name

class NPC(object, Base):
    pass
class Friendly(NPC):
    pass
class Enemy(NPC):
    def __init__(self):
        self.attackDamage = 5

class PC(object, Base):
    def __init__(self):
        self.weapon = 'gun'
class Archer(PC):
    pass
class Butcher(PC):
    pass
class GreenLantern(PC):
    pass

class Weapon(object):
    def weapon(self, weapon):
        self.weapon = 'gun'
