import random
from Weapon import Weapon

class Enemies(Weapon):
    def __init__(self) -> None:
        self.health = 100
        super().__init__()

    def attack(self, hercules):
        pass