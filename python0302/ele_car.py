class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:

    def __init__(self,size=75):
        self.size = size
    
    def desc_battery(self):
        print(f"电池容量{self.size}")

    def get_range(self):
        if self.size == 75:
            range = 160
        elif self.size == 100:
            range = 300
        print(f"续航{range}")

class EleCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
my_tesla = EleCar('tasela', 'models', '2022')
my_tesla.battery.desc_battery()
my_tesla.battery.get_range()

# 练习

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



class IceCreamStand(Restaurant):
    def __init__(self, name, type_name):
        super().__init__(name, type_name)
        self.flavors = ['hgds','xbd','bmy']
    
    def desc_ice(self):
        print(self.flavors)

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ["can add post" ,"can delete post" ,"canban user"]
    
    def show_privileges(self):
        print(self.privileges)

ice = IceCreamStand('肯德基', '连锁商店')
ice.desc_ice()
admin = Admin('zhang', 'qinghe')
admin.show_privileges()