from Hercules import Hercules
from Enemies import Enemies

class Battlefield:
    def __init__(self):
        self.hercules = Hercules()
        self.enemies = Enemies()

    def run_game(self):
        self.welcome()
        self.battle()
        self.winner()

    def welcome(self):
        print("Welcome to the battle of the Otherworld!\n Hercules is said to be undefeatable so we are going to put him to the test!")
        print("Going up against three of his foes: Nemean, Hydra, and Cerberus, we will see if he can survive!")
        print("Or will the power of his foes be too much!\n Let the battle...BEGIN!!!")
        print("")

    def battle(self):
        while self.hercules.health > 0 and self.enemies.health > 0:
            self.hercules.attack(self.enemies)
            self.enemies.attack(self.hercules)
            print("")
            if self.hercules.health >= self.enemies.health:
                print('Take that you crazy bat!')
                print("")
            else:
                print('What a hit!')
                print("")


    def winner(self):
        if self.hercules.health > self.enemies.health:
            print("Hercules is still undefeated!")
        else:
            print("The Enemies with gathered force defeated the almighty Hercules!")
