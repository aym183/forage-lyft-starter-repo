from abc import ABC
from tyres.tyres import Tyre

class OctoprimeTyres(Tyre, ABC):
    def __init__(self, tyres_array):
        self.tyres_array = tyres_array

    def tyre_needs_service(self):
        for i in self.tyres_array:
            if i < 0 or i > 1:
                return "Invalid"
            elif i>= 0.9:
                return True
            else:
                return False