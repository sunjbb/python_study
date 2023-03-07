from name_function import get_formatted_name

print('输入姓名')
while True:
    first = input('输入姓')
    if first == 'q':
        break
    last = input('输入名')
    if last == 'q':
        break
    
    format_name = get_formatted_name(first, last)
    print(format_name)
