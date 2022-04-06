class Mermaid:

    def __init__( self , name, strength = 30, speed = 5, health = 100 ):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , nereid ):
        ninja.health -= self.strength
        pirate.health -= self.strength
        print(self.strength)
        return self
    
    def sea_call( self, nereid):
        pass # adds strength
    
    def swim_fast():
        pass # boosts up speed 
    
ceto = Mermaid("Ceto", strength=50, health = 200)

ceto.attack()
