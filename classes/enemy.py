import random
from classes.bruiser import Bruiser
from classes.frenchie import Frenchie
from classes.mermaid import Mermaid


class Enemy:
    def __init__(self):
        self.name = self.get_random_name()
        rand_class = self.choose_random_class()
        self.class_name = rand_class(self.name)

    def show_self(self):
        return self

    @staticmethod
    def get_random_name():
        names = ['Akibrus',
                 'Angun',
                 'Balrus',
                 'Bulruk',
                 'Caldor',
                 'Dagen',
                 'Darvyn',
                 'Delvin',
                 'Dracyian',
                 'Dray',
                 'Eldar',
                 'Engar',
                 'Fabien',
                 'Farkas',
                 'Galdor',
                 'Igor',
                 'Jai-Blynn',
                 'Klayden',
                 'Laimus',
                 'Malfas',
                 'Norok',
                 'Orion',
                 'Pindious',
                 'Quintus',
                 'Rammir',
                 'Remus',
                 'Rorik',
                 'Sabir',
                 'Séverin',
                 'Sirius',
                 'Soril',
                 'Sulfu',
                 'Syfas',
                 'Viktas',
                 'Vyn',
                 'Wilkass',
                 'Yagul',
                 'Zakkas',
                 'Zarek',
                 'Zorion']
        return names[random.randint(0, len(names) - 1)]

    @staticmethod
    def choose_random_class():
        classes = [Bruiser, Frenchie, Mermaid]
        return classes[random.randint(0, len(classes) - 1)]
