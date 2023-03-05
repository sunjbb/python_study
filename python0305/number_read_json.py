import json

with open('testnumber.json') as file_obj:
    number = json.load(file_obj)

print(number)