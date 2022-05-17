from datetime import datetime
from engine.engine_types.capulet_engine import CapuletEngine
from battery.battery_types.spindler_battery import SpindlerBattery

class Calliope(CapuletEngine, SpindlerBattery):

    def service_check(self):
        if self.engine_needs_service() and self.battery_needs_service():
            return True
        else:
            return False
