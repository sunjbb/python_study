# 复制列表
foods = ["KFC","LM","RY","MDL1"]
# 复制，独立的列表，不会受原列表的影响
foods_bak = foods[:]
foods.append("test")  
print(foods)
print(foods_bak)

for food in foods[0:3]:
    print(food)

for food in foods[1:3]:
    print(food)    
for food in foods[-3:]:
    print(food)   