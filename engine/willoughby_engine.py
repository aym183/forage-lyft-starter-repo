from abc import ABC
from car import Car
from engine.engine import Engine


class WilloughbyEngine(ABC):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        pass
    # def engine_should_be_serviced(self):
    #     return self.current_mileage - self.last_service_mileage > 60000
