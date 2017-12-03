# 函数
# 定义函数
def greet_user():
    """显示简单的问候语"""
    print("Hello")

greet_user()

# 向函数传递信息
def greet_user(username):
    print("hello" + username)

greet_user('jesse')

# 默认值
def describe_pet(pet_name,aniaml_type='dog'):
    print("I have a "+aniaml_type)

describe_pet("halo")

# 返回值
def get_formamted_name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name

musician = get_formamted_name('jimi','hendrix')
print(musician)

