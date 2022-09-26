from weapon import Weapon
import random

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Laser Beam', range(-1, 31))

    def attack(self, dinosaur):
        dinosaur.health - self.active_weapon.attack_power
        if self.active_weapon.attack_power >= 20:
            print("Critical Hit!")
        elif self.active_weapon.attack_power >= 10 and self.active_weapon.attack_power < 20:
            print("Moderate damage")
        elif self.active_weapon.attack_power < 10 and self.active_weapon.attack_power < 0:
            print("Minimal damage")
        else:
            print("MISS!!!")

        print(f"{self.name} attacks {dinosaur} with {self.active_weapon.name} and reduces their health by {self.active_weapon.attack_power}")