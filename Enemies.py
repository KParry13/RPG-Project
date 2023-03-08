import random
from Weapon import Weapon

class Enemies(Weapon):
    def __init__(self) -> None:
        self.name = ['Nemean', 'Hydra', 'Cerberus']
        self.health = 100
        super().__init__()

    def attack(self, hercules):
        weapon = Weapon()
        random.choice(weapon.attack_name)
        hercules.health -= .attack_power
        name = random.choice(self.name)
        print(f"{name} uses their {weapon} and does damage of {Weapon.attack_power}!")
        print(f"Hercules health is down to {hercules.health}!")

    
    