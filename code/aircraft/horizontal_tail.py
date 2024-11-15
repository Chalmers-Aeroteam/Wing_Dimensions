from aircraft.main_wing import MainWing


class HorizontalTail(MainWing):
    def __init__(self, HT_span, c_HT, c_elevator_ratio, L_HT, cv_HT, main_wing):
        super().__init__(main_wing.wing_span, main_wing.wing_cord)
        self.cv_HT= cv_HT
        self.L_HT = L_HT
        # self.S_HT = self.horizontal_tail_area()
        self.HT_span = HT_span
        self.c_HT = c_HT
        self.c_elevator = c_elevator_ratio * c_HT


    def horizontal_tail_area(self):
        return self.cv_HT * self.wing_cord * self.wing_area / self.L_HT

    def elevator_area(self):
        return self.c_elevator*self.HT_span



