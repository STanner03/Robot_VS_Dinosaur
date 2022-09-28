from robot import Robot

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