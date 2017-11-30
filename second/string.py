# 字符串
name = "add lovelace"
print(name)

# 1.使用方法修改字符串的大小写
name = "add lovelace"
# Add Lovelace title()首字母大写
print(name.title())
# ADD LOVELACE upper()全部大写
print(name.upper())
# add lovelace lower()全部小写
print(name.lower())

# 2.合并（拼接）字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + last_name
print(full_name)

# 3.使用制表符或换行符来添加空白
# \t 制表符（等于Tab键）
print("\tpython")
# \n 换行符
print("\nPython\nJavascript")

# 4.删除空白
favorite_language = " python "
# 右侧删除空白
favorite_language = favorite_language.rstrip()
# 左侧删除空白
favorite_language = favorite_language.lstrip()
# 两端删除空白
favorite_language = favorite_language.strip()
print(favorite_language)