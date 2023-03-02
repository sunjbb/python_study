# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表。
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止。
# 将每个经过验证的用户都移到已验证用户列表中。
while unconfirmed_users:
    user = unconfirmed_users.pop()
    print(f"user {user}")
    confirmed_users.append(user)

for user in confirmed_users:
    print(user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# 练习
sandwich_orders = ['a','b','c','d']
finished_sandwiches = []
for order in sandwich_orders:
    print(order)
    finished_sandwiches.append(sandwich_orders.pop())

for case in finished_sandwiches:
    print(case) 