from character import Character


class Mermaid(Character):
    def __init__( self , name, strength, speed, health):
        super().__init__(name, strength, speed, health)
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , victim ):
        victim.health -= self.strength
        print(self.strength)
        return self
    
    def sea_call(self):
        if self.health < 20:
            self.health += 50
        return self
    
    def swim_fast(self):
        if self.health < 10:
            self.speed += 80
        return self

            
    def back_slap(self, victim):
        if self.health <= 30:
            self.strength += 40
            victim.health -= self.strength
        return self
            

    def Info(self):
        print(f"The one the only {self.name}")
        print(f"Health: {self.strength}")
        print(f"Speed: {self.speed}")
        print(f"Health: {self.health}")
        return self
    
ceto = Mermaid("Ceto", strength=21, speed = 20, health = 100)
