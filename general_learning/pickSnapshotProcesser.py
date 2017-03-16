import json
from pprint import pprint

with open('pickSnapshot.json') as data_file:
    data = json.load(data_file)

#pprint(data[0]["demandId"])
#pprint(data[0]["needByDate"])
#pprint(data[0]["creationDate"])
for demand in data:
    pprint(demand["demandId"])
    pprint(demand["needByDate"])
    pprint(demand["needByDate"])