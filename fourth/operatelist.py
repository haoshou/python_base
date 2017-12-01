# 列表操作
# 遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 创建数值列表
# 1.使用函数 range() 能够轻松地生成一系列的数字。
for value in range(1, 5):
    print(value)
# range()只是打印数字1~4
# 2.使用 range()创建数字列表
number = list(range(1, 6))
print(number)
# [1, 2, 3, 4, 5]
# 3.对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
# 4.列表解析 列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素。
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 使用列表的一部分(Python称之为切片)
# 1.切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# 如果你没有指定第一个索引，Python将自动从列表开头开始
print(players[:1])
# 2.遍历切片
for player in players[:3]:
    print(player)
# 3.复制列表
my_food = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_food[:]
print(friend_foods)

# 元组 Python将不能修改的值称为不可变的，而不可变的列表被称为元组。
dimeosions = (200, 50)
print(dimeosions[0])
print(dimeosions[1])
