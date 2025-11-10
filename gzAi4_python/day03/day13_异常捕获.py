

# try:
#     a = 1/0
#     print(a)
# except:
#     print('a计算出错')

try:
    print(name)

except Exception as e:
# except Exception :

    print(e)

try:
    print(ss)
except Exception as e:
    print(e)
else:
    print('no problem!!')


print('---' * 30)

# 升级猜数字游戏，增加程序健壮性，用户在输入过程中可能不会输入数字或者不按照要求输入，程序要能捕获到用户的异常输入。在已有的猜数游戏中加入异常功能。