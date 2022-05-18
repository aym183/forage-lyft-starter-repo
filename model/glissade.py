from datetime import datetime
from engine.engine_types.willoughby_engine import WilloughbyEngine
from battery.battery_types.spindler_battery import SpindlerBattery
from tyres.tyre_types.carrigan_tyres import CarriganTyres


class Glissade():
    def __init__(self, current_mileage, last_service_mileage, last_service_date, today, tyre_sensors):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.last_service_date = last_service_date
        self.today = today
        self.tyre_sensors = tyre_sensors
   
    def service_check(self):
        engine = WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        battery = SpindlerBattery(self.last_service_date, self.today)
        tyre = CarriganTyres(self.tyre_sensors)
        if engine.engine_needs_service() or battery.battery_needs_service() or tyre.tyre_needs_service():
            return True
        else:
            return False
