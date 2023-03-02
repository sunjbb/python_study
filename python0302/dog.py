class Dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name},蹲下')
    
    def roll_over(self):
        print(f'{self.name} 打滚')
my_dog = Dog('大黄', '2')
print(my_dog.age)
my_dog.sit()
my_dog.roll_over()