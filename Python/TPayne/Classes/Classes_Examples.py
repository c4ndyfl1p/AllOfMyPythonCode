class Ham:
    def __init__(self):
        self.name = 'ham'
        self.healthBonus = 10
class Hero:
    def __init__(self):
        self.health = 100
    def eat(self, food):
        self.health += food.healthBonus

Bob = Hero()
ham = Ham()
Bob.eat(ham)
print Bob.health
