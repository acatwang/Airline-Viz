__author__ = 'user'
import json

json_data=open('data/flight.json')
data = json.load(json_data)

state_ip = [1,2,4,5,6,8,9,10,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,53,54,55,56,72,75,78]
state_ip = [str(x) for x in state_ip]
for key in data:
    print key

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
