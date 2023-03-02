user_0 = {
    'username': 'efermi',
    'first': 'enrcio',
    'last': 'fermi'
}
for key, value in user_0.items():
    print(f'key:{key} value:{value}\n')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# for key,value in favorite_languages.items():
#     print(key.title())

for name in favorite_languages.keys():
    print(name.upper())
# 等同下面写法
# for name in favorite_languages:
#     print(name.upper())    

for value in favorite_languages.values():
    print(value)

user_1 = {
    'username': 'efermi',
    'first': 'enrcio',
    'last': 'fermi'
}

for key,value in user_1.items():
    print(f'{key} todo {value}')

for key in user_1.keys():
    print(key)

for value in user_1.values():
    print(value)

if 'phil' in favorite_languages.keys():
    print('success')