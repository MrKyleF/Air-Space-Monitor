#Kyle R Fogerty
#Zone Helper: Helper Functions such as print, tweet
from Tweeter import sendTweet

def fixZoneName(zone_name):
    if zone_name == "europe":
        return "Europe"
    elif zone_name == "northamerica":
        return "North America"
    elif zone_name == "southamerica":
        return "South America"
    elif zone_name == "oceania":
        return "Oceania"
    elif zone_name == "asia":
        return "Asia"
    elif zone_name == "africa":
        return "Africa"
    elif zone_name == "atlantic":
        return "Atlantic"
    elif zone_name == "maldives":
        return "Maldives"
    elif zone_name == "northatlantic":
        return "North Atlantic"
    else:
        return zone_name

def printFlightLogs(zone_name, logs):
    if len(logs) > 0:
        print(fixZoneName(zone_name) + ":")
        print("")
        for flight in logs:
            print(flight.full_name if flight.full_name != None else "Currently Unavailable")
            print(flight.aircraft_name if flight.aircraft_name != None else "Currently Unavailable")
            print(flight.flight.registration)
            print("")
        print("")
        print("")
       

def tweetFlightLogs(zone_name, logs):
    if len(logs) > 0:
        for flight in logs:
            with open('temp_tweet.txt', 'w') as f:
                f.write(fixZoneName(zone_name) + ":" + "\n" + "\n")
                f.write(flight.full_name if flight.full_name != None else "Currently Unavailable")
                f.write("\n")
                f.write(flight.aircraft_name if flight.aircraft_name != None else "Currently Unavailable")
                f.write("\n")
                f.write("Coord: " + str(flight.logs[-1].getCoordinates()))
                f.write(" | Altitude: " + str(flight.logs[-1].getAltitude()))
                f.write(" | Heading: " + str(flight.logs[-1].getHeading()))
                f.write("\n")
                f.write("Registration: #" + flight.flight.registration)
                f.close()
            sendTweet()

