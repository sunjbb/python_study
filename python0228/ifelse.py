car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
# and or   不支持 && ||

a = 5
if a < 19:
    print(a)
else:
    print(19)
if a > 18:
    print(a)
elif a < 8:
    print("小孩")
else:
    print("刚刚好")
# 练习

# alien_color = input()
# if alien_color == "green":
#     print("获得5分 ")
# elif alien_color == "yellow":
#     print("获得10分")
# elif alien_color == "red":
#     print("获得15分")

# 数组中是否包含 使用in
# available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"add {requested_topping}")
#     else:
#         print(f"dont have {requested_topping}")
# print("finsh")

players = ["zs",'ls','ww','zl','wmz',"admin"]
user_name = input()
if players:
    if user_name in players and user_name == "admin":
        print("admin VIP")
    elif user_name not in players:
        print("输入错误")
    else:
        print(f"hello {user_name}")
else:
    print("员工为空")





