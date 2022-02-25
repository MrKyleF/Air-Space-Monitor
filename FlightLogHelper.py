#Kyle R Fogerty
#Flight Log Helper: Helper Functions For Flight Log

import csv
from FlightRadar24.api import FlightRadar24API

def getAirline(iata="N/A", icao="N/A"):
    with open('Code_Addresses/airline_codes.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csv_reader:
            if (row[0] == iata and row[0] != "N/A" ) or (row[1] == icao and row[1] != "N/A"):
                airline_name = row[2] if row[2] != '' else "N/A"                        #Airline Name From Database File
                callsign = row[3] if row[3] != '' else "N/A"                            #Call Sign From Database File
                country_flag = row[4] if row[4] != '' else "N/A"                        #Country Flag From Databse File
                comments = row[5] if row[5] != '' else "N/A"                            #Comments On Airline From Database File
                full_name = str(airline_name + ": ") if airline_name != "N/A" else ""   
                full_name += (comments) if comments != "N/A" else ""                    #Constructed Full Name For Airline
                return airline_name, callsign, country_flag, comments, full_name
    
    return None, None, None, None, None

def getAircraftName(aircraft_code = "N/A", skip_second_check=False):
    with open('Code_Addresses/aircraft_codes.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        #Check Row 1 For Aircraft Code: Shows All Options
        for row in csv_reader:
            if (row[1] == aircraft_code and row[1] != "N/A"):
                return row[2] if row[2] != '' else "N/A"        #Return Aircraft Name From Database File
        #Check Row 0
        if skip_second_check == False:                          #Can be skipped if values are all being found in check 0
            for row in csv_reader:
                if (row[0] == aircraft_code and row[0] != "N/A" ):
                    return row[2] if row[2] != '' else "N/A"    #Return Aircraft Name From Database File
    
    return "Raw: " + aircraft_code                              #Aircraft Not Found In Database File, Return Input With Raw Prefix