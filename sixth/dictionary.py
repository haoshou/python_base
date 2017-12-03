# 字典 在Python中，字典是一系列键—值对
alien_0 = {'color': 'green', 'point': 5}
print(alien_0['color'])
print(alien_0['point'])

# 添加键—值对
alien_0['x_postion'] = 0
alien_0['y_postion'] = 25
print(alien_0)
# {'color': 'green', 'point': 5, 'x_postion': 0, 'y_postion': 25} 成功添加

# 删除键-值对
del alien_0['point']
print(alien_0)

# 遍历字典
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print('key:' + key)
    print('value:' + value)

# 遍历字典中的所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages.keys():
    print(name)

# 按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(name)

# 遍历字典中的所有值
for language in favorite_languages.values():
    print(language)

