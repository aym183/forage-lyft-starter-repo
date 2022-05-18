from datetime import datetime
from engine.engine_types.sternman_engine import SternmanEngine
from battery.battery_types.spindler_battery import SpindlerBattery
from tyres.tyre_types.octoprime_tyres import OctoprimeTyres


class Palindrome():
    def __init__(self, warning_light_is_on, last_service_date, today, tyre_sensors):
        self.warning_light_is_on = warning_light_is_on
        self.last_service_date = last_service_date
        self.today = today
        self.tyre_sensors = tyre_sensors
   
    def service_check(self):
        engine = SternmanEngine(self.warning_light_is_on)
        battery = SpindlerBattery(self.last_service_date, self.today)
        tyre = OctoprimeTyres(self.tyre_sensors)
        if engine.engine_needs_service() or battery.battery_needs_service() or tyre.tyre_needs_service():
            return True
        else:
            return False
