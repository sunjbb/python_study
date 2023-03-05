# ZeroDivisionError 除0 异常 except
# print(5/0)

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('除数不能为0')

while True:
    first_num = input("请输入第一个数：")
    if first_num == 'q':
        break
    secound_num = input('请输入第二')
    if secound_num == 'q':
        break
    
    try:
        answer = int(first_num)/int(secound_num)
    except ZeroDivisionError:
        print('not 0')
    # 没有异常则输出else中的情况
    else:
        print(answer)
        
    