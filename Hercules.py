from Weapon import Weapon

class Hercules:
    def __init__(self) -> None:
        self.health = 100
        super().__init__()

    def weapon_choice(self):
        print(Weapon.attack_name)
        attack = input("What will Hercules attack weapon be?")
        print(attack)

    weapon_choice()

    def attack(self,enemies):
        pass
