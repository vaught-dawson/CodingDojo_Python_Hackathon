import math
import random


class Character:
    all_abilities = {}

    def __init__(self, name, strength, speed, health):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health

    def show_stats(self):
        print(
            f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        return self

    def change_health(self, amount):
        self.health += amount
        return self

    def attack(self, victim):
        attack_roll = Character.roll_d20() + self.get_stat_bonus(self.speed)
        defense_roll = Character.roll_d20() + victim.get_stat_bonus(victim.speed)
        print(f'{self.name} attacks {victim.name}')
        if attack_roll > defense_roll:
            print(
                f'{self.name}\'s attack of {attack_roll} beats {victim.name}\'s defense of {defense_roll}')
            damage = Character.roll_d20() + self.get_stat_bonus(self.strength)
            victim.change_health(-damage)
            print(
                f'{victim.name} takes {damage} damage! {victim.health} health remaining')
        else:
            print(
                f'{victim.name} wards off the attack from {self.name}! ({attack_roll} attack vs {defense_roll} defense)')
        return self

    @staticmethod
    def get_stat_bonus(stat):
        return math.floor(stat / 5)

    @staticmethod
    def roll_d20():
        return random.randint(1, 20)

    @classmethod
    def display_all_characters(cls):
        for character in cls.all_characters:
            character.show_stats()
