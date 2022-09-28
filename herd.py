from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs_list = self.dinosaurs()
        self.dinosaur_health = self.dinosaurs_list[0].health + self.dinosaurs_list[1].health + self.dinosaurs_list[2].health

    def dinosaurs(self):
        self.dinosaurs_list = []
        velociraptor = Dinosaur('Velociraptor', 30)
        self.dinosaurs_list.append(velociraptor)
        dilophosaurus = Dinosaur('Dilophosaurus', 35)
        self.dinosaurs_list.append(dilophosaurus)
        t_rex = Dinosaur('T Rex', 40)
        self.dinosaurs_list.append(t_rex)
        return self.dinosaurs_list