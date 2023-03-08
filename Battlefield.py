from Hercules import Hercules
from Enemies import Enemies

class Battlefield:
    def __init__(self):
        self.hercules = Hercules()
        self.enemies = Enemies()

    def run_game(self):
        self.welcome()

    def welcome(self):
        pass

    def attack(self):
        pass

    def winner(self):
        pass
