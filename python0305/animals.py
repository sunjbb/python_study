def read_file(file_name):
    try:
        with open(file_name,'r',encoding='utf-8') as file_obj:
            print(file_obj.read())
    except FileNotFoundError:
        pass
        # print(f'{file_name}文件不存在')

read_file('python0305/dogs.txt')
read_file('python0305/cat.txt')