import random

weapon_info = {
            'weapon_name': ['sword slice', 'martial arts move', 'megapunch', 'megakick']
        }

class Weapon:
    def __init__(self) -> None:
        self.attack_name = (weapon_info["weapon_name"])
        self.attack_power = random.choice(range(10,25))
        