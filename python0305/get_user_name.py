import json

file_name = 'user_name.json'

with open(file_name,'r',encoding='utf-8') as file_obj:
    user_name = json.load(file_obj)

print(f'欢迎回来{user_name}')