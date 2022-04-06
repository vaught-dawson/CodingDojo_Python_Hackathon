import random
from classes.character import Character


class Bruiser(Character):

    def __init__(self, name):
        strength = random.randint(16, 24)
        speed = random.randint(16,20)
        health = random.randint(90, 120)
        super().__init__(name, strength, speed, health)

    def info(self):
        print(f"******  {self.name}  ******")
        print(f"Health: {self.strength}")
        print(f"Speed: {self.speed}")
        print(f"Health: {self.health}")
        return self

    def body_slam(self, victim):
        print(f'{self.name} used body slam on {victim.name}!')
        self.attack(victim)

    def heavy_fist (self, victim):
        print(f'{self.name} uses a heavy fist on {victim.name}')
        increased_strength = Character.roll_d20()
        self.strength += increased_strength
        print(f'(Increased attack strength my {increased_strength} for this turn)')
        self.attack(victim)
        self.strength -= increased_strength

    def attitude_adjustment(self, victim):
        print(f'{self.name} used attitude adjustment on {victim.name}')

    def blood_thirsty(self, victim):
        print(f'{self.name} used bloodthirsty on {victim.name}')


