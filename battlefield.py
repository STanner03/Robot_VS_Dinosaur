import random
from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot('C-3PO')
        self.dinosaur = Dinosaur('T-Rex', 50)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()


    def display_welcome(self):
        print(f"Welcome to the battle between {self.robot.name} and {self.dinosaur.name}!\nWho will be VICTORIOUS?")

    def battle_phase(self):
        # dinosaur_health = self.dinosaur.health
        # robot_health = self.robot.health
        while self.robot.health > 0 and self.dinosaur.health > 0:
            
            attack_power = Robot.attack(Robot, self.dinosaur, Robot.weapons_choice(self))
            self.dinosaur.health -= attack_power
            print(f"{self.robot.name} attacks {self.dinosaur.name} and reduces their health by {attack_power}.\n{self.dinosaur.name}'s health is now, {self.dinosaur.health}!")
            if self.dinosaur.health < 50 and self.dinosaur.health > 10:
                print('Health is below 50%!')
            elif self.dinosaur.health < 10 and self.dinosaur.health > 0:
                print('Health is below 10%,\nFINISH THIS!!!')
            elif self.dinosaur.health <= 0:
                break

            attack_power = Dinosaur.attack(Dinosaur, self.robot)
            self.robot.health -= attack_power
            print(f"{self.dinosaur.name} attacks {self.robot.name} and reduces their health by {attack_power}.\n{self.robot.name}'s health is now, {self.robot.health}!")
            if self.robot.health < 50 and self.robot.health > 10:
                print('Health is below 50%!')
            elif self.robot.health < 10 and self.robot.health > 0:
                print('Health is below 10%,\nFINISH THIS!!!')
            elif self.robot.health <= 0:
                break

    def display_winner(self):
        if self.robot.health > self.dinosaur.health:
            print(f"{self.robot.name} is VICTORIOUS!!!\n{self.dinosaur.name} is extinct!")
        if self.dinosaur.health > self.robot.health:
            print(f"{self.dinosaur.name} is VICTORIOUS!!!\nMay {self.robot.name} rust in peace!")
