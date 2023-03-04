file_name = 'python0304/test_file_write.txt'
# 写入文件，创建文件或覆盖
# with open(file_name,'w',encoding='utf-8') as file_obj:
#     file_obj.write('123456')
# 为文件追加内容
with open(file_name,'a') as file_obj:
    file_obj.write('789')
# 读取文件
with open(file_name) as file_obj:
    print(file_obj.read())
