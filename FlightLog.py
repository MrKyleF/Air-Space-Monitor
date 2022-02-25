#Kyle R Fogerty
#Flight Log: Contains Past Data of Aircraft

from LogEntry import LogEntry
from FlightLogHelper import *
from FlightRadar24.api import FlightRadar24API


class FlightLog:
    #Default Information From Local Database
    def setDefaultInfomation(self):
        self.airline_name, self.callsign, self.country_flag, self.comments, self.full_name = getAirline(iata=self.flight.airline_iata, icao=self.flight.airline_icao)
        self.aircraft_name = getAircraftName(aircraft_code=self.flight.aircraft_code)

    #Create Log Entry For Each Query
    def createLogEntry(self, flight):
        self.logs.append(LogEntry(flight))

    def __init__(self, flight):
        self.flight = flight            #Flight Radar Flight Object
        self.logs = []                  #Logs Of This Aircraft from Queries
        self.createLogEntry(flight)     #Creates First Logs
        self.setDefaultInfomation()     #Sets All Defualt Information From Local Files