from weapon import Weapon
import random

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = self.weapons_choice()

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