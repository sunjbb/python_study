# 任意数量的列表参数,*toppings底层是元组
# def make_pizza(*toppings):
#     print(toppings)
# 多个参数时 必须把可变参数放到最后
def make_pizza(size,*toppings):
    print(size,toppings)

# make_pizza('a')
# make_pizza('a','b')

# user_profile
# **user_info 底层是字典
# def build_profile(first,last,**user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
# user_profile = build_profile('alber', 'eins',location='arms')
# user_profile = build_profile('孙', '家宝',home='无',money='0',car='None')
# print(user_profile)
# # 练习
# def make_smz(*pl):
#     print(pl)

# def make_car(speed,size,**info):
#     info['speed'] = speed
#     info['size'] = size
#     return info
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)