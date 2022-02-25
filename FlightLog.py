#Kyle R Fogerty
#Flight Log: Contains Past Data of Aircraft

from LogEntry import LogEntry
from FlightRadar24.api import FlightRadar24API


class FlightLog:
    def setDefaultInfomation(self):
        print("")
    #Create Log Entry For Each Query
    def createLogEntry(self, flight):
        self.logs.append(LogEntry(flight))

    def __init__(self, flight):
        self.flight = flight
        self.logs = []
        self.createLogEntry(flight)