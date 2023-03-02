alien_0 = {'color': 'green','points': 5}
print(alien_0['color'],alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 100
print(alien_0)

alien_0['speed'] = 'medium'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] += x_increment
print(f"new position {alien_0['x_position']}")
# 删除键值对
del alien_0["color"]
# get 方式获取值，第一个是key 第二个参数是失败的提示
print(alien_0.get("x_position3",'placeholder'))