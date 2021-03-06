import random
from classes.character import Character


class Mermaid(Character):
    abilities = {}

    def __init__(self, name):
        strength = random.randint(20, 24)
        speed = random.randint(15, 23)
        health = random.randint(90, 150)
        super().__init__(name, strength, speed, health)
        if not self.abilities:
            self.add_abilities()
        self.class_name = 'Mermaid'

    def add_abilities(self):
        self.abilities['Sea Call'] = self.sea_call
        self.abilities['Shimmer'] = self.shimmer
        self.abilities['Tail Slap'] = self.tail_slap
        self.abilities['Basic Attack'] = self.attack

    def show_stats(self):
        print(
            f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self, victim):
        victim.class_name.health -= self.strength
        print(
            f"{self.name} hits you with a glorious back hand \n{victim.name} suffers {self.strength} of damage")
        return self

    def sea_call(self, victim):
        if self.health < 20:
            self.health += 50
        victim.class_name.health -= 30
        print(
            f"Poseidon blessed you with {self.health} points of health \nPoseidon: {victim.name} how dare you hurt my {self.name}! \n{victim.name} was dealt 30 points of damage")
        return self

    def shimmer(self, victim):
        if self.health < 10:
            self.speed += 80
        print(
            f"You shimmer like the sparkly ocean ;) {self.speed} points on speed!")
        return self

    def tail_slap(self, victim):
        if self.health <= 30:
            self.strength += 40
            victim.class_name.health -= self.strength
        print(f"{self.name} uses her glorious tail to slap {victim.name} on the face!")
        return self

    def Info(self):
        print(f"The one the only {self.name}")
        print(f"Health: {self.strength}")
        print(f"Speed: {self.speed}")
        print(f"Health: {self.health}")
        return self
