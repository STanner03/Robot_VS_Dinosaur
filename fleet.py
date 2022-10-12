from robot import Robot
from weapon import Weapon
import random

class Fleet:
    def __init__(self):
        self.robots_list = self.robots()
        self.fleet_health = self.robots_list[0].health  + self.robots_list[1].health + self.robots_list[2].health

    def robots(self):
        self.robots_list = []
        c_3po = Robot('C-3PO')
        self.robots_list.append(c_3po)
        d_a_r_y_l = Robot('D.A.R.Y.L.')
        self.robots_list.append(d_a_r_y_l)
        robo_cop = Robot('Robo Cop')
        self.robots_list.append(robo_cop)
        return self.robots_list

    def attack(self):
        hit_points = 0
        self.robot.robots_list[0].active_weapon = Weapon.weapons_choice(Weapon)
        hp = int(self.robot.robots_list[0].active_weapon.attack_power * random.randrange(70, 170) / 100)
        hit_points += hp
        print(f"{self.robot.robots_list[0].name}'s attack adds {hp} damage")
        self.robot.robots_list[1].active_weapon = Weapon.weapons_choice(Weapon)
        hp = int(self.robot.robots_list[1].active_weapon.attack_power * random.randrange(55, 155) / 100)
        hit_points += hp
        print(f"{self.robot.robots_list[1].name}'s attack adds {hp} damage")
        self.robot.robots_list[2].active_weapon = Weapon.weapons_choice(Weapon)
        hp = int(self.robot.robots_list[2].active_weapon.attack_power * random.randrange(50, 140) / 100)
        hit_points += hp
        print(f"{self.robot.robots_list[2].name}'s attack adds {hp} damage\n ")
        return hit_points