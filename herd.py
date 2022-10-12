from dinosaur import Dinosaur
import random

class Herd:
    def __init__(self):
        self.dinosaurs_list = self.dinosaurs()
        self.dinosaur_health = self.dinosaurs_list[0].health + self.dinosaurs_list[1].health + self.dinosaurs_list[2].health

    def dinosaurs(self):
        self.dinosaurs_list = []
        velociraptor = Dinosaur('Velociraptor')
        self.dinosaurs_list.append(velociraptor)
        dilophosaurus = Dinosaur('Dilophosaurus')
        self.dinosaurs_list.append(dilophosaurus)
        t_rex = Dinosaur('T Rex')
        self.dinosaurs_list.append(t_rex)
        return self.dinosaurs_list

    def attack(self):
        attack_power = 0
        self.dinosaur.dinosaurs_list[0].attack_power = Herd.attack_power_generator(Herd)
        ap = int(self.dinosaur.dinosaurs_list[0].attack_power * random.randrange(50, 150) / 100)
        attack_power += ap
        print(f"{self.dinosaur.dinosaurs_list[0].name}'s attack adds {ap} damage")
        self.dinosaur.dinosaurs_list[1].attack_power = Herd.attack_power_generator(Herd)
        ap = int(self.dinosaur.dinosaurs_list[1].attack_power * random.randrange(55, 135) / 100)
        attack_power += ap
        print(f"{self.dinosaur.dinosaurs_list[1].name}'s attack adds {ap} damage")
        self.dinosaur.dinosaurs_list[2].attack_power = Herd.attack_power_generator(Herd)
        ap = int(self.dinosaur.dinosaurs_list[2].attack_power * random.randrange(60, 120) / 100)
        attack_power += ap
        print(f"{self.dinosaur.dinosaurs_list[2].name}'s attack adds {ap} damage\n ")
        return attack_power

    def attack_power_generator(self):
        self.attack_power = random.randrange(-1, 50)
        if self.attack_power > 40:
            self.attack_power = 50
            print("Critical Hit!")
        elif self.attack_power > 30 and self.attack_power <= 40:
            self.attack_power = 40
            print("Powerful Hit!")
        elif self.attack_power > 20 and self.attack_power <= 30:
            self.attack_power = 30
            print("Moderate damage.")
        elif self.attack_power > 10 and self.attack_power <= 20:
            self.attack_power = 20
            print("Weak hit, minimum damage...")
        else:
            self.attack_power = 0
            print("MISS!!!")
        return self.attack_power