from weapon import Weapon
import random

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Lightsaber', 50)

    def attack(self, dinosaur):
        attack_power = random.randrange(-1, 50)
        if attack_power >= 35:
            print("Critical Hit!")
        elif attack_power >= 20 and attack_power < 35:
            print("Moderate damage")
        elif attack_power < 20 and attack_power > 0:
            print("Minimal damage")
        else:
            print("MISS!!!")
        return attack_power
