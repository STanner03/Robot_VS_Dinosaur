import random

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def attack(self, robot):
        attack_power = random.randrange(-1, 50)
        if attack_power > 40:
            attack_power = 50
            print("Critical Hit!")
        elif attack_power > 20 and attack_power <= 40:
            attack_power = 35
            print("Moderate damage")
        elif attack_power <= 20 and attack_power > 10:
            attack_power = 25
            print("Minimal damage")
        elif attack_power <= 10 and attack_power > 5:
            attack_power = 10
        else:
            attack_power = 0
            print("MISS!!!")

        return attack_power
