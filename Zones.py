#Kyle R Fogerty
#Zones: Each Airspaces Flights

from FlightLog import FlightLog
from FlightRadar24.api import FlightRadar24API
from QueryFilter import QueryFilter
fr_api = FlightRadar24API()

class Zone:
    def queryData(self):
        #All Current Flights In Zone
        flights_in_zone = fr_api.get_flights(bounds = self.bounds)
        #Check For Flights Not On List
        for flight in flights_in_zone:
            found = False
            for index in range(0, len(self.flights_flyLogs)):
                #Auto Adds First Element to list
                if len(self.flights_flyLogs) == 0:
                    break
                #Check If Flight Exists and Adds New Entry If Exists
                elif self.flights_flyLogs[index].flight.id == flight.id:
                    found = True
                    self.flights_flyLogs[index].createLogEntry(flight)
                    break
            #Not Found in current list, adding new log
            if found == False:
                self.flights_in_zone.append(flight)
                self.flights_flyLogs.append(FlightLog(flight=flight))
    
    #Search For Certain Aspect In Aircraft
    def searchWithQueryFilter(self):
        if self.query_filter != None:
            self.filtered_in_zone = self.query_filter.checkAllFlightLogs(self.flights_flyLogs)

    def __init__(self, name, bounds, query_filter=QueryFilter()):
        self.name = name                    #Name Of Zone
        self.bounds = bounds                #Zone Bounds
        self.flights_in_zone = []           #All Current Flights Transponding In Zone
        self.flights_flyLogs = []           #Logs Of All Flights In Zone
        self.queryData()                    #Grab All Flights In Zone
        self.filtered_in_zone = []          #List Of Current Flights Fitting Search Parameters
        self.query_filter = query_filter    #Query Filter Currently Being Used, Can Be Set to None to be ignored
        self.searchWithQueryFilter()        #Run Query to populate filtered_in_zone
        


zones = fr_api.get_zones()
Z = None
for zone in zones:
    bounds = fr_api.get_bounds(zones[zone])
    Z = Zone(name=zone, bounds=bounds)
    break

for x in range(0, 3):
    Z.queryData()
    