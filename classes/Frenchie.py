from classes.character import Character


class Frenchie(Character):

    def __init__(self, name, strength, speed, health):
        super().__init__(name, strength, speed, health)

    def Info(self):
        print(f"***** (self.name) *****")
        print(f"Health: (self.strength)")
        print(f"Speed: (self.speed")
        return self
