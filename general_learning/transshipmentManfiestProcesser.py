import json
from pprint import pprint

with open('abe2-trans-pretty-full.json') as data_file:
    data = json.load(data_file)

pprint(data["transferDeliveryItems"][0]["fcSku"])
pprint(data["transferDeliveryItems"][0]["distributorReceivedDateTime"])
transferDeliveryItems = data["transferDeliveryItems"]
for item in transferDeliveryItems:
    pprint(item["fcSku"])
    pprint(item["distributorReceivedDateTime"])
