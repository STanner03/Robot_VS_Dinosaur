from weapon import Weapon
import random

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.active_weapon = ''

    def attack(self, dinosaur):
        if self.health > 0:
            self.active_weapon = Weapon.weapons_choice(Weapon)
            dinosaur.health -= self.active_weapon.attack_power
            print(f"{self.name} attacks {dinosaur.name} and reduces their health by {self.active_weapon.attack_power}")
            return self.active_weapon.attack_power