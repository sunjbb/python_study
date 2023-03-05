import json

user_name = input('你的名字')
with open('user_name.json','w') as file_obj:
    json.dump(user_name,file_obj)
    print(f"{user_name}我记住你了")