import json

number = [1,2,3,5]
file_name = 'testnumber.json'
with open(file_name,'w') as file_obj:
    json.dump(number,file_obj)