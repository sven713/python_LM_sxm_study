

# name = input('商品名称')
#
# id = input('商品编号')
#
# price = input('商品价格')
#
# num = input('购买数量')
#
# mony = float(price) * int(num)
#
# print(f'商品名称{name},商品编号{id}, 价格{price}, 应付款{mony}' )


# age = int( input('请输入年龄'))
# if age > 18:
#     print('网吧欢迎你')
# else :
#     print('小年轻,回家学习吧')

# month = int(input('请输入月份'))

# 3,4,5 春天
# 6,7,8 夏天
# 9,10,11 秋天
# 12,1 ,2 冬天


# if month >= 3 and month <= 5:
#     print('春天')
# elif  6<= month and month<= 8:
#     print('夏天')
# elif month >=9 and month <= 11:
#     print('秋天')
# elif month == 12 or month == 1 or month == 2:
#     print('冬天')
# else:
#     print('非法输入')


# 找出三个数字中最小的一个。取三个整数输入，并将它们存储在 number1, number2, 和number2中。
# 使用 "if...elif...else "语句打印它们之间最小的数字

# number1 = int(input('请输入第一个数字'))
# number2 = int(input('请输入第2个数字'))
# number3 = int(input('请输入第3个数字'))
#
# if number1 <= number2 and number1 <= number3:
#     print(f'第一个数字最小{number1}')
# elif number2 <= number1 and number2 <= number3:
#     print(f'第2个数字最小{number2}')
# else:
#     print(f'第3个数字最小{number3}')

#0---------------------------------------------

# 参与游戏的角色有两个（玩家 与 电脑），玩家手工出拳，电脑随机出拳，根据石头剪刀布判断输赢。
#
# 玩家：player（玩家手工输入石头0、剪刀1、布2）
#
# 电脑：computer（随机出拳）
# import  random
#
# user = input('请出拳')
# opts = ['石头', '剪刀','布']
# comp = random.choice(opts)
#
# if user == comp:
#     print('平局')
# elif user == '石头'

#--------------------------------------------

# count = 5
# while count >= 0:
#     print('hello world')
#     # count --
#     count = count -1


#--------------------------------------------
# 使用while循环求1..100的和
# count  = 1
# result = 0
# while count <= 100 :
#     result = result + count
#     count = count + 1
#
#
# print(f'结果{result}')

#--------------------------------------------

# 案例2：求1~100之间，所有偶数的和
# count  = 1
# result = 0
# while count <= 100 :
#     if count % 2 == 0:
#         result = result + count
#
#     count = count + 1
# print(f'结果{result}')
#--------------------------------------------
# 场景一：如果吃的过程中，吃完第三个吃饱了，则不需要再吃第4个和第5个苹果，即是吃苹果的动作停止
#
# i = 1
# while i<= 5:
#     if i == 4:
#         print('吃完三个苹果了,爆了不吃了')
#         break
#
#     print(f'吃第{i}个苹果')
#     i+=1

# --------------------------------------------
# 场景二：如果吃的过程中，吃到第三个吃出一个大虫子..., 是不是这个苹果就不吃了，开始吃第四个苹果



# i = 1
# while i<= 5:
#     if i == 4:
#         print('有个大虫子, 不吃了.跳过')
#         # i += 1
#         continue
#
#     print(f'吃第{i}个苹果')
#     i+=1



# num = 1
# while True:
#     print(f"我跑了多少圈{num}")
#     num += 1
#
#     flag = input("请告诉我什么时候结束")
#     if flag=="finish":
#         break

# --------------------------------------------
# 编写一个Python程序，随机生成一个1到100之间的整数，用户通过输入猜测的数字，
# 程序会根据用户的输入提示“猜大了”、“猜小了”或“猜对了”。用户可以无限次猜测，直到猜对为止。猜对后，程序会提示用户并结束游戏。
import random
target = random.randint(1, 100)
print(f'随机数是{target}')

user = int( input('你猜猜是多少?1~100'))

while user != target:
    if user > target:
        print('太大了')
        user = int(input('你猜猜是多少?1~100'))

    else:
        print('太小了')
        user = int(input('你猜猜是多少?1~100'))

print('猜对了!!!')