from classes.bruiser import Bruiser
from classes.frenchie import Frenchie
from classes.mermaid import Mermaid
from classes.enemy import Enemy

print("Welcome to the Dojo, fight different members to prove your strength!")
# Get player name as an input
player_name = input("Enter your name: ")
player_object = None

# Get a valid class option from the player as an input
is_invalid_class = True
player_class = ''
while is_invalid_class:
    print("\nClasses-\n1. Bruiser\n2. Frenchie\n3. Mermaid\n")
    player_class = input("Enter your chosen class: ")

    match player_class.lower():
        case '1':
            player_object = Bruiser(player_name)
            is_invalid_class = False
        case '2':
            player_object = Frenchie(player_name)
            is_invalid_class = False
        case '3':
            player_object = Mermaid(player_name)
            is_invalid_class = False
        case 'bruiser':
            player_object = Bruiser(player_name)
            is_invalid_class = False
        case 'frenchie':
            player_object = Frenchie(player_name)
            is_invalid_class = False
        case 'mermaid':
            player_object = Mermaid(player_name)
            is_invalid_class = False
        case _:
            print('Please enter a valid class name or number!')

e1 = Enemy()

print(f'Enemy {e1.name} has appeared!')
still_alive = True
# Loop to do rounds (Unfinished)
while still_alive:
    print('Abilities:')
    invalid_move = True
    # Loop to do check valid ability choice (Abilities are unfinished)
    while invalid_move:
        abilities = player_object.abilities
        for ability in abilities:
            print(f'- {ability}')
        input_ability = input('What ability would you like to use?\n')
        if abilities.get(input_ability) != None:
            player_object.all_abilities[input_ability](e1)
            invalid_move = False
