from datetime import datetime
from engine.engine_types.capulet_engine import CapuletEngine
from battery.battery_types.nubbin_battery import NubbinBattery

class Thovex(CapuletEngine, NubbinBattery):
    def needs_service(self):
        if self.engine_needs_service() and self.battery_needs_service():
            return True
        else:
            return False