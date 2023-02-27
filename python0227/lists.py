# 人员名单
names = ["zs","ls","ww","zl"]
for name in names:
    msg = f"Hello {name}"
    print(msg)
# 新增元素
names.append("zmz")
# 指定位置插入元素
names.insert(0, "xiao0")
print(names)
# 删除指定元素
del names[0]
print(names)
# 弹出指定位置的元素，默认最后一个，弹出后源列表中就没了
names.pop()
print(names)
# 删除指定内容的元素
names.remove("ls")
print(names)

# 排序
# names.sort()
print(names)
print(sorted(names))
print(names)
# # test01 人员名单
# names = ["zs","ls","ww","zl"]
# # 换人
# names[2] = 'w6'
# # 加人
# names.append("q1")
# names.insert(0,"q2")
# names.insert(3,"q3")
# print(names)
# # 只留两个
# while(names.__len__()>2):
#     print(names.pop()+"bye")
# print(names)
# # 清空
# del names[1]
# del names[0]
# print(names)


# test02
    

