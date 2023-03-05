def file_read(file_name='python0304/pl.txt'):
    file_name = file_name
    try:
        with open(file_name,'r',encoding='utf-8') as file_obj:
            print(file_obj.read())
    except FileNotFoundError:
        # pass 什么也不做，简称 过，静默失败
        pass
        # print(f'{file_name}文件不存在')

# 文件不存在时也可跳过这个错误继续向下
file_read()
file_read('python0304/我pl.txt')
file_read('python0304/test_file_write.txt')