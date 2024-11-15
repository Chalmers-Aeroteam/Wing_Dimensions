

class MainWing:
    def __init__(self, wing_span, wing_cord):
        self.wing_span = wing_span
        self.wing_cord = wing_cord
        self.wing_area = self.wing_area()

    def wing_area(self):
        return self.wing_cord*self.wing_span