import random
from classes.character import Character


class Frenchie(Character):

    def __init__(self, name):
        strength = random.randint(8, 16)
        speed = random.randint(18, 24)
        health = random.randint(80, 120)
        super().__init__(name, strength, speed, health)

    def Info(self):
        print(f"***** (self.name) *****")
        print(f"Health: (self.strength)")
        print(f"Speed: (self.speed")
        return self
