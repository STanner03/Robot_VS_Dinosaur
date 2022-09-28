import random
from herd import Herd
from fleet import Fleet
from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Fleet()
        self.dinosaur = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()


    def display_welcome(self):
        print(f"Welcome to the battle between Robots '{self.robot.robots_list[0].name}, {self.robot.robots_list[1].name}, and {self.robot.robots_list[2].name}' \nand Dinosaurs '{self.dinosaur.dinosaurs_list[0].name}, {self.dinosaur.dinosaurs_list[1].name}, and {self.dinosaur.dinosaurs_list[2].name}'!\nWho will be VICTORIOUS?")

    def battle_phase(self):
        coin_flip = random.randrange(0, 2)
        while self.robot.fleet_health > 0 and self.dinosaur.dinosaur_health > 0:
            if coin_flip == 0:
                hit_points = 0
                hp = int(self.robot.robots_list[0].active_weapon.attack_power * random.randrange(-1, 110) / 100)
                hit_points += hp
                print(f"{self.robot.robots_list[0].name}'s attack adds {hp} damage")
                hp = int(self.robot.robots_list[1].active_weapon.attack_power * random.randrange(-5, 110) / 100)
                hit_points += hp
                print(f"{self.robot.robots_list[1].name}'s attack adds {hp} damage")
                hp = int(self.robot.robots_list[2].active_weapon.attack_power * random.randrange(-10, 110) / 100)
                hit_points += hp
                print(f"{self.robot.robots_list[2].name}'s attack adds {hp} damage\n ")
                self.dinosaur.dinosaur_health -= hit_points
                print(f"The Robots attack the Dinosaurs and reduces their health by {hit_points}.\n\nDinosaurs' health is now, {self.dinosaur.dinosaur_health}!\n ")
                if self.dinosaur.dinosaur_health < 150 and self.dinosaur.dinosaur_health >= 30:
                    print('Health is below 50 %!')
                elif self.dinosaur.dinosaur_health < 30 and self.dinosaur.dinosaur_health > 0:
                    print('Health is below 10 %,\nFINISH THIS!!!')
                elif self.dinosaur.dinosaur_health <= 0:
                    break
                coin_flip = 1

            if coin_flip == 1:    
                attack_power = 0
                ap = int(self.dinosaur.dinosaurs_list[0].attack_power * random.randrange(-1, 110) / 100)
                attack_power += ap
                print(f"{self.dinosaur.dinosaurs_list[0].name}'s attack adds {ap} damage")
                ap = int(self.dinosaur.dinosaurs_list[1].attack_power * random.randrange(-5, 110) / 100)
                attack_power += ap
                print(f"{self.dinosaur.dinosaurs_list[1].name}'s attack adds {ap} damage")
                ap = int(self.dinosaur.dinosaurs_list[2].attack_power * random.randrange(-10, 110) / 100)
                attack_power += ap
                print(f"{self.dinosaur.dinosaurs_list[2].name}'s attack adds {ap} damage")
                self.robot.fleet_health -= attack_power
                print(f"\nDinosaurs attack Robots and reduces their health by {attack_power}.\n\nRobots' health is now, {self.robot.fleet_health}!\n ")
                if self.robot.fleet_health < 150 and self.robot.fleet_health >= 30:
                    print('Health is below 50 %!')
                elif self.robot.fleet_health < 30 and self.robot.fleet_health > 0:
                    print('Health is below 10 %,\nFINISH THIS!!!')
                elif self.robot.fleet_health <= 0:
                    break
                coin_flip = 0

    def display_winner(self):
        if self.robot.fleet_health > self.dinosaur.dinosaur_health:
            print(f"Robots are VICTORIOUS!!!\nDinosaurs have become extinct!")
        if self.dinosaur.dinosaur_health > self.robot.fleet_health:
            print(f"Dinosaurs are VICTORIOUS!!!\nMay Robots rust in peace!")
