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
    
    def runForLoops(self, loops: int, wait_time=30):
        for loop in range(0, loops):
            self.runDataQueryOnZones()
            self.searchWithQueryFilterOnZones()
            self.printFilteredLogsOnZones()
            print("----------------------------------------------------------------------------------------------")
            print("")
            sleep(wait_time)

ZM = ZoneManager()
ZM.runForLoops(10)