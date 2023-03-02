def get_user(username):
    print(f"你好 {username}" )

def display_message(date):
    print(f"{date}学习了函数")


# 指出一个宠物属于哪种动物以及它叫什么名字
def decribe_pet(animal_type,pet_name):
    print(f'这个是{animal_type}')
    print(f'{animal_type},name {pet_name.title()}')

decribe_pet('猫', '大菊')
# get_user('ll')
# display_message("金他")
decribe_pet(pet_name='eee',animal_type='test')

# 练习

def make_shirt(size,message='china'):
    print(f'T恤，大小{size},Logo {message.title()}')

make_shirt(2)

def make_album(name,song_name,number=None):
    message = {'name': name, 'song': song_name}
    if number:
        message['number'] = number
    return message

active = True
while active:
    name = input("姓名：")
    song = input("名称：")
    print(make_album(name, song)) 
    message = input("是否退出？Yes/No")
    if message == 'Yes':
        break