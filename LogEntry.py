#Kyle R Fogerty
#Log Record of Flight Query

from FlightRadar24.api import FlightRadar24API

class LogEntry:
    def __init__(self, flight):
        self.coordinates = [flight.latitude, flight.longitude]
        self.heading = flight.heading
        self.altitude = flight.altitude
        self.ground_speed = flight.ground_speed
        self.time = flight.time
        self.on_ground = True if flight.on_ground == 1 else False
        self.veritcal_speed = flight.vertical_speed