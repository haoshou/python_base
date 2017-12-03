# if语句
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.lower())

# 检查多个条件
# 1.使用and检查多个条件
age_0 = 22
age_1 = 28
print(age_0 >= 21 and age_1 >=21)
# 使用or检查多个条件
print(age_0 >= 21 or age_1 >= 21)
# 检查特定值是否包含在列表中
print('bmw' in cars)