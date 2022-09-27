from weapon import Weapon
import random

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = ''

    def weapons_choice(self):
        weapons = []
        lightsaber = Weapon('Lightsaber', 30)
        weapons.append(lightsaber)
        lazer_cannon = Weapon('Lazer Cannon', 35)
        weapons.append(lazer_cannon)
        satellite_beam = Weapon('Satellite Beam', 40)
        weapons.append(satellite_beam)
        answer = input('What weapon do you choose? \nA) Lightsaber \nB) Lazer Cannon \nC) Satellite Beam \nA, B, or C? ')
        if answer == 'A' or answer == 'a' or answer == 'lightsaber' or answer == 'Lightsaber':
            answer = weapons[0]
        elif answer == 'B' or answer == 'b' or answer == 'lazer cannon' or answer == 'Lazer Cannon':
            answer = weapons[1]
        elif answer == 'C' or answer == 'c' or answer == 'satellite beam' or answer == 'Satellite Beam':
            answer = weapons[2]
        return answer


    def attack(self, dinosaur, answer):
        if answer.name == 'Lightsaber':
            attack_power = answer.attack_power + random.randrange(-30, 10)
            if attack_power >= 35:
                attack_power = 40
                print("Critical Hit!")
            elif attack_power >= 25 and attack_power < 35:
                attack_power = 30
                print("Moderate damage")
            elif attack_power > 10 and attack_power < 25:
                attack_power = 20
                print("Minimal damage")
            else:
                attack_power = 0
                print("MISS!!!")

        if answer.name == 'Lazer Cannon':
            attack_power = answer.attack_power + random.randrange(-35, 15)
            if attack_power >= 40:
                attack_power = 45
                print("Critical Hit!")
            elif attack_power >= 30 and attack_power < 40:
                attack_power = 35
                print("Moderate damage")
            elif attack_power > 15 and attack_power < 30:
                attack_power = 25
                print("Minimal damage")
            else:
                attack_power = 0
                print("MISS!!!")

        if answer.name == 'Satellite Beam':
            attack_power = answer.attack_power + random.randrange(-40, 15)
            if attack_power >= 45:
                attack_power = 50
                print("Critical Hit!")
            elif attack_power >= 35 and attack_power < 45:
                attack_power = 40
                print("Moderate damage")
            elif attack_power > 20 and attack_power < 35:
                attack_power = 30
                print("Minimal damage")
            else:
                attack_power = 0
                print("MISS!!!")
        return attack_power
