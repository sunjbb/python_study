# 一次性读取
# with open('python0304/pl.txt') as file_obj:
#     print(file_obj.read())

# 逐行读取
# with open('python0304/pl.txt') as file_obj:
#     for line in file_obj:
#         print(line.strip())

# 将文件读取并按行存储到列表中
# with open('python0304/pl.txt') as file_obj:
# 解决中文读取问题
# with open('python0304/pl.txt','r',encoding='utf-8') as file_obj:
#     read_lines = file_obj.readlines()

# for line in read_lines:
#     print(line.rstrip())

# # 将内容拼接为一个字符串
# pi_str = ''

# for line in read_lines:
#     pi_str += line.rstrip()

# print(len(pi_str))
# print('st' in pi_str)
# 练习
with open('python0304/pl.txt','r',encoding='utf-8') as file_obj:
    # print(file_obj.read())
    # for line in file_obj.readlines():
    #     print(line.strip())
    lines = file_obj.readlines()

for line in lines:
    print( line.strip().replace('python','C++'))







