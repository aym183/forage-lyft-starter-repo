from abc import ABC
from car import Car
from engine.engine import Engine


class SternmanEngine(Engine, ABC):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def engine_needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False