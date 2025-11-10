# 封装一个函数，参数有两个num1，num2，求两个数的四则运算结果

def siZeYunSuan (num1, num2):
    sum = num1 + num2
    minus = num1 - num2
    cheng = num1 * num2
    chu = num1 / num2
    return  sum, minus, cheng, chu



res = siZeYunSuan(2,1)
print(res)

def return_num():
    return 1
    return 2

result = return_num()
print(result)

def return_num():
    return 1,1,2,3,4,5

result = return_num()
print(result, type(result))


print("-"*50)
def my_if(num):
    if num>=18:
        return "您满18岁了"

    print(f"您的年龄是{num}岁")
    return num


result = my_if(20)
print(result)


def func():
    # 在函数内部定义一个局部变量
    num = 10
    print(f'在局部作用域中调用num局部变量：{num}')

# 调用func函数
func()
# 在全局作用域中调用num局部变量
# print(f'在全局作用域中调用num局部变量：{num}')



num = 10
# 定义一个函数func
def func():
    # 尝试在局部作用域中修改全局变量
    global num
    num = 20

# 调用函数func
func()
# 尝试访问全局变量num
print(num)


my_num_1 = 10

def my_fun():
    # 局部变量：只能在函数内部使用，无法在函数外部使用
    my_num_2 = 100
    print(f"my_num_2的值是{my_num_2}")

    # 如果想在局部地区【修改】全局变量的值，必须使用global关键字修饰。
    # 如果需要使用global关键字修饰全局变量，那么global这句话必须放在该变量首次出现之前
    global my_num_1
    print(f"修改前，my_num_1的值是{my_num_1}")
    my_num_1 += 99
    print(f"修改后，my_num_1的值是{my_num_1}")

my_fun()

print(my_num_1)


my_list = [1,2,3]

def my_fun():
    my_list.append(4)
    my_list.append(5)
    my_list.append(6)
    print(f"函数中打印{my_list}")

my_fun()
print(f"全局打印{my_list}")


def user_info(name, age, address):
    print(f'我的名字{name}，今年{age}岁了，家里住在{address}')

# 调用函数（使用关键词参数）
user_info(name='Tom',  address='美国纽约', age=999)


def user_info(name, age,gender='男' ):
    print(f'我的名字{name}，今年{age}岁了，我的性别为{gender}')

user_info('李林', 25)


def print_user_info(name,age,score,address):
    print(f"我的姓名：{name}，年龄：{age}，考试成绩：{score}，居住地：{address}")

print_user_info("张三",18,99.6,"北京")
print_user_info(18,"张三",99.6,"北京")

# print_user_info(age=18,score=99.6,"张三",address="北京") 报错
print_user_info("张三",age=18,score=99.6,address="北京")


print("-"*50)

def my_sum(*args):
    print("元组的长度是",len(args))
    for i in args:
        print(i)
    return sum(args)

print(my_sum(1, 2,3))
res = sum((11,2))
print(res)

print("-"*50)

def print_user_info(name,age,*args,score=100,**kwargs):
    print(f"我的姓名：{name}，年龄：{age}，考试成绩：{score}")
    print(args,type(args))
    print(kwargs,type(kwargs))

print_user_info("张三",18,1,2,3,score=999,a=99,b=100)



a = 10
print(id(a))


a = 10
b = a
print(id(a))
print(id(b))


a = 10
b = a

a = 100
print(b)  # 10 或 100


print(id(a))
print(id(b))


# 定义一个函数
def func(mynames):
    mynames.append('赵六')


# 定义一个全局变量
names = ['张三', '李四', '王五']
# 调用函数
func(names)

print(names)  # ???


# 定义一个函数
def func(num):
    num += 1
    print(num)


# 定义一个全局变量
a = 10
# 调用函数
func(a)
# 在全局作用域中打印a
print(a)


a = 10
b = 20
a,b = b,a
print(a,b)


a = 10
b = 20
c = 30
print(a,b,c)
a,b,c = b,c,a
print(a,b,c)


def fn1():
    return 100

# 调用fn1函数
print(fn1)  # 返回fn1函数在内存中的地址
print(fn1())


fn = lambda a, b, c=100 : a + b + c
print(fn(10, 20))

lambda_fn_3 = lambda age: "成年了" if age>=18 else "未成年"
print(lambda_fn_3(18))
print(lambda_fn_3(10))