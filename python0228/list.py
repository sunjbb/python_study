for num in range(5):
    print(num)
print("--------------")
for num in range(2,5):
    print(num)
print("--------------")
for num in range(2,10,2):
    print(num)
print("--------------")
# 生成的列表转为数组
list_num = list(range(5))
print(list_num)
print("--------------")

print(max(list_num))
print(sum(list_num))
print(min(list_num))
print("--------------")
# 列表解析
squares = [value**2 for value in range(1,10) ]
print(squares)
# 章节练习
# for num in range(1,21):
    # print(num)
# for num in range(1,1000001):
    # print(num)
# print(min(range(1,1000001)),max(range(1,1000001)),sum(range(1,1000001)))

# for num in range(1,21,2):
#     print(num)
# for num in range(3,31,3):
#     print(num)
for num in range(1,11):
    print(num**3)
num_list = [num**3 for num in range(1,11)]
print(num_list)