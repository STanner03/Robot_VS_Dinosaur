import random
from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot('R2 D2')
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
            
            attack_power = Robot.attack(Robot, self.dinosaur)
            self.dinosaur.health -= attack_power
            print(f"{self.robot.name} attacks {self.dinosaur.name} and reduces their health by {attack_power}")
            
            attack_power = Dinosaur.attack(Dinosaur, self.robot)
            self.robot.health -= attack_power
            print(f"{self.dinosaur.name} attacks {self.robot.name} and reduces their health by {attack_power}")
        

    def display_winner(self):
        if self.robot.health > self.dinosaur.health:
            print(f"{self.robot.name} is VICTORIOUS!!!")
        if self.dinosaur.health > self.robot.health:
            print(f"{self.dinosaur.name} is VICTORIOUS!!!")
