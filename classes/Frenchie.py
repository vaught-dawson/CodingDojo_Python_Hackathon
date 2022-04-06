import random
from classes.character import Character


class Frenchie(Character):

    def __init__(self, name):
        strength = random.randint(8, 16)
        speed = random.randint(18, 24)
        health = random.randint(80, 120)
        super().__init__(name, strength, speed, health)
        self.all_abilities['Lick to Death'] = self.lick_to_death
        self.all_abilities['Fart Cloud'] = self.fart_cloud
        self.all_abilities['Zoomies'] = self.zoomies
        self.all_abilities['Bite Leg Off'] = self.bite_leg_off

    def info(self):
        print(f"***** (self.name) *****")
        print(f"Health: (self.strength)")
        print(f"Speed: (self.speed")
        return self

    def lick_to_death(self, victim):
        print(f"{self.name} use lick to death {victim.name}!")
        self.attack(victim)

    def fart_cloud(self, victim):
        print(f"{self.name} use fart cloud on {victim.name}")
        self.attack(victim)

    def zoomies(self, victim):
        print(f"{self.name} use zoomies on {victim.name}")
        self.attack(victim)

    def bite_leg_off(self, victim):
        print(f"{self.name} use bite leg off on {victim.name}")
        self.attack(victim)
