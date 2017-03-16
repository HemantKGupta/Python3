import json
from pprint import pprint

with open('abe2-trans-one-full.json') as data_file:
    data = json.load(data_file)

pprint(data["transferDeliveryItems"][0]["fcSku"])
pprint(data["transferDeliveryItems"][0]["distributorReceivedDateTime"])
for demand in data:
    pprint(demand["demandId"])
    pprint(demand["needByDate"])
    pprint(demand["needByDate"])