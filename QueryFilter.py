#Kyle R Fogerty
#QueryFilter: Contains Parameters required to perform filtering

class QueryFilter:
    #Set Keywords that will be searched
    def setKeywords(self):
        if self.category == "miltary": 
            self.keywords = ["force", "army","navy","unit "] #Keywords used to located miltary aircraft
        else:
            self.keywords = []
        
    def __init__(self, category="miltary"):
        self.category = category.lower() #Category Name (lowercased)
        self.setKeywords()
    
    #Check if it is true that this flight log contains keywords else return false
    def checkSingleFlightLog(self, flight_log):
        if flight_log.comments == None and flight_log.airline_name == None:     #Check For none fields
            return False                                                        #Returns False, not in filter
        lowercase_comments = flight_log.comments.lower()
        lowercase_airline_name = flight_log.airline_name.lower()
        for keyword in range(0, len(self.keywords)):
            if self.keywords[keyword] in lowercase_comments or self.keywords[keyword] in lowercase_airline_name:
                return True                                                     #Returns True, in filter

        return False                                                            #Returns False, not in filter

    def checkAllFlightLogs(self, flight_logs):
        keywords_found = []                                     #Flight Logs Containing Keywords
        for flight in flight_logs:                              
            if self.checkSingleFlightLog(flight) == True:       #Check Each Log for Containing Keywords & Append to found list
                keywords_found.append(flight)                   
        
        return keywords_found                                   #Return List of Flights Containing Keywords


