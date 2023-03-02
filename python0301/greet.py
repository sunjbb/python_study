# name = input("请输入内容：")
# print(f"刚刚输入的内容有个：{name}")
# age = int(name)
# print(age)
# index = 0
# while index <= 5:
#     print(index)
#     index+=1
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     print(prompt)
#     message = input(prompt)
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
# 练习

active = True
while  active:
    age = input("请输入年龄")
    if age == 'quit':
        break
    try:
        age = int(age)
    except ValueError:
        print('年龄格式错误')
        continue
    if age < 3:
        print('￥0')
    elif age <18:
        print('$10')
    else:
        print('$15')
