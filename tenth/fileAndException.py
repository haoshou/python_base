# 文件与异常
# 从文件中读取数据
# 读取整个文件
with open('E:\\1.txt') as file_object:
    contents = file_object.read()
    print(contents)


# 逐行读取
filename = 'E:\\1.txt'
with open(filename) as test:
    for line in test:
        print(line)


# 创建一个包含文件各行内容的列表
with open(filename) as file:
    lines = file.readlines()

for line in lines:
    print(line)

# 写入文件
with open(filename,'w') as file_object:
    file_object.write("i love programming")

# 添加到文件
with open(filename,'a') as file_object:
    file_object.write("\ntest add")

# 异常
# ZeroDivisionError
# print(5/0)

# 使用 try-except 代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("不可以除以0")