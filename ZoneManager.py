#Kyle R Fogerty
#Zone Manager: Handles All The Current Zones

from Zone import Zone
from QueryFilter import QueryFilter
from FlightRadar24.api import FlightRadar24API
from time import sleep
fr_api = FlightRadar24API()

class ZoneManager:
    def createZones(self):
        zones = fr_api.get_zones()
        for zone in zones:
            bounds = fr_api.get_bounds(zones[zone])
            self.zones.append(Zone(name=zone, bounds=bounds))

    def __init__(self, query_filter=QueryFilter()):
        print("Initialization Started...")
        self.query_filter = []
        self.zones = []
        self.createZones()
        print("Initialization Complete: Starting Running...")
        print("")
 
    def runDataQueryOnZones(self):
        for i in range(0, len(self.zones)):
            self.zones[i].queryData()
    
    def searchWithQueryFilterOnZones(self):
        for i in range(0, len(self.zones)):
            self.zones[i].searchWithQueryFilter()

    def printFilteredLogsOnZones(self):
        for i in range(0, len(self.zones)):
            self.zones[i].printFilteredLogs()
    
    def tweetFlightLogsOnZones(self):
        for i in range(0, len(self.zones)):
            _ = self.zones[i].tweetFlightLogs()
    
    def runOneZoneAtTime(self, wait_time=150):
        loop_count = 0
        while True:
            self.zones[loop_count % len(self.zones)].queryData()
            self.zones[loop_count % len(self.zones)].searchWithQueryFilter()
            if self.zones[loop_count % len(self.zones)].tweetFlightLogs() == True:
                sleep(wait_time)
            loop_count += 1
    
    def runForLoops(self, wait_time=600):
        while True:
            self.runDataQueryOnZones()
            self.searchWithQueryFilterOnZones()
            self.tweetFlightLogsOnZones()
            print("----------------------------------------------------------------------------------------------")
            print("")
            sleep(wait_time)