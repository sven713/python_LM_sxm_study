# todo: 猜数字异常
import random

userNum = int( input('请输入你猜的数字'))

target = random.randint(1, 100)

while True:

  if target == userNum:
    print('命中！！')
    break
  elif target > userNum:
    print('太小了')
    userNum = int( input('请输入你猜的数字'))


  else :
    print('太大了')
    userNum = int( input('请输入你猜的数字'))

