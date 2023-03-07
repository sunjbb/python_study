from random import randint,choice

# print(randint(1, 3))
# print(choice([1,'a','n','mm']))

class Die:
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

die = Die(6)
print(die.roll_die())