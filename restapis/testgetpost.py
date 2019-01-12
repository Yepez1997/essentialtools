import urllib
import sys
import pprint
import json
import json 
import requests


data =  {
    "People":{
        "President": {
            "name": "Zaphod Beebleborx",
            "nickname": "Bete",
            "food": [
                "Nobu"
            ]
        },
        "Secretary": {
            "name": "Beebleborx",
            "nickname": "George",
            "food": [
                "Chickfila",
                "In n Out"
            ]
        }
    }
}


file = "json_test.json"
# first arguement serializes data 
with open((file),"w") as write_file:
    json.dump(data, write_file)

encoded = json.dumps(data, indent=4)
decoded = json.loads(encoded)

with open("json_test.json", "r") as read_file:
    data = json.load(read_file)


# want to create a data structure 
# and their 

people = {}
for i in data['People']:
    for j in data['People'][i]:
        if (j == 'name'):
            people[data['People'][i]['name']] = data['People'][i]['food']

# TO DO unicode - UTF8

file2 = "json_test2.json"
with open((file2),"w") as write_file:
    json.dump(people, write_file)

encoded2 = json.dumps(people, indent=6)
decoded2 = json.loads(encoded2)

print(decoded2)








