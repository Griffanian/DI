import json
data = {}

filename = 'data.json'

with open(filename,'r')as file:
    data=json.load(file)
    
print(data)