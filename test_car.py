import unittest
from datetime import datetime
from model.calliope import Calliope
from model.glissade import Glissade
from model.palindrome import Palindrome
from model.rorschach import Rorschach
from model.thovex import Thovex

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tyres_sensors = [0,0,0,0]

        car = Calliope(current_mileage, last_service_mileage, last_service_date, today, tyres_sensors)
        self.assertTrue(car.service_check())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tyres_sensors = [0,0,0,0]

        car = Calliope(current_mileage, last_service_mileage, last_service_date, today, tyres_sensors)
        self.assertFalse(car.service_check())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tyres_sensors = [0,0,0,0]

        car = Calliope(current_mileage, last_service_mileage, last_service_date, today, tyres_sensors)
        self.assertTrue(car.service_check())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tyres_sensors = [0,0,0,0]

        car = Calliope(current_mileage, last_service_mileage, last_service_date, today, tyres_sensors)
        self.assertFalse(car.service_check())

    def test_tyre_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tyres_sensors = [0,2,0,0]

        car = Calliope(current_mileage, last_service_mileage, last_service_date, today, tyres_sensors)
        self.assertFalse(car.service_check())

    def test_tyre_should_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tyres_sensors = [0,1,0,0]

        car = Calliope(current_mileage, last_service_mileage, last_service_date, today, tyres_sensors)
        self.assertTrue(car.service_check())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tyres_sensors = [0,0,0,0]

        car = Glissade(current_mileage, last_service_mileage, last_service_date, today, tyres_sensors)
        self.assertTrue(car.service_check())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tyres_sensors = [0,0,0,0]
        
        car = Glissade(current_mileage, last_service_mileage, last_service_date, today, tyres_sensors)
        self.assertFalse(car.service_check())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tyres_sensors = [0,0,0,0]
        
        car = Glissade(current_mileage, last_service_mileage, last_service_date, today, tyres_sensors)
        self.assertTrue(car.service_check())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tyres_sensors = [0,0,0,0]
        
        car = Glissade(current_mileage, last_service_mileage, last_service_date, today, tyres_sensors)
        self.assertFalse(car.service_check())

    def test_tyre_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tyres_sensors = [0,2,0,0]

        car = Glissade(current_mileage, last_service_mileage, last_service_date, today, tyres_sensors)
        self.assertFalse(car.service_check())

    def test_tyre_should_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tyres_sensors = [0,1,0,0]

        car = Glissade(current_mileage, last_service_mileage, last_service_date, today, tyres_sensors)
        self.assertTrue(car.service_check())

class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        tyre_sensors = [0,0,0,0]

        car = Palindrome(warning_light_is_on, last_service_date, today, tyre_sensors)
        self.assertTrue(car.service_check())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        tyre_sensors = [0,0,0,0]
        
        car = Palindrome(warning_light_is_on, last_service_date, today, tyre_sensors)
        self.assertFalse(car.service_check())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        warning_light_is_on = True
        tyre_sensors = [0,0,0,0]
        
        car = Palindrome(warning_light_is_on, last_service_date, today, tyre_sensors)
        self.assertTrue(car.service_check())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        warning_light_is_on = False
        tyre_sensors = [0,0,0,0]
        
        car = Palindrome(warning_light_is_on, last_service_date, today, tyre_sensors)
        self.assertFalse(car.service_check())

    def test_tyre_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        warning_light_is_on = False
        tyre_sensors = [0,1.5,0,0]

        car = Palindrome(warning_light_is_on, last_service_date, today, tyre_sensors)
        self.assertFalse(car.service_check())

    def test_tyre_should_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        warning_light_is_on = False
        tyre_sensors = [1,1,1,1]

        car = Palindrome(warning_light_is_on, last_service_date, today, tyre_sensors)
        self.assertTrue(car.service_check())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tyre_sensors = [0,0,0,0]

        car = Rorschach(current_mileage, last_service_mileage, last_service_date, today, tyre_sensors)
        self.assertTrue(car.service_check())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tyre_sensors = [0,0,0,0]

        car = Rorschach(current_mileage, last_service_mileage, last_service_date, today, tyre_sensors)
        self.assertFalse(car.service_check())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tyre_sensors = [0,0,0,0]

        car = Rorschach(current_mileage, last_service_mileage, last_service_date, today, tyre_sensors)
        self.assertTrue(car.service_check())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tyre_sensors = [0,0,0,0]

        car = Rorschach(current_mileage, last_service_mileage, last_service_date, today, tyre_sensors)
        self.assertFalse(car.service_check())

    def test_tyre_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tyres_sensors = [0,2,0,0]

        car = Rorschach(current_mileage, last_service_mileage, last_service_date, today, tyres_sensors)
        self.assertFalse(car.service_check())

    def test_tyre_should_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tyres_sensors = [0,1,1,1]

        car = Rorschach(current_mileage, last_service_mileage, last_service_date, today, tyres_sensors)
        self.assertTrue(car.service_check())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tyre_sensors = [0,0,0,0]

        car = Thovex(current_mileage, last_service_mileage, last_service_date, today, tyre_sensors)
        self.assertTrue(car.service_check())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tyre_sensors = [0,0,0,0]

        car = Thovex(current_mileage, last_service_mileage, last_service_date, today, tyre_sensors)
        self.assertFalse(car.service_check())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tyre_sensors = [0,0,0,0]

        car = Thovex(current_mileage, last_service_mileage, last_service_date, today, tyre_sensors)
        self.assertTrue(car.service_check())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tyre_sensors = [0,0,0,0]

        car = Thovex(current_mileage, last_service_mileage, last_service_date, today, tyre_sensors)
        self.assertFalse(car.service_check())

    def test_tyre_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tyres_sensors = [0,2,0,0]

        car = Thovex(current_mileage, last_service_mileage, last_service_date, today, tyres_sensors)
        self.assertFalse(car.service_check())

    def test_tyre_should_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tyres_sensors = [0,1,0,0]

        car = Thovex(current_mileage, last_service_mileage, last_service_date, today, tyres_sensors)
        self.assertTrue(car.service_check())



if __name__ == '__main__':
    unittest.main()

