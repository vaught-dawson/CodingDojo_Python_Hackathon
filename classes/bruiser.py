import random
from classes.character import Character


class Bruiser(Character):

    def __init__(self, name):
        strength = random.randint(16, 24)
        speed = random.randint(8,16)
        health = random.randint(90, 120)
        super().__init__(name, strength, speed, health)

    def Info(self):
        print(f"******  {self.name}  ******")
        print(f"Health: {self.strength}")
        print(f"Speed: {self.speed}")
        print(f"Health: {self.health}")
        return self
