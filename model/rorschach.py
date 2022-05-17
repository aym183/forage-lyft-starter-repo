from datetime import datetime
from engine.engine_types.willoughby_engine import WilloughbyEngine
from battery.battery_types.spindler_battery import SpindlerBattery


class Rorschach(WilloughbyEngine, SpindlerBattery):
    def needs_service(self):
        if self.engine_needs_service() and self.battery_needs_service():
            return True
        else:
            return False
