class Restaurant:
    def __init__(self,name,type_name):
        self.name = name
        self.type_name = type_name
        self.number_served = 0
    
    def set_number_served(self,number):
        self.number_served = number
        print(self.number_served)

    def increment_number_served(self,insert_num):
        self.number_served += insert_num
        print(f"就餐人数{self.number_served}")

    def descript_rest(self):
        print(self.name,self.type_name)
    
    def open_rest(self):
        print("营业中。。。。")

class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_num = 0
    
    def descript_rest(self):
        print(self.first_name,self.last_name)
    
    def greet_user(self):
        print(f'你好,{self.first_name}{self.last_name}')

    def do_login(self):
        self.login_num +=1
    
    def reset_login(self):
        self.login_num = 0


rest = Restaurant('如意餐馆', '川菜')
print(rest.name,rest.type_name)
rest.descript_rest()
rest.open_rest()
rest.increment_number_served(2)

rest1 = Restaurant('如意餐馆1', '川菜')
rest1.descript_rest()

rest2 = Restaurant('如意餐馆2', '川菜')
rest2.descript_rest()

user1 = User('章', '三')
user1.descript_rest()

user2 = User('李', '四')
user2.descript_rest()

user1.do_login()
user1.do_login()
user1.do_login()
user1.do_login()
print(user1.login_num)
user1.reset_login()
print(user1.login_num)