# with open('python0303/test.txt') as file_obj:
#     context = file_obj.read()
# print(context)

with open('python0303/test.txt') as file_obj:
    for line in file_obj:
        print(line)
