from character import Character


class Mermaid(Character):
    def __init__( self , name, strength, speed, health):
        super().__init__( self , name, strength, speed, health):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , mermaid ):
        frenchie.health -= self.strength
        bruiser.health -= self.strength
        print(self.strength)
        return self
    
    def sea_call():
        pass # adds strength
    
    def swim_fast():
        if health is < 30
            self.health += 50
            
    def back_slap():
        pass
             
    
ceto = Mermaid("Ceto", strength=21, speed = 20, health = 5000)

ceto.attack()
