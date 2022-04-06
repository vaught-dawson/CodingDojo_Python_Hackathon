from classes.bruiser import Bruiser
from classes.frenchie import Frenchie
from classes.mermaid import Mermaid

print("Welcome to the Dojo, fight different members to prove your strength!")
player_name = input("Enter your name: ")
player_object = None

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

player_object.show_stats()
