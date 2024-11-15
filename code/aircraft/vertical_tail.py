from aircraft.main_wing import MainWing


class VerticalTail(MainWing):
    def __init__(self, VT_span, MAC_VT, c_rudder_ratio, L_VT, cv_VT, main_wing):
        super().__init__(main_wing.wing_span, main_wing.wing_cord)
        self.cv_VT = cv_VT
        self.L_VT = L_VT
        self.VT_span = VT_span
        self.MAC_VT = MAC_VT
        self.c_rudder = c_rudder_ratio*MAC_VT


    def vertical_tail_area(self):
        return self.cv_VT * self.wing_span * self.wing_area / self.L_VT

    def rudder_area(self):
        return self.VT_span*self.c_rudder


