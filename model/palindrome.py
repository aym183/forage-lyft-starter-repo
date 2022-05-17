from datetime import datetime
from engine.engine_types.sternman_engine import SternmanEngine
from battery.battery_types.spindler_battery import SpindlerBattery


class Palindrome(SternmanEngine, SpindlerBattery):
    def needs_service(self):
        if self.engine_needs_service() and self.battery_needs_service():
            return True
        else:
            return False
