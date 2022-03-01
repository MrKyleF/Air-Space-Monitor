#Kyle R Fogerty
#Flight Log Helper: Helper Functions For Flight Log

#getAirline():
##Input: Two Airline Codes
##Output 1: Airline_Name, CallSign, Country_Flag, Comments, Full_Name
##Output 2: None, None, None, None, None
##Dependents: 'Code_Addresses/airline_codes.csv'

#getAircraftName()
##Input: Aircraft_Code, Skip Checking second row
##Ouptut 1: Aircraft_Name
##Output 2: "Raw: (input)"
##Dependents: 'Code_Addresses/aircraft_codes.csv'

#Imports
import csv
from FlightRadar24.api import FlightRadar24API

def getAirline(iata="N/A", icao="N/A"):
    with open('Code_Addresses/airline_codes.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csv_reader:
            if (row[0] == iata and row[0] != "N/A" ) or (row[1] == icao and row[1] != "N/A"):
                airline_name = "N/A" if len(row) <= 2 else (row[2] if row[2] != '' else "N/A")                        #Airline Name From Database File
                callsign = "N/A" if len(row) <= 3 else (row[3] if row[3] != '' else "N/A")                            #Call Sign From Database File
                country_flag = "N/A" if len(row) <= 4 else (row[4] if row[4] != '' else "N/A")                        #Country Flag From Databse File
                comments = "N/A" if len(row) <= 5 else (row[5] if row[5] != '' else "N/A")                            #Comments On Airline From Database File
                full_name = str(airline_name + (": " if comments != "N/A" else "")) if airline_name != "N/A" else ""   
                full_name += (comments) if comments != "N/A" else ""                                                  #Constructed Full Name For Airline
                csvfile.close()
                return airline_name, callsign, country_flag, comments, full_name
    csvfile.close()
    return None, None, None, None, None

def getAircraftName(aircraft_code = "N/A", skip_second_check=False):
    with open('Code_Addresses/aircraft_codes.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csv_reader:
            # Beed to check row 1 first
            if (row[1] == aircraft_code and row[1] != "N/A" ): # or (row[1] == aircraft_code and row[1] != "N/A"):
                aircraft_name = row[2] if row[2] != '' else "N/A"
                csvfile.close()
                return aircraft_name
        csvfile.close()
    with open('Code_Addresses/aircraft_codes.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csv_reader:
            # Beed to check row 1 first
            if (row[0] == aircraft_code and row[0] != "N/A" ): # or (row[1] == aircraft_code and row[1] != "N/A"):
                aircraft_name = row[2] if row[2] != '' else "N/A"
                csvfile.close()
                return aircraft_name
        
        csvfile.close()
    return "Raw: " + aircraft_code                           #Aircraft Not Found In Database File, Return Input With Raw Prefix