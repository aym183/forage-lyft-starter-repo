from datetime import datetime

from engine.engine_types.capulet_engine import CapuletEngine


class Thovex(CapuletEngine):
    def needs_service(self):
        pass
        # service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        # if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
        #     return True
        # else:
        #     return False
