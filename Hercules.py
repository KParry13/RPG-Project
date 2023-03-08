from Weapon import Weapon

class Hercules:
    def __init__(self) -> None:
        self.health = 100
        super().__init__()

    def weapon_choice(self):
        weapon = Weapon()
        print(weapon.attack_name)
        print("")
        attack = input("What will Hercules attack weapon be?\n").lower()
        print("")

        if attack == 'sword slice':
            print("Hercules chose sword slice!!")
        elif attack == 'martial arts move':
            print("Hercules chose martial arts move!!")
        elif attack == 'megapunch':
            print("Hercules chose megapunch!!")
        elif attack == 'megakick':
            print("Hercules chose megakick!!")
        else:
            print("Choose valid weapon")

    # weapon_choice(weapon_choice)

    def attack(self,enemies):
        pass
