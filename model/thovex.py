from datetime import datetime
from engine.engine_types.capulet_engine import CapuletEngine
from battery.battery_types.nubbin_battery import NubbinBattery

class Thovex():
    def __init__(self, current_mileage, last_service_mileage, last_service_date, today):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.last_service_date = last_service_date
        self.today = today
   
    def service_check(self):
        engine = CapuletEngine(self.current_mileage, self.last_service_mileage)
        battery = NubbinBattery(self.last_service_date, self.today)
        if engine.engine_needs_service() or battery.battery_needs_service():
            return True
        else:
            return False
