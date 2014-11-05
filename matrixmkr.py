__author__ = 'user'
import json,csv
"""
json_data=open('data/flight.json')
data = json.load(json_data)

state_ip = [1,2,4,5,6,8,9,10,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,53,54,55,56,72,75,78]
state_ip = [str(x) for x in state_ip]
print state_ip;

flights = []

for ip in state_ip:
    state =[]
    if ip in data:

        for ip2 in state_ip:
            if ip2 in data[ip]:
                state.append(data[ip][ip2]['flight'])
            else:
                state.append(0)

    else:
        state =[0]*len(state_ip)
    flights.append(state)
print flights
"""

#Make state info json
def makeStateJson():
    stateJson ={}

    with open("data/states.csv") as f:
       reader = csv.reader(f,delimiter =",")
       for row in reader:
           stateJson[row[0]] = {"state_name" : row[2],
                                "population" : row[3],
                                "region" : row[4]}
    print stateJson
    with open("data/stateInfo.json","wb") as outfile:
        json.dump(stateJson, outfile,sort_keys=True,indent=4, separators=(',', ': '))

#makeStateJson();

def makePassengerMatrix():
    passenger = {}
    with open("data/flight.csv","rb") as f:
        reader= csv.reader(f,delimiter=",")
        header = reader.next()
        print header
        for row in reader:
            #print row
            #print row[12]
            orginStateID = row[12]
            destStateID = row[19]
            try:

                if row[19] in passenger[row[12]]: # if destiation has shown before
                    passenger[row[12]][row[19]] += int(row[0])
                else:
                    passenger[row[12]][row[19]] = int(row[0])
            except KeyError:
                passenger[row[12]] = {row[19]:int(row[0])}
        print passenger
        with open("data/passengers.json","wb") as outfile:
            json.dump(passenger, outfile,sort_keys=True,indent=4, separators=(',', ': '))
makePassengerMatrix()