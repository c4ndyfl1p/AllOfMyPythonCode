class Hero:
    """
        A hero is allergic to Appels
    """
    def __init__(self, name):
        """
        Whatever we want
        """
        self.name = name
        self.health = 100
    def eat(self, food):
        if(food == 'apple'):
            self.health -= 100
        elif(food == 'ham'):
            self.health += 20
            
Bob = Hero("Bob")
print Bob.name
print Bob.health
Bob.eat("ham")
print Bob.health
