from datetime import datetime
from engine.engine_types.sternman_engine import SternmanEngine
from battery.battery_types.spindler_battery import SpindlerBattery


class Palindrome():
    def __init__(self, warning_light_is_on, last_service_date, today):
        self.warning_light_is_on = warning_light_is_on
        self.last_service_date = last_service_date
        self.today = today
   
    def service_check(self):
        engine = SternmanEngine(self.warning_light_is_on)
        battery = SpindlerBattery(self.last_service_date, self.today)
        if engine.engine_needs_service() or battery.battery_needs_service():
            return True
        else:
            return False
