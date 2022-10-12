import random

class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.attack_power = 0

    def attack(self, robot):
        self.attack_power = random.randrange(-1, 50)
        if self.attack_power > 40:
            self.attack_power = 50
            print("Critical Hit!")
            if self.health > 0:
                robot.health -= self.attack_power
                print(f"{self.name} attacks {robot.name} and reduces their health by {self.attack_power}")

        elif self.attack_power > 30 and self.attack_power <= 40:
            self.attack_power = 40
            print("Powerful Hit!")
            if self.health > 0:
                robot.health -= self.attack_power
                print(f"{self.name} attacks {robot.name} and reduces their health by {self.attack_power}")

        elif self.attack_power > 20 and self.attack_power <= 30:
            self.attack_power = 30
            print("Moderate damage.")
            if self.health > 0:
                robot.health -= self.attack_power
                print(f"{self.name} attacks {robot.name} and reduces their health by {self.attack_power}")

        elif self.attack_power > 10 and self.attack_power <= 20:
            self.attack_power = 20
            print("Weak hit, minimum damage...")
            if self.health > 0:
                robot.health -= self.attack_power
                print(f"{self.name} attacks {robot.name} and reduces their health by {self.attack_power}")

        else:
            self.attack_power = 0
            print("MISS!!!")
            if self.health > 0:
                robot.health -= self.attack_power
                print(f"{self.name} attacks {robot.name} and reduces their health by {self.attack_power}")