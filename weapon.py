import random

class Weapon:
    def __init__(self, name):
        self.name = name
        self.attack_power = 0

    def weapons_choice(self):
        weapons = []
        lightsaber = Weapon('Lightsaber')
        weapons.append(lightsaber)
        lazer_cannon = Weapon('Lazer Cannon')
        weapons.append(lazer_cannon)
        satellite_beam = Weapon('Satellite Beam')
        weapons.append(satellite_beam)
        answer = input('What weapon do you choose?\nA) Lightsaber\nB) Lazer Cannon\nC) Satellite Beam\n')
        while True:
            if answer == 'A' or answer == 'a' or answer == 'lightsaber' or answer == 'Lightsaber':
                weapons[0].attack_power = Weapon.attack_power_computer(Weapon, 'Lightsaber')
                answer = weapons[0]
                return answer
            elif answer == 'B' or answer == 'b' or answer == 'lazer cannon' or answer == 'Lazer Cannon':
                weapons[1].attack_power = Weapon.attack_power_computer(Weapon, 'Lazer Cannon')
                answer = weapons[1]
                return answer
            elif answer == 'C' or answer == 'c' or answer == 'satellite beam' or answer == 'Satellite Beam':
                weapons[2].attack_power = Weapon.attack_power_computer(Weapon, 'Satellite Beam')
                answer = weapons[2]
                return answer
            else:
                answer = input('Sorry, that was not a valid option. \nWhat weapon do you choose?\nA) Lightsaber\nB) Lazer Cannon\nC) Satellite Beam\n')

    def attack_power_computer(self, weapon):
        if weapon == 'Lightsaber':
            attack_power = random.randrange(-1, 50)
            if attack_power > 30 and attack_power <= 45:
                attack_power = 30
                print("Good hit, Moderate damage.")
            elif attack_power > 20 and attack_power <= 30:
                attack_power = 20
                print("Hit.")
            elif attack_power > 8 and attack_power <= 20:
                attack_power = 10
                print("Weak hit, minimum damage...")
            else:
                attack_power = 0
                print("MISS!!!")
        if weapon == 'Lazer Cannon':
            attack_power = random.randrange(-1, 55)
            if attack_power > 41 and attack_power <= 50:
                attack_power = 50
                print("Critical Hit!")
            elif attack_power > 31 and attack_power <= 40:
                attack_power = 40
                print("Powerful Hit!")
            elif attack_power > 21 and attack_power <= 30:
                attack_power = 30
                print("Moderate damage.")
            elif attack_power > 9 and attack_power <= 20:
                attack_power = 20
                print("Weak hit, minimum damage...")
            else:
                attack_power = 0
                print("MISS!!!")
        if weapon == 'Satellite Beam':
            attack_power = random.randrange(-1, 80)
            if attack_power > 69 and attack_power <= 75:
                attack_power = 70
                print("Monstrous Attack!!")
            elif attack_power > 61 and attack_power <= 68:
                attack_power = 60
                print("Deadly Hit!")
            elif attack_power > 50 and attack_power <= 60:
                attack_power = 50
                print("Critical Hit!")
            elif attack_power > 39 and attack_power <= 49:
                attack_power = 40
                print("Powerful Hit!")
            elif attack_power > 26 and attack_power <= 38:
                attack_power = 30
                print("Moderate damage.")
            elif attack_power > 5 and attack_power <= 25:
                attack_power = 20
                print("Weak hit, minimum damage...")
            else:
                attack_power = 0
                print("MISS!!!")
        return attack_power