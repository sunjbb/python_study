""" 练习汽车类 """
# 三引号是 引用时的提示
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.make},{self.model},{self.year}"
        return long_name.title()
    
    def read_odometer_reading(self):
        print(self.odometer_reading)

    def update_odometer(self,odometer_reading):
        if self.odometer_reading > odometer_reading:
            print("干哈呢，不行阿")
        else:
            self.odometer_reading = odometer_reading
    
# my_new_car = Car('audi', 'a6', '2020')
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 22
# my_new_car.read_odometer_reading()