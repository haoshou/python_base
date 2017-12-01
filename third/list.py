# 列表
# 列表由一系列按特定顺序排列的元素组成。
# 1.访问列表元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# Python特殊语法：最后一个列表元素：索引为-1，负数代表从后面开始数
print(bicycles[-2])
# 索引从0而不是1开始
print(bicycles[0])

# 2.修改、添加和删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# 修改 honda->ducati
motorcycles[0] = 'ducati'
print(motorcycles)
# 添加 ducati到列表末尾
motorcycles.append('ducati')
print(motorcycles)
# 插入元素 根据索引插入元素
motorcycles.insert(0, 'test')
print(motorcycles)
# 删除元素
# 1.使用del语句删除元素（如果知道要删除的元素在列表中的位置，可使用del语句。）
del motorcycles[0]
print(motorcycles)
# 2.使用pop()删除元素
popped_motorcycle = motorcycles.pop()
# pop弹出末尾元素，但是并未删除列表元素
print(popped_motorcycle)
print(motorcycles)
# 3.根据值删除元素
motorcycles.remove('ducati')
print(motorcycles)

# 列表排序
# 1.使用方法 sort()对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
# 按字母顺序排列的，再也无法恢复到原来的排列顺序：
cars.sort()
print(cars)
# 反序 sort()方法传递参数reverse=True。
cars.sort(reverse=True)
print(cars)
# 2.使用函数 sorted()对列表进行临时排序
print(sorted(cars))
# 3.倒着打印列表
cars.reverse()
print(cars)
# 4.确定列表的长度
print(len(cars))
