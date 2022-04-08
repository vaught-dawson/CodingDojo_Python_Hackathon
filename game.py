from classes.bruiser import Bruiser
from classes.frenchie import Frenchie
from classes.mermaid import Mermaid
from classes.enemy import Enemy
import math

# Game Functions ---------------------


def is_player_turn(turn):
    return turn % 2 == 1

# ------------------------------------


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
print(f'\nAn enemy {e1.class_name.class_name} has appeared!\n\"{player_name}. I, {e1.name}, will be the one to end you!\"\n*{e1.name} gets into their battle stance*')
still_alive = True
turn = 1
# Loop to do rounds (Unfinished)
while still_alive:
    if (is_player_turn(turn)):
        print('\nAbilities:')
        move = None
        # Loop to do check valid ability choice (Abilities are unfinished)
        while not move:
            for ability in player_object.abilities:
                print(f'- {ability}')
            input_ability = input('What ability would you like to use?\n')

            if player_object.abilities.get(input_ability) == None:
                print('\nInvalid move! The moves are CaSe-Sensitive.\nTry Again!\n')
                continue
            move = input_ability
            print(f'Chosen move: {move}\n')
            player_object.abilities[input_ability](e1)
    else:
        pass

    if not player_object.is_alive():
        print('You have died!')
        still_alive = False
    elif not e1.class_name.is_alive():
        print(f'You have bested {e1.name}!\nProceed to the next level.')
        still_alive = False
