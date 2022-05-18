from abc import ABC
from battery.battery import Battery

class SpindlerBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def battery_needs_service(self):
        date = self.current_date - self.last_service_date
        if (date.days) >= 1095:
            return True
        else:
            return False 